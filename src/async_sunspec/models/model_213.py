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


class Model213Evt(IntFlag):
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



class Model213(SunSpecModel, model_name="ac_meter_abcn_float", id=213):
    """
    Attributes:
        A (float): Total AC Current
        AphA (float): Phase A Current
        AphB (float): Phase B Current
        AphC (float): Phase C Current
        PhV (float): Line to Neutral AC Voltage (average of active phases)
        PhVphA (float): Phase Voltage AN
        PhVphB (float): Phase Voltage BN
        PhVphC (float): Phase Voltage CN
        PPV (float): Line to Line AC Voltage (average of active phases)
        PPVphAB (float): Phase Voltage AB
        PPVphBC (float): Phase Voltage BC
        PPVphCA (float): Phase Voltage CA
        Hz (float): Frequency
        W (float): Total Real Power
        WphA (float)
        WphB (float)
        WphC (float)
        VA (float): AC Apparent Power
        VAphA (float)
        VAphB (float)
        VAphC (float)
        VAR (float): Reactive Power
        VARphA (float)
        VARphB (float)
        VARphC (float)
        PF (float): Power Factor
        PFphA (float)
        PFphB (float)
        PFphC (float)
        TotWhExp (float): Total Real Energy Exported
        TotWhExpPhA (float)
        TotWhExpPhB (float)
        TotWhExpPhC (float)
        TotWhImp (float): Total Real Energy Imported
        TotWhImpPhA (float)
        TotWhImpPhB (float)
        TotWhImpPhC (float)
        TotVAhExp (float): Total Apparent Energy Exported
        TotVAhExpPhA (float)
        TotVAhExpPhB (float)
        TotVAhExpPhC (float)
        TotVAhImp (float): Total Apparent Energy Imported
        TotVAhImpPhA (float)
        TotVAhImpPhB (float)
        TotVAhImpPhC (float)
        TotVArhImpQ1 (float): Total Reactive Energy Imported Quadrant 1
        TotVArhImpQ1phA (float)
        TotVArhImpQ1phB (float)
        TotVArhImpQ1phC (float)
        TotVArhImpQ2 (float): Total Reactive Power Imported Quadrant 2
        TotVArhImpQ2phA (float)
        TotVArhImpQ2phB (float)
        TotVArhImpQ2phC (float)
        TotVArhExpQ3 (float): Total Reactive Power Exported Quadrant 3
        TotVArhExpQ3phA (float)
        TotVArhExpQ3phB (float)
        TotVArhExpQ3phC (float)
        TotVArhExpQ4 (float): Total Reactive Power Exported Quadrant 4
        TotVArhExpQ4phA (float)
        TotVArhExpQ4phB (float)
        TotVArhExpQ4phC (float)
        Evt (Model213Evt): Meter Event Flags
    """

    A: Annotated[float, ("SunSpecPoint", {'name': 'A', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    AphA: Annotated[float, ("SunSpecPoint", {'name': 'AphA', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    AphB: Annotated[float, ("SunSpecPoint", {'name': 'AphB', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    AphC: Annotated[float, ("SunSpecPoint", {'name': 'AphC', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PhV: Annotated[float, ("SunSpecPoint", {'name': 'PhV', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PhVphA: Annotated[float, ("SunSpecPoint", {'name': 'PhVphA', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PhVphB: Annotated[float, ("SunSpecPoint", {'name': 'PhVphB', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PhVphC: Annotated[float, ("SunSpecPoint", {'name': 'PhVphC', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PPV: Annotated[float, ("SunSpecPoint", {'name': 'PPV', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PPVphAB: Annotated[float, ("SunSpecPoint", {'name': 'PPVphAB', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PPVphBC: Annotated[float, ("SunSpecPoint", {'name': 'PPVphBC', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PPVphCA: Annotated[float, ("SunSpecPoint", {'name': 'PPVphCA', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    Hz: Annotated[float, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    W: Annotated[float, ("SunSpecPoint", {'name': 'W', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    WphA: Annotated[float, ("SunSpecPoint", {'name': 'WphA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    WphB: Annotated[float, ("SunSpecPoint", {'name': 'WphB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    WphC: Annotated[float, ("SunSpecPoint", {'name': 'WphC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VA: Annotated[float, ("SunSpecPoint", {'name': 'VA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VAphA: Annotated[float, ("SunSpecPoint", {'name': 'VAphA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VAphB: Annotated[float, ("SunSpecPoint", {'name': 'VAphB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VAphC: Annotated[float, ("SunSpecPoint", {'name': 'VAphC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VAR: Annotated[float, ("SunSpecPoint", {'name': 'VAR', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VARphA: Annotated[float, ("SunSpecPoint", {'name': 'VARphA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VARphB: Annotated[float, ("SunSpecPoint", {'name': 'VARphB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VARphC: Annotated[float, ("SunSpecPoint", {'name': 'VARphC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PF: Annotated[float, ("SunSpecPoint", {'name': 'PF', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PFphA: Annotated[float, ("SunSpecPoint", {'name': 'PFphA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PFphB: Annotated[float, ("SunSpecPoint", {'name': 'PFphB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PFphC: Annotated[float, ("SunSpecPoint", {'name': 'PFphC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotWhExp: Annotated[float, ("SunSpecPoint", {'name': 'TotWhExp', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    TotWhExpPhA: Annotated[float, ("SunSpecPoint", {'name': 'TotWhExpPhA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotWhExpPhB: Annotated[float, ("SunSpecPoint", {'name': 'TotWhExpPhB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotWhExpPhC: Annotated[float, ("SunSpecPoint", {'name': 'TotWhExpPhC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotWhImp: Annotated[float, ("SunSpecPoint", {'name': 'TotWhImp', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    TotWhImpPhA: Annotated[float, ("SunSpecPoint", {'name': 'TotWhImpPhA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotWhImpPhB: Annotated[float, ("SunSpecPoint", {'name': 'TotWhImpPhB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotWhImpPhC: Annotated[float, ("SunSpecPoint", {'name': 'TotWhImpPhC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhExp: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhExp', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhExpPhA: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhExpPhA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhExpPhB: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhExpPhB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhExpPhC: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhExpPhC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhImp: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhImp', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhImpPhA: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhImpPhA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhImpPhB: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhImpPhB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVAhImpPhC: Annotated[float, ("SunSpecPoint", {'name': 'TotVAhImpPhC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ1: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ1', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ1phA: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ1phA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ1phB: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ1phB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ1phC: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ1phC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ2: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ2', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ2phA: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ2phA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ2phB: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ2phB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhImpQ2phC: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhImpQ2phC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ3: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ3', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ3phA: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ3phA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ3phB: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ3phB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ3phC: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ3phC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ4: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ4', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ4phA: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ4phA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ4phB: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ4phB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TotVArhExpQ4phC: Annotated[float, ("SunSpecPoint", {'name': 'TotVArhExpQ4phC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]

