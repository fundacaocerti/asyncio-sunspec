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
from enum import IntEnum, IntFlag


class Model125ModEna(IntFlag):
    """
    Is price-based charge/discharge mode active?

    Members:
        ENABLE (int): ENABLE
    """
    ENABLE = 1 << 0



class Model125SigType(IntEnum):
    """
    Meaning of the pricing signal. When a Price schedule is used, type must match the schedule range variable description.

    Members:
        UNKNOWN (int): UNKNOWN
        ABSOLUTE (int): ABSOLUTE
        RELATIVE (int): RELATIVE
        MULTIPLIER (int): MULTIPLIER
        LEVEL (int): LEVEL
    """
    UNKNOWN = 0
    ABSOLUTE = 1
    RELATIVE = 2
    MULTIPLIER = 3
    LEVEL = 4



class Model125(SunSpecModel, model_name="pricing", id=125):
    """
    Pricing Signal  

    Attributes:
        ModEna (Model125ModEna): Is price-based charge/discharge mode active?
        SigType (Model125SigType): Meaning of the pricing signal. When a Price schedule is used, type must match the schedule range variable description.
        Sig (int): Utility/ESP specific pricing signal. Content depends on pricing signal type. When H/M/L type is specified. Low=0; Med=1; High=2.
        WinTms (int): Time window for charge/discharge pricing change.
        RvtTms (int): Timeout period for charge/discharge pricing change.
        RmpTms (int): Ramp time for moving from current charge or discharge level to new level.
        Sig_SF (int): Pricing signal scale factor.
        Pad (int)
    """

    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    SigType: Annotated[int, ("SunSpecPoint", {'name': 'SigType', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Sig: Annotated[int, ("SunSpecPoint", {'name': 'Sig', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Sig_SF
    WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Sig_SF: Annotated[int, ("SunSpecPoint", {'name': 'Sig_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

