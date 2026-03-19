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


class Model201Evt(IntFlag):
    """
    Meter Event Flags

    Members:
        Power_Failure (int): Power_Failure
        Under_Voltage (int): Under_Voltage
        Low_PF (int): Low_PF
        Over_Current (int): Over_Current
        Over_Voltage (int): Over_Voltage
        Missing_Sensor (int): Missing_Sensor
        OEM01 (int): OEM01
        OEM02 (int): OEM02
        OEM03 (int): OEM03
        OEM04 (int): OEM04
        OEM05 (int): OEM05
        OEM06 (int): OEM06
        OEM07 (int): OEM07
        OEM08 (int): OEM08
        OEM09 (int): OEM09
        OEM10 (int): OEM10
        OEM11 (int): OEM11
        OEM12 (int): OEM12
        OEM13 (int): OEM13
        OEM14 (int): OEM14
        OEM15 (int): OEM15
    """
    Power_Failure = 1 << 2
    Under_Voltage = 1 << 3
    Low_PF = 1 << 4
    Over_Current = 1 << 5
    Over_Voltage = 1 << 6
    Missing_Sensor = 1 << 7
    OEM01 = 1 << 16
    OEM02 = 1 << 17
    OEM03 = 1 << 18
    OEM04 = 1 << 19
    OEM05 = 1 << 20
    OEM06 = 1 << 21
    OEM07 = 1 << 22
    OEM08 = 1 << 23
    OEM09 = 1 << 24
    OEM10 = 1 << 25
    OEM11 = 1 << 26
    OEM12 = 1 << 27
    OEM13 = 1 << 28
    OEM14 = 1 << 29
    OEM15 = 1 << 30



class Model201(SunSpecModel, model_name="ac_meter_an_or_ab", id=201):
    """
    Include this model for single phase (AN or AB) metering

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
        PPVphAB (int): Phase Voltage AB
        PPVphBC (int): Phase Voltage BC
        PPVphCA (int): Phase Voltage CA
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
        Evt (Model201Evt): Meter Event Flags
    """

    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphA: Annotated[int, ("SunSpecPoint", {'name': 'AphA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphB: Annotated[int, ("SunSpecPoint", {'name': 'AphB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    AphC: Annotated[int, ("SunSpecPoint", {'name': 'AphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    PhV: Annotated[int, ("SunSpecPoint", {'name': 'PhV', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PhVphA: Annotated[int, ("SunSpecPoint", {'name': 'PhVphA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PhVphB: Annotated[int, ("SunSpecPoint", {'name': 'PhVphB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PhVphC: Annotated[int, ("SunSpecPoint", {'name': 'PhVphC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPV: Annotated[int, ("SunSpecPoint", {'name': 'PPV', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPVphAB: Annotated[int, ("SunSpecPoint", {'name': 'PPVphAB', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPVphBC: Annotated[int, ("SunSpecPoint", {'name': 'PPVphBC', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPVphCA: Annotated[int, ("SunSpecPoint", {'name': 'PPVphCA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
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

