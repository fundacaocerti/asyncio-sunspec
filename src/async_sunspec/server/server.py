# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Start an async Modbus TCP server backed by SunSpec server devices."""

from pymodbus.datastore import ModbusServerContext
from pymodbus.server import StartAsyncTcpServer

from async_sunspec.server.device import SunSpecServerDevice


class SunSpecServer:
    """Run a pymodbus TCP server using one or more SunSpec devices."""

    def __init__(self, host: str = "localhost", port: int = 502, *, devices: list[SunSpecServerDevice] | None = None) -> None:
        """Initialize server bind settings and attached devices.

        Args:
            host: IP address or hostname the server will listen on.
                Defaults to ``"localhost"``.
            port: TCP port number. Defaults to ``502``.
            devices: One or more :class:`.SunSpecServerDevice` instances to
                serve.  A single device may be passed directly; it will be
                wrapped in a list automatically.  Defaults to ``None``
                (empty list — :meth:`run` returns immediately).
        """
        self._host = host
        self._port = port
        self._server = None
        self._devices = devices or []
        if isinstance(self._devices, SunSpecServerDevice):
            self._devices = [self._devices]

    async def run(self) -> None:
        """Bind device contexts and serve Modbus TCP requests.

        For each device, calls :meth:`.SunSpecServerDevice.bind_register`,
        :meth:`.SunSpecDevice.lock`, and :meth:`.SunSpecServerDevice.get_context`
        before handing the combined context to
        :func:`pymodbus.server.StartAsyncTcpServer`.

        Note:
            If ``devices`` is empty this coroutine returns immediately
            without starting the server.
        """
        if not self._devices:
            return
        
        contexts = []
        for device in self._devices:
            device.bind_register()
            device.lock()
            ctx = device.get_context()
            contexts.append(ctx)

        single = len(contexts) == 1
        context = ModbusServerContext(devices=contexts[0], single=single)

        await StartAsyncTcpServer(
            context=context,
            address=(self._host, self._port),
        )
        
