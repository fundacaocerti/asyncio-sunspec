# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Server orchestration helpers for the basic SunSpec server example."""

from __future__ import annotations

import asyncio
import logging
from contextlib import suppress

from async_sunspec.server.device import SunSpecServerDevice
from async_sunspec.server.server import SunSpecServer


logger = logging.getLogger(__name__)

try:
    # Package import style: `from examples.basic_server.server import ...`
    from .device import build_example_device, simulate_model_701
except ImportError:
    # Script-local import style used by `examples/basic_server/run.py`.
    from device import build_example_device, simulate_model_701


async def run_sunspec_server(
    host: str,
    port: int,
    device: SunSpecServerDevice,
) -> None:
    """Run the async Modbus TCP SunSpec server with a prepared device."""
    server = SunSpecServer(host=host, port=port, devices=device)
    logger.info("[server] Starting on %s:%d", host, port)
    await server.run()


async def run_basic_server_stack(
    host: str,
    port: int,
    device_id: int,
    address: int,
    update_interval: float,
) -> None:
    """Run server and telemetry simulation tasks together."""
    device, model_701 = build_example_device(device_id=device_id, address=address)
    simulation_task = asyncio.create_task(
        simulate_model_701(model_701, update_interval),
    )
    try:
        await run_sunspec_server(host=host, port=port, device=device)
    finally:
        simulation_task.cancel()
        with suppress(asyncio.CancelledError):
            await simulation_task
