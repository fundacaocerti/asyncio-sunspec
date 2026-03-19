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
from enum import IntEnum


class Model10St(IntEnum):
    """
    Overall interface status

    Members:
        DOWN (int): DOWN
        UP (int): UP
        FAULT (int): FAULT
    """
    DOWN = 0
    UP = 1
    FAULT = 2



class Model10Typ(IntEnum):
    """
    Enumerated value.  Type of physical media

    Members:
        UNKNOWN (int): UNKNOWN
        INTERNAL (int): INTERNAL
        TWISTED_PAIR (int): TWISTED_PAIR
        FIBER (int): FIBER
        WIRELESS (int): WIRELESS
    """
    UNKNOWN = 0
    INTERNAL = 1
    TWISTED_PAIR = 2
    FIBER = 3
    WIRELESS = 4



class Model10(SunSpecModel, model_name="model_10", id=10):
    """
    To be included first for a complete interface description

    Attributes:
        St (Model10St): Overall interface status
        Ctl (int): Overall interface control (TBD)
        Typ (Model10Typ): Enumerated value.  Type of physical media
        Pad (int)
    """

    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Typ: Annotated[int, ("SunSpecPoint", {'name': 'Typ', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

