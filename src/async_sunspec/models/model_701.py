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


class Model701ACType(IntEnum):
    """
    AC wiring type.

    Members:
        SINGLE_PHASE (int): Single Phase
        SPLIT_PHASE (int): Split Phase
        THREE_PHASE (int): Three Phase
    """
    SINGLE_PHASE = 0
    SPLIT_PHASE = 1
    THREE_PHASE = 2



class Model701St(IntEnum):
    """
    Operating state of the DER.

    Members:
        OFF (int): Off
        ON (int): On
    """
    OFF = 0
    ON = 1



class Model701InvSt(IntEnum):
    """
    Enumerated value.  Inverter state.

    Members:
        OFF (int): OFF
        SLEEPING (int): SLEEPING
        STARTING (int): STARTING
        RUNNING (int): RUNNING
        THROTTLED (int): THROTTLED
        SHUTTING_DOWN (int): SHUTTING_DOWN
        FAULT (int): FAULT
        STANDBY (int): STANDBY
    """
    OFF = 0
    SLEEPING = 1
    STARTING = 2
    RUNNING = 3
    THROTTLED = 4
    SHUTTING_DOWN = 5
    FAULT = 6
    STANDBY = 7



class Model701ConnSt(IntEnum):
    """
    Grid connection state of the DER.

    Members:
        DISCONNECTED (int): Disconnected from the grid.
        CONNECTED (int): Connected to the grid.
    """
    DISCONNECTED = 0
    CONNECTED = 1



class Model701Alrm(IntFlag):
    """
    Active alarms for the DER.

    Members:
        GROUND_FAULT (int): Ground Fault
        DC_OVER_VOLT (int): DC Over Voltage
        AC_DISCONNECT (int): AC Disconnect Open
        DC_DISCONNECT (int): DC Disconnect Open
        GRID_DISCONNECT (int): Grid Disconnect
        CABINET_OPEN (int): Cabinet Open
        MANUAL_SHUTDOWN (int): Manual Shutdown
        OVER_TEMP (int): Over Temperature
        OVER_FREQUENCY (int): Frequency Above Limit
        UNDER_FREQUENCY (int): Frequency Under Limit
        AC_OVER_VOLT (int): AC Voltage Above Limit
        AC_UNDER_VOLT (int): AC Voltage Under Limit
        BLOWN_STRING_FUSE (int): Blown String Fuse On Input
        UNDER_TEMP (int): Under Temperature
        MEMORY_LOSS (int): Generic Memory Or Communication Error (Internal)
        HW_TEST_FAILURE (int): Hardware Test Failure
        MANUFACTURER_ALRM (int): Manufacturer alarm, see ManAlrmInfo field for more information.
    """
    GROUND_FAULT = 1 << 0
    DC_OVER_VOLT = 1 << 1
    AC_DISCONNECT = 1 << 2
    DC_DISCONNECT = 1 << 3
    GRID_DISCONNECT = 1 << 4
    CABINET_OPEN = 1 << 5
    MANUAL_SHUTDOWN = 1 << 6
    OVER_TEMP = 1 << 7
    OVER_FREQUENCY = 1 << 8
    UNDER_FREQUENCY = 1 << 9
    AC_OVER_VOLT = 1 << 10
    AC_UNDER_VOLT = 1 << 11
    BLOWN_STRING_FUSE = 1 << 12
    UNDER_TEMP = 1 << 13
    MEMORY_LOSS = 1 << 14
    HW_TEST_FAILURE = 1 << 15
    MANUFACTURER_ALRM = 1 << 16



class Model701DERMode(IntFlag):
    """
    Current operational characteristics of the DER.

    Members:
        GRID_FOLLOWING (int): The DER is operating as part of a larger grid.
        GRID_FORMING (int): The DER is providing the grid.
        PV_CLIPPED (int): The PV output is clipped.
    """
    GRID_FOLLOWING = 1 << 0
    GRID_FORMING = 1 << 1
    PV_CLIPPED = 1 << 2



class Model701ThrotSrc(IntFlag):
    """
    Active throttling source.

    Members:
        MAX_W (int): MAX_W
        FIXED_W (int): FIXED_W
        FIXED_VAR (int): FIXED_VAR
        FIXED_PF (int): FIXED_PF
        VOLT_VAR (int): VOLT_VAR
        FREQ_WATT (int): FREQ_WATT
        DYN_REACT_CURR (int): DYN_REACT_CURR
        LVRT (int): LVRT
        HVRT (int): HVRT
        WATT_VAR (int): WATT_VAR
        VOLT_WATT (int): VOLT_WATT
        SCHEDULED (int): SCHEDULED
        LFRT (int): LFRT
        HFRT (int): HFRT
        DERATED (int): DERATED
    """
    MAX_W = 1 << 0
    FIXED_W = 1 << 1
    FIXED_VAR = 1 << 2
    FIXED_PF = 1 << 3
    VOLT_VAR = 1 << 4
    FREQ_WATT = 1 << 5
    DYN_REACT_CURR = 1 << 6
    LVRT = 1 << 7
    HVRT = 1 << 8
    WATT_VAR = 1 << 9
    VOLT_WATT = 1 << 10
    SCHEDULED = 1 << 11
    LFRT = 1 << 12
    HFRT = 1 << 13
    DERATED = 1 << 14



class Model701(SunSpecModel, model_name="DERMeasureAC", id=701):
    """
    DER AC measurement model.

    Attributes:
        ACType (Model701ACType): AC wiring type.
        St (Model701St): Operating state of the DER.
        InvSt (Model701InvSt): Enumerated value.  Inverter state.
        ConnSt (Model701ConnSt): Grid connection state of the DER.
        Alrm (Model701Alrm): Active alarms for the DER.
        DERMode (Model701DERMode): Current operational characteristics of the DER.
        W (int): Total active power. Active power is positive for DER generation and negative for absorption.
        VA (int): Total apparent power.
        Var (int): Total reactive power.
        PF (int): Power factor. The sign of power factor should be the sign of active power.
        A (int): Total AC current.
        LLV (int): Line to line AC voltage as an average of active phases.
        LNV (int): Line to neutral AC voltage as an average of active phases.
        Hz (int): AC frequency.
        TotWhInj (int): Total active energy injected (Quadrants 1 & 4).
        TotWhAbs (int): Total active energy absorbed (Quadrants 2 & 3).
        TotVarhInj (int): Total reactive energy injected (Quadrants 1 & 2).
        TotVarhAbs (int): Total reactive energy absorbed (Quadrants 3 & 4).
        TmpAmb (int): Ambient temperature.
        TmpCab (int): Cabinet temperature.
        TmpSnk (int): Heat sink temperature.
        TmpTrns (int): Transformer temperature.
        TmpSw (int): IGBT/MOSFET temperature.
        TmpOt (int): Other temperature.
        WL1 (int): Active power L1.
        VAL1 (int): Apparent power L1.
        VarL1 (int): Reactive power L1.
        PFL1 (int): Power factor phase L1.
        AL1 (int): Current phase L1.
        VL1L2 (int): Phase voltage L1-L2.
        VL1 (int): Phase voltage L1-N.
        TotWhInjL1 (int): Total active energy injected L1.
        TotWhAbsL1 (int): Total active energy absorbed L1.
        TotVarhInjL1 (int): Total reactive energy injected L1.
        TotVarhAbsL1 (int): Total reactive energy absorbed L1.
        WL2 (int): Active power L2.
        VAL2 (int): Apparent power L2.
        VarL2 (int): Reactive power L2.
        PFL2 (int): Power factor L2.
        AL2 (int): Current L2.
        VL2L3 (int): Phase voltage L2-L3.
        VL2 (int): Phase voltage L2-N.
        TotWhInjL2 (int): Total active energy injected L2.
        TotWhAbsL2 (int): Total active energy absorbed L2.
        TotVarhInjL2 (int): Total reactive energy injected L2.
        TotVarhAbsL2 (int): Total reactive energy absorbed L2.
        WL3 (int): Active power L3.
        VAL3 (int): Apparent power L3.
        VarL3 (int): Reactive power L3.
        PFL3 (int): Power factor L3.
        AL3 (int): Current L3.
        VL3L1 (int): Phase voltage L3-L1.
        VL3 (int): Phase voltage L3-N.
        TotWhInjL3 (int): Total active energy injected L3.
        TotWhAbsL3 (int): Total active energy absorbed L3.
        TotVarhInjL3 (int): Total reactive energy injected L3.
        TotVarhAbsL3 (int): Total reactive energy absorbed L3.
        ThrotPct (int): Throttling in pct of maximum active power.
        ThrotSrc (Model701ThrotSrc): Active throttling source.
        A_SF (int): Current scale factor.
        V_SF (int): Voltage scale factor.
        Hz_SF (int): Frequency scale factor.
        W_SF (int): Active power scale factor.
        PF_SF (int): Power factor scale factor.
        VA_SF (int): Apparent power scale factor.
        Var_SF (int): Reactive power scale factor.
        TotWh_SF (int): Active energy scale factor.
        TotVarh_SF (int): Reactive energy scale factor.
        Tmp_SF (int): Temperature scale factor.
        MnAlrmInfo (str): Manufacturer alarm information. Valid if MANUFACTURER_ALRM indication is active.
    """

    ACType: Annotated[int, ("SunSpecPoint", {'name': 'ACType', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    InvSt: Annotated[int, ("SunSpecPoint", {'name': 'InvSt', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ConnSt: Annotated[int, ("SunSpecPoint", {'name': 'ConnSt', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Alrm: Annotated[int, ("SunSpecPoint", {'name': 'Alrm', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    DERMode: Annotated[int, ("SunSpecPoint", {'name': 'DERMode', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    VA: Annotated[int, ("SunSpecPoint", {'name': 'VA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    Var: Annotated[int, ("SunSpecPoint", {'name': 'Var', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Var_SF
    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    LLV: Annotated[int, ("SunSpecPoint", {'name': 'LLV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    LNV: Annotated[int, ("SunSpecPoint", {'name': 'LNV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: Hz_SF
    TotWhInj: Annotated[int, ("SunSpecPoint", {'name': 'TotWhInj', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhAbs: Annotated[int, ("SunSpecPoint", {'name': 'TotWhAbs', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotVarhInj: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhInj', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    TotVarhAbs: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhAbs', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    TmpAmb: Annotated[int, ("SunSpecPoint", {'name': 'TmpAmb', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpCab: Annotated[int, ("SunSpecPoint", {'name': 'TmpCab', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpSnk: Annotated[int, ("SunSpecPoint", {'name': 'TmpSnk', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpTrns: Annotated[int, ("SunSpecPoint", {'name': 'TmpTrns', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpSw: Annotated[int, ("SunSpecPoint", {'name': 'TmpSw', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpOt: Annotated[int, ("SunSpecPoint", {'name': 'TmpOt', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    WL1: Annotated[int, ("SunSpecPoint", {'name': 'WL1', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    VAL1: Annotated[int, ("SunSpecPoint", {'name': 'VAL1', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VarL1: Annotated[int, ("SunSpecPoint", {'name': 'VarL1', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Var_SF
    PFL1: Annotated[int, ("SunSpecPoint", {'name': 'PFL1', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    AL1: Annotated[int, ("SunSpecPoint", {'name': 'AL1', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    VL1L2: Annotated[int, ("SunSpecPoint", {'name': 'VL1L2', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    VL1: Annotated[int, ("SunSpecPoint", {'name': 'VL1', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    TotWhInjL1: Annotated[int, ("SunSpecPoint", {'name': 'TotWhInjL1', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhAbsL1: Annotated[int, ("SunSpecPoint", {'name': 'TotWhAbsL1', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotVarhInjL1: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhInjL1', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    TotVarhAbsL1: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhAbsL1', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    WL2: Annotated[int, ("SunSpecPoint", {'name': 'WL2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    VAL2: Annotated[int, ("SunSpecPoint", {'name': 'VAL2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VarL2: Annotated[int, ("SunSpecPoint", {'name': 'VarL2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Var_SF
    PFL2: Annotated[int, ("SunSpecPoint", {'name': 'PFL2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    AL2: Annotated[int, ("SunSpecPoint", {'name': 'AL2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    VL2L3: Annotated[int, ("SunSpecPoint", {'name': 'VL2L3', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    VL2: Annotated[int, ("SunSpecPoint", {'name': 'VL2', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    TotWhInjL2: Annotated[int, ("SunSpecPoint", {'name': 'TotWhInjL2', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhAbsL2: Annotated[int, ("SunSpecPoint", {'name': 'TotWhAbsL2', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotVarhInjL2: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhInjL2', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    TotVarhAbsL2: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhAbsL2', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    WL3: Annotated[int, ("SunSpecPoint", {'name': 'WL3', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    VAL3: Annotated[int, ("SunSpecPoint", {'name': 'VAL3', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VarL3: Annotated[int, ("SunSpecPoint", {'name': 'VarL3', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Var_SF
    PFL3: Annotated[int, ("SunSpecPoint", {'name': 'PFL3', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    AL3: Annotated[int, ("SunSpecPoint", {'name': 'AL3', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    VL3L1: Annotated[int, ("SunSpecPoint", {'name': 'VL3L1', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    VL3: Annotated[int, ("SunSpecPoint", {'name': 'VL3', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    TotWhInjL3: Annotated[int, ("SunSpecPoint", {'name': 'TotWhInjL3', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhAbsL3: Annotated[int, ("SunSpecPoint", {'name': 'TotWhAbsL3', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotVarhInjL3: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhInjL3', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    TotVarhAbsL3: Annotated[int, ("SunSpecPoint", {'name': 'TotVarhAbsL3', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: TotVarh_SF
    ThrotPct: Annotated[int, ("SunSpecPoint", {'name': 'ThrotPct', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ThrotSrc: Annotated[int, ("SunSpecPoint", {'name': 'ThrotSrc', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    VA_SF: Annotated[int, ("SunSpecPoint", {'name': 'VA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Var_SF: Annotated[int, ("SunSpecPoint", {'name': 'Var_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    TotWh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotWh_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    TotVarh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotVarh_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Tmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tmp_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    MnAlrmInfo: Annotated[str, ("SunSpecPoint", {'name': 'MnAlrmInfo', 'ptype': 'string', 'size': 32, 'mandatory': False, 'static': False})]

