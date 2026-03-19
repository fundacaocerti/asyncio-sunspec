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
from enum import IntFlag


class Model202Evt(IntFlag):
    """
    Meter Event Flags

    Members:
        M_EVENT_Power_Failure (int): M_EVENT_Power_Failure
        M_EVENT_Under_Voltage (int): M_EVENT_Under_Voltage
        M_EVENT_Low_PF (int): M_EVENT_Low_PF
        M_EVENT_Over_Current (int): M_EVENT_Over_Current
        M_EVENT_Over_Voltage (int): M_EVENT_Over_Voltage
        M_EVENT_Missing_Sensor (int): M_EVENT_Missing_Sensor
        M_EVENT_Reserved1 (int): M_EVENT_Reserved1
        M_EVENT_Reserved2 (int): M_EVENT_Reserved2
        M_EVENT_Reserved3 (int): M_EVENT_Reserved3
        M_EVENT_Reserved4 (int): M_EVENT_Reserved4
        M_EVENT_Reserved5 (int): M_EVENT_Reserved5
        M_EVENT_Reserved6 (int): M_EVENT_Reserved6
        M_EVENT_Reserved7 (int): M_EVENT_Reserved7
        M_EVENT_Reserved8 (int): M_EVENT_Reserved8
        M_EVENT_OEM01 (int): M_EVENT_OEM01
        M_EVENT_OEM02 (int): M_EVENT_OEM02
        M_EVENT_OEM03 (int): M_EVENT_OEM03
        M_EVENT_OEM04 (int): M_EVENT_OEM04
        M_EVENT_OEM05 (int): M_EVENT_OEM05
        M_EVENT_OEM06 (int): M_EVENT_OEM06
        M_EVENT_OEM07 (int): M_EVENT_OEM07
        M_EVENT_OEM08 (int): M_EVENT_OEM08
        M_EVENT_OEM09 (int): M_EVENT_OEM09
        M_EVENT_OEM10 (int): M_EVENT_OEM10
        M_EVENT_OEM11 (int): M_EVENT_OEM11
        M_EVENT_OEM12 (int): M_EVENT_OEM12
        M_EVENT_OEM13 (int): M_EVENT_OEM13
        M_EVENT_OEM14 (int): M_EVENT_OEM14
        M_EVENT_OEM15 (int): M_EVENT_OEM15
    """
    M_EVENT_Power_Failure = 1 << 2
    M_EVENT_Under_Voltage = 1 << 3
    M_EVENT_Low_PF = 1 << 4
    M_EVENT_Over_Current = 1 << 5
    M_EVENT_Over_Voltage = 1 << 6
    M_EVENT_Missing_Sensor = 1 << 7
    M_EVENT_Reserved1 = 1 << 8
    M_EVENT_Reserved2 = 1 << 9
    M_EVENT_Reserved3 = 1 << 10
    M_EVENT_Reserved4 = 1 << 11
    M_EVENT_Reserved5 = 1 << 12
    M_EVENT_Reserved6 = 1 << 13
    M_EVENT_Reserved7 = 1 << 14
    M_EVENT_Reserved8 = 1 << 15
    M_EVENT_OEM01 = 1 << 16
    M_EVENT_OEM02 = 1 << 17
    M_EVENT_OEM03 = 1 << 18
    M_EVENT_OEM04 = 1 << 19
    M_EVENT_OEM05 = 1 << 20
    M_EVENT_OEM06 = 1 << 21
    M_EVENT_OEM07 = 1 << 22
    M_EVENT_OEM08 = 1 << 23
    M_EVENT_OEM09 = 1 << 24
    M_EVENT_OEM10 = 1 << 25
    M_EVENT_OEM11 = 1 << 26
    M_EVENT_OEM12 = 1 << 27
    M_EVENT_OEM13 = 1 << 28
    M_EVENT_OEM14 = 1 << 29
    M_EVENT_OEM15 = 1 << 30



class Model202(SunSpecModel, model_name="ac_meter_abn", id=202):
    """
    Attributes:
        A (int): Total AC Current
        AphA (int): Phase A Current
        AphB (int): Phase B Current
        AphC (int): Phase C Current
        A_SF (int): Current scale factor
        PhV (int): Line to Neutral AC Voltage (average of active phases)
        PhVphA (int): Phase Voltage AN
        PhVphB (int): Phase Voltage BN
        PhVphC (int): Phase Voltage CN
        PPV (int): Line to Line AC Voltage (average of active phases)
        PhVphAB (int): Phase Voltage AB
        PhVphBC (int): Phase Voltage BC
        PhVphCA (int): Phase Voltage CA
        V_SF (int): Voltage scale factor
        Hz (int): Frequency
        Hz_SF (int): Frequency scale factor
        W (int): Total Real Power
        WphA (int)
        WphB (int)
        WphC (int)
        W_SF (int): Real Power scale factor
        VA (int): AC Apparent Power
        VAphA (int)
        VAphB (int)
        VAphC (int)
        VA_SF (int): Apparent Power scale factor
        VAR (int): Reactive Power
        VARphA (int)
        VARphB (int)
        VARphC (int)
        VAR_SF (int): Reactive Power scale factor
        PF (int): Power Factor
        PFphA (int)
        PFphB (int)
        PFphC (int)
        PF_SF (int): Power Factor scale factor
        TotWhExp (int): Total Real Energy Exported
        TotWhExpPhA (int)
        TotWhExpPhB (int)
        TotWhExpPhC (int)
        TotWhImp (int): Total Real Energy Imported
        TotWhImpPhA (int)
        TotWhImpPhB (int)
        TotWhImpPhC (int)
        TotWh_SF (int): Real Energy scale factor
        TotVAhExp (int): Total Apparent Energy Exported
        TotVAhExpPhA (int)
        TotVAhExpPhB (int)
        TotVAhExpPhC (int)
        TotVAhImp (int): Total Apparent Energy Imported
        TotVAhImpPhA (int)
        TotVAhImpPhB (int)
        TotVAhImpPhC (int)
        TotVAh_SF (int): Apparent Energy scale factor
        TotVArhImpQ1 (int): Total Reactive Energy Imported Quadrant 1
        TotVArhImpQ1PhA (int)
        TotVArhImpQ1PhB (int)
        TotVArhImpQ1PhC (int)
        TotVArhImpQ2 (int): Total Reactive Power Imported Quadrant 2
        TotVArhImpQ2PhA (int)
        TotVArhImpQ2PhB (int)
        TotVArhImpQ2PhC (int)
        TotVArhExpQ3 (int): Total Reactive Power Exported Quadrant 3
        TotVArhExpQ3PhA (int)
        TotVArhExpQ3PhB (int)
        TotVArhExpQ3PhC (int)
        TotVArhExpQ4 (int): Total Reactive Power Exported Quadrant 4
        TotVArhExpQ4PhA (int)
        TotVArhExpQ4PhB (int)
        TotVArhExpQ4PhC (int)
        TotVArh_SF (int): Reactive Energy scale factor
        Evt (Model202Evt): Meter Event Flags
    """

    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphA: Annotated[int, ("SunSpecPoint", {'name': 'AphA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    AphB: Annotated[int, ("SunSpecPoint", {'name': 'AphB', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphC: Annotated[int, ("SunSpecPoint", {'name': 'AphC', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    PhV: Annotated[int, ("SunSpecPoint", {'name': 'PhV', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphA: Annotated[int, ("SunSpecPoint", {'name': 'PhVphA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphB: Annotated[int, ("SunSpecPoint", {'name': 'PhVphB', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphC: Annotated[int, ("SunSpecPoint", {'name': 'PhVphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPV: Annotated[int, ("SunSpecPoint", {'name': 'PPV', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphAB: Annotated[int, ("SunSpecPoint", {'name': 'PhVphAB', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphBC: Annotated[int, ("SunSpecPoint", {'name': 'PhVphBC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PhVphCA: Annotated[int, ("SunSpecPoint", {'name': 'PhVphCA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Hz_SF
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: W_SF
    WphA: Annotated[int, ("SunSpecPoint", {'name': 'WphA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    WphB: Annotated[int, ("SunSpecPoint", {'name': 'WphB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    WphC: Annotated[int, ("SunSpecPoint", {'name': 'WphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VA: Annotated[int, ("SunSpecPoint", {'name': 'VA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VAphA: Annotated[int, ("SunSpecPoint", {'name': 'VAphA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VAphB: Annotated[int, ("SunSpecPoint", {'name': 'VAphB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VAphC: Annotated[int, ("SunSpecPoint", {'name': 'VAphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VA_SF: Annotated[int, ("SunSpecPoint", {'name': 'VA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    VAR: Annotated[int, ("SunSpecPoint", {'name': 'VAR', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VAR_SF
    VARphA: Annotated[int, ("SunSpecPoint", {'name': 'VARphA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VAR_SF
    VARphB: Annotated[int, ("SunSpecPoint", {'name': 'VARphB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VAR_SF
    VARphC: Annotated[int, ("SunSpecPoint", {'name': 'VARphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VAR_SF
    VAR_SF: Annotated[int, ("SunSpecPoint", {'name': 'VAR_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    PFphA: Annotated[int, ("SunSpecPoint", {'name': 'PFphA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    PFphB: Annotated[int, ("SunSpecPoint", {'name': 'PFphB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    PFphC: Annotated[int, ("SunSpecPoint", {'name': 'PFphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    TotWhExp: Annotated[int, ("SunSpecPoint", {'name': 'TotWhExp', 'ptype': 'uint32', 'mandatory': True, 'static': False})]  # sf: TotWh_SF
    TotWhExpPhA: Annotated[int, ("SunSpecPoint", {'name': 'TotWhExpPhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhExpPhB: Annotated[int, ("SunSpecPoint", {'name': 'TotWhExpPhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhExpPhC: Annotated[int, ("SunSpecPoint", {'name': 'TotWhExpPhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhImp: Annotated[int, ("SunSpecPoint", {'name': 'TotWhImp', 'ptype': 'uint32', 'mandatory': True, 'static': False})]  # sf: TotWh_SF
    TotWhImpPhA: Annotated[int, ("SunSpecPoint", {'name': 'TotWhImpPhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhImpPhB: Annotated[int, ("SunSpecPoint", {'name': 'TotWhImpPhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWhImpPhC: Annotated[int, ("SunSpecPoint", {'name': 'TotWhImpPhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotWh_SF
    TotWh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotWh_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    TotVAhExp: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhExp', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhExpPhA: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhExpPhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhExpPhB: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhExpPhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhExpPhC: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhExpPhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhImp: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhImp', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhImpPhA: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhImpPhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhImpPhB: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhImpPhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhImpPhC: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhImpPhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotVAh_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    TotVArhImpQ1: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ1PhA: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ1PhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ1PhB: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ1PhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ1PhC: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ1PhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ2: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ2PhA: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ2PhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ2PhB: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ2PhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ2PhC: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ2PhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ3: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ3', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ3PhA: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ3PhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ3PhB: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ3PhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ3PhC: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ3PhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ4: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ4', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ4PhA: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ4PhA', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ4PhB: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ4PhB', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ4PhC: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ4PhC', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotVArh_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]

