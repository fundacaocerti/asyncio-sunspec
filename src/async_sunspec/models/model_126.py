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


class Model126DeptRef(IntEnum):
    """
    Meaning of dependent variable: 1=%WMax 2=%VArMax 3=%VArAval.

    Members:
        WMax (int): WMax
        VArMax (int): VArMax
        VArAval (int): VArAval
    """
    WMax = 1
    VArMax = 2
    VArAval = 3



class Model126ReadOnly(IntEnum):
    """
    Boolean flag indicates if curve is read-only or can be modified.

    Members:
        READWRITE (int): READWRITE
        READONLY (int): READONLY
    """
    READWRITE = 0
    READONLY = 1



class Model126CurveGroup(SunSpecGroup):
    """
    Attributes:
        ActPt (int): Number of active points in array.
        DeptRef (Model126DeptRef): Meaning of dependent variable: 1=%WMax 2=%VArMax 3=%VArAval.
        V1 (int): Point 1 Volts.
        VAr1 (int): Point 1 VARs.
        V2 (int): Point 2 Volts.
        VAr2 (int): Point 2 VARs.
        V3 (int): Point 3 Volts.
        VAr3 (int): Point 3 VARs.
        V4 (int): Point 4 Volts.
        VAr4 (int): Point 4 VARs.
        V5 (int): Point 5 Volts.
        VAr5 (int): Point 5 VARs.
        V6 (int): Point 6 Volts.
        VAr6 (int): Point 6 VARs.
        V7 (int): Point 7 Volts.
        VAr7 (int): Point 7 VARs.
        V8 (int): Point 8 Volts.
        VAr8 (int): Point 8 VARs.
        V9 (int): Point 9 Volts.
        VAr9 (int): Point 9 VARs.
        V10 (int): Point 10 Volts.
        VAr10 (int): Point 10 VARs.
        V11 (int): Point 11 Volts.
        VAr11 (int): Point 11 VARs.
        V12 (int): Point 12 Volts.
        VAr12 (int): Point 12 VARs.
        V13 (int): Point 13 Volts.
        VAr13 (int): Point 13 VARs.
        V14 (int): Point 14 Volts.
        VAr14 (int): Point 14 VARs.
        V15 (int): Point 15 Volts.
        VAr15 (int): Point 15 VARs.
        V16 (int): Point 16 Volts.
        VAr16 (int): Point 16 VARs.
        V17 (int): Point 17 Volts.
        VAr17 (int): Point 17 VARs.
        V18 (int): Point 18 Volts.
        VAr18 (int): Point 18 VARs.
        V19 (int): Point 19 Volts.
        VAr19 (int): Point 19 VARs.
        V20 (int): Point 20 Volts.
        VAr20 (int): Point 20 VARs.
        CrvNam (str): Optional description for curve. (Max 16 chars)
        RmpTms (int): The time of the PT1 in seconds (time to accomplish a change of 95%).
        RmpDecTmm (int): The maximum rate at which the VAR value may be reduced in response to changes in the voltage value. %refVal is %WMax %VArMax or %VArAval depending on value of DeptRef.
        RmpIncTmm (int): The maximum rate at which the VAR value may be increased in response to changes in the voltage value. %refVal is %WMax %VArMax or %VArAval depending on value of DeptRef.
        ReadOnly (Model126ReadOnly): Boolean flag indicates if curve is read-only or can be modified.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    DeptRef: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    V1: Annotated[int, ("SunSpecPoint", {'name': 'V1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr1: Annotated[int, ("SunSpecPoint", {'name': 'VAr1', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V2: Annotated[int, ("SunSpecPoint", {'name': 'V2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr2: Annotated[int, ("SunSpecPoint", {'name': 'VAr2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V3: Annotated[int, ("SunSpecPoint", {'name': 'V3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr3: Annotated[int, ("SunSpecPoint", {'name': 'VAr3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V4: Annotated[int, ("SunSpecPoint", {'name': 'V4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr4: Annotated[int, ("SunSpecPoint", {'name': 'VAr4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V5: Annotated[int, ("SunSpecPoint", {'name': 'V5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr5: Annotated[int, ("SunSpecPoint", {'name': 'VAr5', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V6: Annotated[int, ("SunSpecPoint", {'name': 'V6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr6: Annotated[int, ("SunSpecPoint", {'name': 'VAr6', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V7: Annotated[int, ("SunSpecPoint", {'name': 'V7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr7: Annotated[int, ("SunSpecPoint", {'name': 'VAr7', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V8: Annotated[int, ("SunSpecPoint", {'name': 'V8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr8: Annotated[int, ("SunSpecPoint", {'name': 'VAr8', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V9: Annotated[int, ("SunSpecPoint", {'name': 'V9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr9: Annotated[int, ("SunSpecPoint", {'name': 'VAr9', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V10: Annotated[int, ("SunSpecPoint", {'name': 'V10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr10: Annotated[int, ("SunSpecPoint", {'name': 'VAr10', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V11: Annotated[int, ("SunSpecPoint", {'name': 'V11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr11: Annotated[int, ("SunSpecPoint", {'name': 'VAr11', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V12: Annotated[int, ("SunSpecPoint", {'name': 'V12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr12: Annotated[int, ("SunSpecPoint", {'name': 'VAr12', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V13: Annotated[int, ("SunSpecPoint", {'name': 'V13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr13: Annotated[int, ("SunSpecPoint", {'name': 'VAr13', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V14: Annotated[int, ("SunSpecPoint", {'name': 'V14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr14: Annotated[int, ("SunSpecPoint", {'name': 'VAr14', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V15: Annotated[int, ("SunSpecPoint", {'name': 'V15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr15: Annotated[int, ("SunSpecPoint", {'name': 'VAr15', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V16: Annotated[int, ("SunSpecPoint", {'name': 'V16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr16: Annotated[int, ("SunSpecPoint", {'name': 'VAr16', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V17: Annotated[int, ("SunSpecPoint", {'name': 'V17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr17: Annotated[int, ("SunSpecPoint", {'name': 'VAr17', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V18: Annotated[int, ("SunSpecPoint", {'name': 'V18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr18: Annotated[int, ("SunSpecPoint", {'name': 'VAr18', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V19: Annotated[int, ("SunSpecPoint", {'name': 'V19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr19: Annotated[int, ("SunSpecPoint", {'name': 'VAr19', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    V20: Annotated[int, ("SunSpecPoint", {'name': 'V20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VAr20: Annotated[int, ("SunSpecPoint", {'name': 'VAr20', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF
    CrvNam: Annotated[str, ("SunSpecPoint", {'name': 'CrvNam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpDecTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpDecTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    RmpIncTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model126ModEna(IntFlag):
    """
    Is Volt-VAR control active.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model126(SunSpecModel, model_name="volt_var", id=126):
    """
    Static Volt-VAR Arrays 

    Attributes:
        ActCrv (int): Index of active curve. 0=no active curve.
        ModEna (Model126ModEna): Is Volt-VAR control active.
        WinTms (int): Time window for volt-VAR change.
        RvrtTms (int): Timeout period for volt-VAR curve selection.
        RmpTms (int): The time of the PT1 in seconds (time to accomplish a change of 95%).
        NCrv (int): Number of curves supported (recommend 4).
        NPt (int): Number of curve points supported (maximum of 20).
        V_SF (int): Scale factor for percent VRef.
        DeptRef_SF (int): scale factor for dependent variable.
        RmpIncDec_SF (int)
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
    curve: Annotated[Model126CurveGroup, ("SunSpecGroup", {"name": "curve", "group_type": Model126CurveGroup})]

