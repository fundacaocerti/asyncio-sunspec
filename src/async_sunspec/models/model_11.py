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


class Model11CfgSt(IntFlag):
    """
    Bitmask values Interface flags.

    Members:
        LINK (int): LINK
        FULL_DUPLEX (int): FULL_DUPLEX
        AUTO_NEG1 (int): AUTO_NEG1
        AUTO_NEG2 (int): AUTO_NEG2
        AUTO_NEG3 (int): AUTO_NEG3
        RESET_REQUIRED (int): RESET_REQUIRED
        HW_FAULT (int): HW_FAULT
    """
    LINK = 1 << 0
    FULL_DUPLEX = 1 << 1
    AUTO_NEG1 = 1 << 2
    AUTO_NEG2 = 1 << 3
    AUTO_NEG3 = 1 << 4
    RESET_REQUIRED = 1 << 5
    HW_FAULT = 1 << 6



class Model11St(IntEnum):
    """
    Enumerated value. State information for this interface

    Members:
        UNKNOWN (int): UNKNOWN
        ENABLED (int): ENABLED
        DISABLED (int): DISABLED
        TESTING (int): TESTING
    """
    UNKNOWN = 0
    ENABLED = 1
    DISABLED = 2
    TESTING = 3



class Model11Ctl(IntFlag):
    """
    Control flags

    Members:
        AUTO (int): AUTO
        FULL_DUPLEX (int): FULL_DUPLEX
    """
    AUTO = 1 << 0
    FULL_DUPLEX = 1 << 1



class Model11(SunSpecModel, model_name="model_11", id=11):
    """
    Include to support a wired ethernet port

    Attributes:
        Spd (int): Interface speed in Mb/s
        CfgSt (Model11CfgSt): Bitmask values Interface flags.
        St (Model11St): Enumerated value. State information for this interface
        MAC (str): IEEE MAC address of this interface
        Nam (str): Interface name (8 chars)
        Ctl (Model11Ctl): Control flags
        FrcSpd (int): Forced interface speed in Mb/s when AUTO is disabled
    """

    Spd: Annotated[int, ("SunSpecPoint", {'name': 'Spd', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CfgSt: Annotated[int, ("SunSpecPoint", {'name': 'CfgSt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    MAC: Annotated[str, ("SunSpecPoint", {'name': 'MAC', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False})]
    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    FrcSpd: Annotated[int, ("SunSpecPoint", {'name': 'FrcSpd', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]

