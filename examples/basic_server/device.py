# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Device-building helpers for the basic SunSpec server example.

This module illustrates how a user can:

1. Create a `SunSpecServerDevice`.
2. Populate it with supported models (`Model1`, `Model701`).
3. Drive live value changes in a model over time.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass

from async_sunspec.models.model_1 import Model1
from async_sunspec.models.model_701 import Model701, Model701St
from async_sunspec.server.device import SunSpecServerDevice


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SimStep:
    """Single simulation step for Model 701 values."""

    state: Model701St
    watts: int
    amps: int


def build_example_device(
    device_id: int,
    address: int,
) -> tuple[SunSpecServerDevice, Model701]:
    """Build and return a pre-populated SunSpec server device.

    Returns a tuple with:
    - `SunSpecServerDevice`: the device to expose through Modbus TCP
    - `Model701`: the model instance that will be updated by the simulator
    """
    device = SunSpecServerDevice(device_id=device_id, address=address)

    # Model 1 is mandatory in SunSpec devices and carries common identity info.
    common = Model1(
        Mn="CERTI",
        Md="AsyncSunSpecSrv",
        Opt="basic",
        Vr="0.1b1",
        SN="EXAMPLE-0001",
    )
    device.add_model(common)

    measurements = Model701(
        LNV=220,
        LLV=380,
        Hz=60,
        W=0,
        A=0,
        St=Model701St.OFF,
    )
    device.add_model(measurements)
    return device, measurements


async def simulate_model_701(
    model: Model701,
    interval_seconds: float,
) -> None:
    """Continuously update a `Model701` instance with demo telemetry values."""
    profile = (
        SimStep(state=Model701St.OFF, watts=0, amps=0),
        SimStep(state=Model701St.ON, watts=1200, amps=6),
        SimStep(state=Model701St.ON, watts=1800, amps=8),
        SimStep(state=Model701St.ON, watts=2200, amps=10),
    )
    index = 0
    while True:
        step = profile[index % len(profile)]
        model.St = step.state
        model.W = step.watts
        model.A = step.amps
        logger.debug(
            "[sim] St=%s W=%dW A=%dA (next update in %.1fs)",
            Model701St(model.St).name,
            model.W,
            model.A,
            interval_seconds,
        )
        index += 1
        await asyncio.sleep(interval_seconds)
