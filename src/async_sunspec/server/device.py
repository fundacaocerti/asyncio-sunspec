# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Expose SunSpec devices through pymodbus server datastore abstractions."""
from __future__ import annotations
from array import array
from typing import Self

from pymodbus.constants import ExcCodes
from pymodbus.datastore import ModbusDeviceContext
from pymodbus.datastore.store import BaseModbusDataBlock

from ..device import SunSpecDevice


class SunSpecArrayDataBlock(BaseModbusDataBlock[array]):
    """Creates a sequential modbus datastore."""

    def __init__(self, address: int, values: array) -> None:
        """Initialize the datastore.

        Args:
            address: The starting address of the datastore.
            values: An ``array.array('H', ...)`` buffer of register values.

        Raises:
            ValueError: If ``values`` is not an ``array.array`` instance.
        """
        self.address = address
        if not isinstance(values, array):
            raise ValueError("Values must be an array.array instance")
        self.values = values
        self.default_value = self.values[0].__class__()

    @classmethod
    def create(cls) -> Self:
        """Create a datastore with the full address space initialised to ``0x00``.

        Returns:
            A new :class:`SunSpecArrayDataBlock` spanning 8192 registers.
        """
        return cls(0x00, array('H', [0x00] * 8192))

    def default(self, count: int, value: int = 0) -> None:
        """Re-initialise every slot to a single default value.

        Args:
            count: Number of register slots to allocate.
            value: The value written to every slot. Defaults to ``0``.
        """
        self.default_value = value
        self.values = array('H', [self.default_value] * count)
        self.address = 0x00

    def reset(self):
        """Reset the datastore to the initialized default value."""
        self.values = array('H', [self.default_value] * len(self.values))

    def getValues(self, address: int, count: int = 1) -> list[int] | ExcCodes:
        """Return a contiguous slice of register values.

        Args:
            address: Absolute starting register address.
            count: Number of consecutive registers to read. Defaults to ``1``.

        Returns:
            A list of register values, or :attr:`ExcCodes.ILLEGAL_ADDRESS` if
            the requested range falls outside the allocated buffer.
        """
        start = address - self.address
        if start < 0 or len(self.values) < start+count:
            return ExcCodes.ILLEGAL_ADDRESS
        return self.values[start : start + count]

    def setValues(self, address: int, values: list[int] | int) -> None | ExcCodes:
        """Write values into a contiguous slice of the register buffer.

        Args:
            address: Absolute starting register address.
            values: A single integer or a list of integers to write.

        Returns:
            ``None`` on success, or :attr:`ExcCodes.ILLEGAL_ADDRESS` if the
            target range falls outside the allocated buffer.
        """
        if not isinstance(values, list):
            values = [values]
        start = address - self.address
        if start < 0 or len(self.values) < start+len(values):
            return ExcCodes.ILLEGAL_ADDRESS
        for i in range(len(values)):
            self.values[start + i] = values[i]
        return None


class SunSpecServerDevice(SunSpecDevice):
    """Specialize :class:`SunSpecDevice` for server context generation."""

    def __init__(self, device_id: int, address: int = 0):
        """Initialize a server-side device wrapper."""
        super().__init__(device_id=device_id, address=address)

    def get_context(self) -> ModbusDeviceContext:
        """Build a ``ModbusDeviceContext`` from the locked device registers."""
        if not self.is_locked:
            raise ValueError(f"Device {self._device_id} must be locked before creating context.")

        if not self._sunspec_models:
            raise ValueError(f"Device {self._device_id} has no models to create context from.")

        store = SunSpecArrayDataBlock(self._address + 1, self._register)
        return ModbusDeviceContext(hr=store)
