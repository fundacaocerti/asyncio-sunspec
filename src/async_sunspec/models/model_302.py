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


class Model302RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        GHI (int): Global Horizontal Irradiance
        POAI (int): Plane-of-Array Irradiance
        DFI (int): Diffuse Irradiance
        DNI (int): Direct Normal Irradiance
        OTI (int): Other Irradiance
    """

    GHI: Annotated[int, ("SunSpecPoint", {'name': 'GHI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    POAI: Annotated[int, ("SunSpecPoint", {'name': 'POAI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    DFI: Annotated[int, ("SunSpecPoint", {'name': 'DFI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    DNI: Annotated[int, ("SunSpecPoint", {'name': 'DNI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    OTI: Annotated[int, ("SunSpecPoint", {'name': 'OTI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]


class Model302(SunSpecModel, model_name="irradiance", id=302):
    """
    Include to support various irradiance measurements
    """

    repeating: Annotated[Model302RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model302RepeatingGroup})]

