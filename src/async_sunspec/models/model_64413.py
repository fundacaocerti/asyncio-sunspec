# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************

from async_sunspec.model import SunSpecModel
from async_sunspec.group import SunSpecGroup, SunSpecRepeatingBlock
from typing import Annotated


class Model64413IvGroup(SunSpecGroup):
    """
    Attributes:
        P (float): Power
        I (float): Current
        V (float): Voltage
    """

    P: Annotated[float, ("SunSpecPoint", {'name': 'P', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    I: Annotated[float, ("SunSpecPoint", {'name': 'I', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    V: Annotated[float, ("SunSpecPoint", {'name': 'V', 'ptype': 'float32', 'mandatory': False, 'static': False})]


class Model64413(SunSpecModel, model_name="PVSimCurves", id=64413):
    """
    Current-Voltage and Power-Voltage Profiles for PV Simulation.

    Attributes:
        IVLen (int): Number of points in the IV curve.
        Irr (int): Plane of Array Irradiance
        Irr_SF (int)
    """

    IVLen: Annotated[int, ("SunSpecPoint", {'name': 'IVLen', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Irr: Annotated[int, ("SunSpecPoint", {'name': 'Irr', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: Irr_SF
    Irr_SF: Annotated[int, ("SunSpecPoint", {'name': 'Irr_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    IV: Annotated[SunSpecRepeatingBlock[Model64413IvGroup], ("SunSpecRepeatingBlock", {"name": "IV", "ptype": "group", "group_type": Model64413IvGroup, "counter": "IVLen"})]

