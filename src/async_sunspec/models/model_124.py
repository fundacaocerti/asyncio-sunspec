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


class Model124StorCtl_Mod(IntFlag):
    """
    Activate hold/discharge/charge storage control mode. Bitfield value.

    Members:
        CHARGE (int): CHARGE
        DiSCHARGE (int): DiSCHARGE
    """
    CHARGE = 1 << 0
    DiSCHARGE = 1 << 1



class Model124ChaSt(IntEnum):
    """
    Charge status of storage device. Enumerated value.

    Members:
        OFF (int): OFF
        EMPTY (int): EMPTY
        DISCHARGING (int): DISCHARGING
        CHARGING (int): CHARGING
        FULL (int): FULL
        HOLDING (int): HOLDING
        TESTING (int): TESTING
    """
    OFF = 1
    EMPTY = 2
    DISCHARGING = 3
    CHARGING = 4
    FULL = 5
    HOLDING = 6
    TESTING = 7



class Model124ChaGriSet(IntEnum):
    """
    Members:
        PV (int): PV
        GRID (int): GRID
    """
    PV = 0
    GRID = 1



class Model124(SunSpecModel, model_name="storage_basic", id=124):
    """
    Basic Storage Controls 

    Attributes:
        WChaMax (int): Setpoint for maximum charge.
        WChaGra (int): Setpoint for maximum charging rate. Default is MaxChaRte.
        WDisChaGra (int): Setpoint for maximum discharge rate. Default is MaxDisChaRte.
        StorCtl_Mod (Model124StorCtl_Mod): Activate hold/discharge/charge storage control mode. Bitfield value.
        VAChaMax (int): Setpoint for maximum charging VA.
        MinRsvPct (int): Setpoint for minimum reserve for storage as a percentage of the nominal maximum storage.
        ChaState (int): Currently available energy as a percent of the capacity rating.
        StorAval (int): State of charge (ChaState) minus storage reserve (MinRsvPct) times capacity rating (AhrRtg).
        InBatV (int): Internal battery voltage.
        ChaSt (Model124ChaSt): Charge status of storage device. Enumerated value.
        OutWRte (int): Percent of max discharge rate.
        InWRte (int): Percent of max charging rate.
        InOutWRte_WinTms (int): Time window for charge/discharge rate change.
        InOutWRte_RvrtTms (int): Timeout period for charge/discharge rate.
        InOutWRte_RmpTms (int): Ramp time for moving from current setpoint to new setpoint.
        ChaGriSet (Model124ChaGriSet)
        WChaMax_SF (int): Scale factor for maximum charge.
        WChaDisChaGra_SF (int): Scale factor for maximum charge and discharge rate.
        VAChaMax_SF (int): Scale factor for maximum charging VA.
        MinRsvPct_SF (int): Scale factor for minimum reserve percentage.
        ChaState_SF (int): Scale factor for available energy percent.
        StorAval_SF (int): Scale factor for state of charge.
        InBatV_SF (int): Scale factor for battery voltage.
        InOutWRte_SF (int): Scale factor for percent charge/discharge rate.
    """

    WChaMax: Annotated[int, ("SunSpecPoint", {'name': 'WChaMax', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: WChaMax_SF
    WChaGra: Annotated[int, ("SunSpecPoint", {'name': 'WChaGra', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: WChaDisChaGra_SF
    WDisChaGra: Annotated[int, ("SunSpecPoint", {'name': 'WDisChaGra', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: WChaDisChaGra_SF
    StorCtl_Mod: Annotated[int, ("SunSpecPoint", {'name': 'StorCtl_Mod', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    VAChaMax: Annotated[int, ("SunSpecPoint", {'name': 'VAChaMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VAChaMax_SF
    MinRsvPct: Annotated[int, ("SunSpecPoint", {'name': 'MinRsvPct', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: MinRsvPct_SF
    ChaState: Annotated[int, ("SunSpecPoint", {'name': 'ChaState', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: ChaState_SF
    StorAval: Annotated[int, ("SunSpecPoint", {'name': 'StorAval', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: StorAval_SF
    InBatV: Annotated[int, ("SunSpecPoint", {'name': 'InBatV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: InBatV_SF
    ChaSt: Annotated[int, ("SunSpecPoint", {'name': 'ChaSt', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    OutWRte: Annotated[int, ("SunSpecPoint", {'name': 'OutWRte', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: InOutWRte_SF
    InWRte: Annotated[int, ("SunSpecPoint", {'name': 'InWRte', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: InOutWRte_SF
    InOutWRte_WinTms: Annotated[int, ("SunSpecPoint", {'name': 'InOutWRte_WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    InOutWRte_RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'InOutWRte_RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    InOutWRte_RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'InOutWRte_RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ChaGriSet: Annotated[int, ("SunSpecPoint", {'name': 'ChaGriSet', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WChaMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'WChaMax_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    WChaDisChaGra_SF: Annotated[int, ("SunSpecPoint", {'name': 'WChaDisChaGra_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VAChaMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'VAChaMax_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    MinRsvPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'MinRsvPct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    ChaState_SF: Annotated[int, ("SunSpecPoint", {'name': 'ChaState_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    StorAval_SF: Annotated[int, ("SunSpecPoint", {'name': 'StorAval_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    InBatV_SF: Annotated[int, ("SunSpecPoint", {'name': 'InBatV_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    InOutWRte_SF: Annotated[int, ("SunSpecPoint", {'name': 'InOutWRte_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]

