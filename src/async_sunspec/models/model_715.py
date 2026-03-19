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


class Model715LocRemCtl(IntEnum):
    """
    DER control mode. Enumeration.

    Members:
        REMOTE (int): Remote Control
        LOCAL (int): Local mode is required for manual/maintenance operations. Once invoked, it must be explicitly exited for the inverter to be controlled remotely.
    """
    REMOTE = 0
    LOCAL = 1



class Model715OpCtl(IntEnum):
    """
    Commands to PCS. Enumerated value.

    Members:
        STOP (int): Stop the DER
        START (int): Start the DER
        ENTER_STANDBY (int): Enter Standby Mode
        EXIT_STANDBY (int): Exit Standby Mode
    """
    STOP = 0
    START = 1
    ENTER_STANDBY = 2
    EXIT_STANDBY = 3



class Model715(SunSpecModel, model_name="DERCtl", id=715):
    """
    DER Control

    Attributes:
        LocRemCtl (Model715LocRemCtl): DER control mode. Enumeration.
        DERHb (int): Value is incremented every second by the DER with periodic resets to zero.
        ControllerHb (int): Value is incremented every second by the controller with periodic resets to zero.
        AlarmReset (int): Used to reset any latched alarms. 1 = Reset.
        OpCtl (Model715OpCtl): Commands to PCS. Enumerated value.
    """

    LocRemCtl: Annotated[int, ("SunSpecPoint", {'name': 'LocRemCtl', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    DERHb: Annotated[int, ("SunSpecPoint", {'name': 'DERHb', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    ControllerHb: Annotated[int, ("SunSpecPoint", {'name': 'ControllerHb', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    AlarmReset: Annotated[int, ("SunSpecPoint", {'name': 'AlarmReset', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    OpCtl: Annotated[int, ("SunSpecPoint", {'name': 'OpCtl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]

