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


class Model132DeptRef(IntEnum):
    """
    Defines the meaning of the Watts DeptRef.  1=% WMax 2=% WAvail

    Members:
        PCTWMax (int): PCTWMax
        PCTWAval (int): PCTWAval
    """
    PCTWMax = 1
    PCTWAval = 2



class Model132ReadOnly(IntEnum):
    """
    Enumerated value indicates if curve is read-only or can be modified.

    Members:
        READWRITE (int): READWRITE
        READONLY (int): READONLY
    """
    READWRITE = 0
    READONLY = 1



class Model132CurveGroup(SunSpecGroup):
    """
    Attributes:
        ActPt (int): Number of active points in array.
        DeptRef (Model132DeptRef): Defines the meaning of the Watts DeptRef.  1=% WMax 2=% WAvail
        V1 (int): Point 1 Volts.
        W1 (int): Point 1 Watts.
        V2 (int): Point 2 Volts.
        W2 (int): Point 2 Watts.
        V3 (int): Point 3 Volts.
        W3 (int): Point 3 Watts.
        V4 (int): Point 4 Volts.
        W4 (int): Point 4 Watts.
        V5 (int): Point 5 Volts.
        W5 (int): Point 5 Watts.
        V6 (int): Point 6 Volts.
        W6 (int): Point 6 Watts.
        V7 (int): Point 7 Volts.
        W7 (int): Point 7 Watts.
        V8 (int): Point 8 Volts.
        W8 (int): Point 8 Watts.
        V9 (int): Point 9 Volts.
        W9 (int): Point 9 Watts.
        V10 (int): Point 10 Volts.
        W10 (int): Point 10 Watts.
        V11 (int): Point 11 Volts.
        W11 (int): Point 11 Watts.
        V12 (int): Point 12 Volts.
        W12 (int): Point 12 Watts.
        V13 (int): Point 13 Volts.
        W13 (int): Point 13 Watts.
        V14 (int): Point 14 Volts.
        W14 (int): Point 14 Watts.
        V15 (int): Point 15 Volts.
        W15 (int): Point 15 Watts.
        V16 (int): Point 16 Volts.
        W16 (int): Point 16 Watts.
        V17 (int): Point 17 Volts.
        W17 (int): Point 17 Watts.
        V18 (int): Point 18 Volts.
        W18 (int): Point 18 Watts.
        V19 (int): Point 19 Volts.
        W19 (int): Point 19 Watts.
        V20 (int): Point 20 Volts.
        W20 (int): Point 20 Watts.
        CrvNam (str): Optional description for curve.
        RmpPt1Tms (int): The time of the PT1 in seconds (time to accomplish a change of 95%).
        RmpDecTmm (int): The maximum rate at which the watt value may be reduced in response to changes in the voltage value.
        RmpIncTmm (int): The maximum rate at which the watt value may be increased in response to changes in the voltage value.
        ReadOnly (Model132ReadOnly): Enumerated value indicates if curve is read-only or can be modified.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    DeptRef: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    V1: Annotated[int, ("SunSpecPoint", {'name': 'V1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W1: Annotated[int, ("SunSpecPoint", {'name': 'W1', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V2: Annotated[int, ("SunSpecPoint", {'name': 'V2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W2: Annotated[int, ("SunSpecPoint", {'name': 'W2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V3: Annotated[int, ("SunSpecPoint", {'name': 'V3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W3: Annotated[int, ("SunSpecPoint", {'name': 'W3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V4: Annotated[int, ("SunSpecPoint", {'name': 'V4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W4: Annotated[int, ("SunSpecPoint", {'name': 'W4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V5: Annotated[int, ("SunSpecPoint", {'name': 'V5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W5: Annotated[int, ("SunSpecPoint", {'name': 'W5', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V6: Annotated[int, ("SunSpecPoint", {'name': 'V6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W6: Annotated[int, ("SunSpecPoint", {'name': 'W6', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V7: Annotated[int, ("SunSpecPoint", {'name': 'V7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W7: Annotated[int, ("SunSpecPoint", {'name': 'W7', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V8: Annotated[int, ("SunSpecPoint", {'name': 'V8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W8: Annotated[int, ("SunSpecPoint", {'name': 'W8', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V9: Annotated[int, ("SunSpecPoint", {'name': 'V9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W9: Annotated[int, ("SunSpecPoint", {'name': 'W9', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V10: Annotated[int, ("SunSpecPoint", {'name': 'V10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W10: Annotated[int, ("SunSpecPoint", {'name': 'W10', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V11: Annotated[int, ("SunSpecPoint", {'name': 'V11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W11: Annotated[int, ("SunSpecPoint", {'name': 'W11', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V12: Annotated[int, ("SunSpecPoint", {'name': 'V12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W12: Annotated[int, ("SunSpecPoint", {'name': 'W12', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V13: Annotated[int, ("SunSpecPoint", {'name': 'V13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W13: Annotated[int, ("SunSpecPoint", {'name': 'W13', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V14: Annotated[int, ("SunSpecPoint", {'name': 'V14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W14: Annotated[int, ("SunSpecPoint", {'name': 'W14', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V15: Annotated[int, ("SunSpecPoint", {'name': 'V15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W15: Annotated[int, ("SunSpecPoint", {'name': 'W15', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V16: Annotated[int, ("SunSpecPoint", {'name': 'V16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W16: Annotated[int, ("SunSpecPoint", {'name': 'W16', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V17: Annotated[int, ("SunSpecPoint", {'name': 'V17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W17: Annotated[int, ("SunSpecPoint", {'name': 'W17', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V18: Annotated[int, ("SunSpecPoint", {'name': 'V18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W18: Annotated[int, ("SunSpecPoint", {'name': 'W18', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V19: Annotated[int, ("SunSpecPoint", {'name': 'V19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W19: Annotated[int, ("SunSpecPoint", {'name': 'W19', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V20: Annotated[int, ("SunSpecPoint", {'name': 'V20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W20: Annotated[int, ("SunSpecPoint", {'name': 'W20', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    CrvNam: Annotated[str, ("SunSpecPoint", {'name': 'CrvNam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpPt1Tms: Annotated[int, ("SunSpecPoint", {'name': 'RmpPt1Tms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpDecTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpDecTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    RmpIncTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model132ModEna(IntFlag):
    """
    Is Volt-Watt control active.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model132(SunSpecModel, model_name="volt_watt", id=132):
    """
    Volt-Watt 

    Attributes:
        ActCrv (int): Index of active curve. 0=no active curve.
        ModEna (Model132ModEna): Is Volt-Watt control active.
        WinTms (int): Time window for volt-watt change.
        RvrtTms (int): Timeout period for volt-watt curve selection.
        RmpTms (int): Ramp time for moving from current mode to new mode.
        NCrv (int): Number of curves supported (recommend min. 4).
        NPt (int): Number of points in array (maximum 20).
        V_SF (int): Scale factor for percent VRef.
        DeptRef_SF (int): Scale Factor for % DeptRef
        RmpIncDec_SF (int): Scale factor for increment and decrement ramps.
    """

    ActCrv: Annotated[int, ("SunSpecPoint", {'name': 'ActCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NCrv: Annotated[int, ("SunSpecPoint", {'name': 'NCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DeptRef_SF: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    RmpIncDec_SF: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncDec_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    curve: Annotated[Model132CurveGroup, ("SunSpecGroup", {"name": "curve", "group_type": Model132CurveGroup})]

