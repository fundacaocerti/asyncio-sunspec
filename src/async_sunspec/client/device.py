# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Provide an async Modbus TCP client for SunSpec discovery and reads."""

import logging
from array import array
from typing import Optional

from pymodbus.client import AsyncModbusTcpClient

logger = logging.getLogger(__name__)

from ..device import SUNSPEC_END_MODEL, SUNSPEC_HEADER, SunSpecDevice
from ..model import SunSpecModel


class SunSpecClient:
    """Talk to a SunSpec device over Modbus TCP."""

    def __init__(self, host: str, port: int = 502) -> None:
        """Prepare client settings without creating the underlying transport.

        The actual :class:`pymodbus.client.AsyncModbusTcpClient` instance is
        created lazily by :meth:`connect` to avoid requiring a running
        event loop at construction time (useful for unit tests).

        Args:
            host: Hostname or IP address of the Modbus TCP server.
            port: TCP port number. Defaults to ``502``.
        """
        self._host = host
        self._port = port
        self._client: Optional[AsyncModbusTcpClient] = None

    async def connect(self) -> None:
        """Open the TCP connection to the target Modbus server.

        Raises:
            ConnectionError: If the underlying pymodbus client cannot
                establish a connection.
        """
        if self._client is None:
            self._client = AsyncModbusTcpClient(self._host, port=self._port)
        await self._client.connect()

    def close(self) -> None:
        """Close the TCP connection."""
        if self._client is None:
            return
        self._client.close()

    @property
    def connected(self) -> bool:
        """Return whether the underlying client is connected."""
        return bool(self._client and getattr(self._client, "connected", False))

    async def _read_registers(self, address: int, count: int, device_id: int) -> list[int]:
        """Read a contiguous range of holding registers.

        Args:
            address: Absolute starting register address.
            count: Number of consecutive registers to read.
            device_id: Modbus unit/device identifier.

        Returns:
            A list of ``count`` unsigned 16-bit register values.

        Raises:
            IOError: If the Modbus response indicates an error.
        """
        response = await self._client.read_holding_registers(
            address, count=count, device_id=device_id,
        )
        if response.isError():
            raise IOError(f"Modbus read error at address {address}: {response}")
        return response.registers

    async def scan(self, device_id: int = 1, address: int = 40000) -> SunSpecDevice:
        """Scan and discover all supported models from a SunSpec address block.

        Reads the SunSpec header at ``address``, then iterates through
        consecutive model headers until the end-of-models marker
        (``0xFFFF``) is found.  Models whose IDs are not in
        :meth:`.SunSpecModel.get_model_class` are skipped silently.

        Args:
            device_id: Modbus unit identifier. Defaults to ``1``.
            address: Register address where the SunSpec ``"SuNs"`` header
                is expected. Defaults to ``40000``.

        Returns:
            A :class:`.SunSpecDevice` populated with all discovered and
            supported model instances.

        Raises:
            ValueError: If the SunSpec identifier is not found at
                ``address``.
            IOError: If any Modbus read fails.
        """
        header = await self._read_registers(address, 2, device_id)
        if tuple(header) != SUNSPEC_HEADER:
            raise ValueError(
                f"SunSpec identifier not found at address {address}: "
                f"expected {SUNSPEC_HEADER}, got {tuple(header)}"
            )

        device = SunSpecDevice(device_id=device_id, address=address)
        offset = address + 2

        while True:
            header = await self._read_registers(offset, 2, device_id)
            model_id, model_length = header[0], header[1]
            logger.debug("Found model ID=%d length=%d at address=%d", model_id, model_length, offset)

            if model_id == SUNSPEC_END_MODEL[0]:
                logger.debug("End of models reached at address=%d", offset)
                break

            model_cls = SunSpecModel.get_model_class(model_id)
            if model_cls is None:
                offset += 2 + model_length
                continue

            model = model_cls()
            model.process_elements()

            total_regs = 2 + model_length
            regs = await self._read_registers(offset, total_regs, device_id)

            register = array('H', regs)
            model.offset = offset - address
            model.read_from_register(register)

            device.add_model(model)
            offset += total_regs

        return device

    async def read_model(self, device: SunSpecDevice, model_id: int) -> SunSpecModel:
        """Refresh one discovered model from the remote device.

        Args:
            device: A :class:`.SunSpecDevice` previously returned by
                :meth:`scan`.
            model_id: Numeric SunSpec model identifier to refresh.

        Returns:
            The updated :class:`.SunSpecModel` instance.

        Raises:
            KeyError: If ``model_id`` was not discovered during :meth:`scan`.
            IOError: If the Modbus read fails.
        """
        model = device._sunspec_models.get(model_id)
        if model is None:
            raise KeyError(f"Model {model_id} not found on device {device.device_id}")

        total_regs = 2 + model.L
        regs = await self._read_registers(
            device.address + model.offset, total_regs, device.device_id,
        )

        register = array('H', regs)
        model.read_from_register(register)
        return model

    async def read_all(self, device: SunSpecDevice) -> None:
        """Refresh all discovered models from the remote device.

        Calls :meth:`read_model` for every model registered on ``device``.

        Args:
            device: A :class:`.SunSpecDevice` previously returned by
                :meth:`scan`.

        Raises:
            IOError: If any individual model read fails.
        """
        for model_id in device._sunspec_models:
            await self.read_model(device, model_id)
