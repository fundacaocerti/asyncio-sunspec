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


class Model123Conn(IntEnum):
    """
    Enumerated valued.  Connection control.

    Members:
        DISCONNECT (int): DISCONNECT
        CONNECT (int): CONNECT
    """
    DISCONNECT = 0
    CONNECT = 1



class Model123WMaxLim_Ena(IntEnum):
    """
    Enumerated valued.  Throttle enable/disable control.

    Members:
        DISABLED (int): DISABLED
        ENABLED (int): ENABLED
    """
    DISABLED = 0
    ENABLED = 1



class Model123OutPFSet_Ena(IntEnum):
    """
    Enumerated valued.  Fixed power factor enable/disable control.

    Members:
        DISABLED (int): DISABLED
        ENABLED (int): ENABLED
    """
    DISABLED = 0
    ENABLED = 1



class Model123VArPct_Mod(IntEnum):
    """
    Enumerated value. VAR percent limit mode.

    Members:
        NONE (int): NONE
        WMax (int): WMax
        VArMax (int): VArMax
        VArAval (int): VArAval
    """
    NONE = 0
    WMax = 1
    VArMax = 2
    VArAval = 3



class Model123VArPct_Ena(IntEnum):
    """
    Enumerated valued.  Percent limit VAr enable/disable control.

    Members:
        DISABLED (int): DISABLED
        ENABLED (int): ENABLED
    """
    DISABLED = 0
    ENABLED = 1



class Model123(SunSpecModel, model_name="controls", id=123):
    """
    Immediate Inverter Controls 

    Attributes:
        Conn_WinTms (int): Time window for connect/disconnect.
        Conn_RvrtTms (int): Timeout period for connect/disconnect.
        Conn (Model123Conn): Enumerated valued.  Connection control.
        WMaxLimPct (int): Set power output to specified level.
        WMaxLimPct_WinTms (int): Time window for power limit change.
        WMaxLimPct_RvrtTms (int): Timeout period for power limit.
        WMaxLimPct_RmpTms (int): Ramp time for moving from current setpoint to new setpoint.
        WMaxLim_Ena (Model123WMaxLim_Ena): Enumerated valued.  Throttle enable/disable control.
        OutPFSet (int): Set power factor to specific value - cosine of angle.
        OutPFSet_WinTms (int): Time window for power factor change.
        OutPFSet_RvrtTms (int): Timeout period for power factor.
        OutPFSet_RmpTms (int): Ramp time for moving from current setpoint to new setpoint.
        OutPFSet_Ena (Model123OutPFSet_Ena): Enumerated valued.  Fixed power factor enable/disable control.
        VArWMaxPct (int): Reactive power in percent of WMax.
        VArMaxPct (int): Reactive power in percent of VArMax.
        VArAvalPct (int): Reactive power in percent of VArAval.
        VArPct_WinTms (int): Time window for VAR limit change.
        VArPct_RvrtTms (int): Timeout period for VAR limit.
        VArPct_RmpTms (int): Ramp time for moving from current setpoint to new setpoint.
        VArPct_Mod (Model123VArPct_Mod): Enumerated value. VAR percent limit mode.
        VArPct_Ena (Model123VArPct_Ena): Enumerated valued.  Percent limit VAr enable/disable control.
        WMaxLimPct_SF (int): Scale factor for power output percent.
        OutPFSet_SF (int): Scale factor for power factor.
        VArPct_SF (int): Scale factor for reactive power percent.
    """

    Conn_WinTms: Annotated[int, ("SunSpecPoint", {'name': 'Conn_WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Conn_RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'Conn_RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Conn: Annotated[int, ("SunSpecPoint", {'name': 'Conn', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WMaxLimPct: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: WMaxLimPct_SF
    WMaxLimPct_WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct_WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMaxLimPct_RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct_RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMaxLimPct_RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct_RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMaxLim_Ena: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLim_Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    OutPFSet: Annotated[int, ("SunSpecPoint", {'name': 'OutPFSet', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: OutPFSet_SF
    OutPFSet_WinTms: Annotated[int, ("SunSpecPoint", {'name': 'OutPFSet_WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    OutPFSet_RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'OutPFSet_RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    OutPFSet_RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'OutPFSet_RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    OutPFSet_Ena: Annotated[int, ("SunSpecPoint", {'name': 'OutPFSet_Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    VArWMaxPct: Annotated[int, ("SunSpecPoint", {'name': 'VArWMaxPct', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArPct_SF
    VArMaxPct: Annotated[int, ("SunSpecPoint", {'name': 'VArMaxPct', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArPct_SF
    VArAvalPct: Annotated[int, ("SunSpecPoint", {'name': 'VArAvalPct', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArPct_SF
    VArPct_WinTms: Annotated[int, ("SunSpecPoint", {'name': 'VArPct_WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VArPct_RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'VArPct_RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VArPct_RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'VArPct_RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VArPct_Mod: Annotated[int, ("SunSpecPoint", {'name': 'VArPct_Mod', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VArPct_Ena: Annotated[int, ("SunSpecPoint", {'name': 'VArPct_Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WMaxLimPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    OutPFSet_SF: Annotated[int, ("SunSpecPoint", {'name': 'OutPFSet_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VArPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'VArPct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]

