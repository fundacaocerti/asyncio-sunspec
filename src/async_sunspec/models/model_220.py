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


class Model220RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        DS (int)
    """

    DS: Annotated[int, ("SunSpecPoint", {'name': 'DS', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model220Evt(IntFlag):
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



class Model220Alg(IntEnum):
    """
    Algorithm used to compute the digital signature

    Members:
        NONE (int): NONE
        AES_GMAC_64 (int): AES_GMAC_64
        ECC_256 (int): ECC_256
    """
    NONE = 0
    AES_GMAC_64 = 1
    ECC_256 = 2



class Model220(SunSpecModel, model_name="ac_meter_secure", id=220):
    """
    Include this model for secure metering

    Attributes:
        A (int): Total AC Current
        A_SF (int): Current scale factor
        PhV (int): Average phase or line voltage
        V_SF (int): Voltage scale factor
        Hz (int): Frequency
        Hz_SF (int): Frequency scale factor
        W (int): Total Real Power
        W_SF (int): Real Power scale factor
        VA (int): AC Apparent Power
        VA_SF (int): Apparent Power scale factor
        VAR (int): Reactive Power
        VAR_SF (int): Reactive Power scale factor
        PF (int): Power Factor
        PF_SF (int): Power Factor scale factor
        TotWhExp (int): Total Real Energy Exported
        TotWhImp (int): Total Real Energy Imported
        TotWh_SF (int): Real Energy scale factor
        TotVAhExp (int): Total Apparent Energy Exported
        TotVAhImp (int): Total Apparent Energy Imported
        TotVAh_SF (int): Apparent Energy scale factor
        TotVArhImpQ1 (int): Total Reactive Energy Imported Quadrant 1
        TotVArhImpQ2 (int): Total Reactive Power Imported Quadrant 2
        TotVArhExpQ3 (int): Total Reactive Power Exported Quadrant 3
        TotVArhExpQ4 (int): Total Reactive Power Exported Quadrant 4
        TotVArh_SF (int): Reactive Energy scale factor
        Evt (Model220Evt): Meter Event Flags
        Rsrvd (int)
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of request
        Alg (Model220Alg): Algorithm used to compute the digital signature
        N (int): Number of registers comprising the digital signature.
    """

    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    PhV: Annotated[int, ("SunSpecPoint", {'name': 'PhV', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: V_SF
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Hz_SF
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: W_SF
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VA: Annotated[int, ("SunSpecPoint", {'name': 'VA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VA_SF: Annotated[int, ("SunSpecPoint", {'name': 'VA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    VAR: Annotated[int, ("SunSpecPoint", {'name': 'VAR', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VAR_SF
    VAR_SF: Annotated[int, ("SunSpecPoint", {'name': 'VAR_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    TotWhExp: Annotated[int, ("SunSpecPoint", {'name': 'TotWhExp', 'ptype': 'uint32', 'mandatory': True, 'static': False})]  # sf: TotWh_SF
    TotWhImp: Annotated[int, ("SunSpecPoint", {'name': 'TotWhImp', 'ptype': 'uint32', 'mandatory': True, 'static': False})]  # sf: TotWh_SF
    TotWh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotWh_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    TotVAhExp: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhExp', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAhImp: Annotated[int, ("SunSpecPoint", {'name': 'TotVAhImp', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVAh_SF
    TotVAh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotVAh_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    TotVArhImpQ1: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhImpQ2: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhImpQ2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ3: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ3', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArhExpQ4: Annotated[int, ("SunSpecPoint", {'name': 'TotVArhExpQ4', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: TotVArh_SF
    TotVArh_SF: Annotated[int, ("SunSpecPoint", {'name': 'TotVArh_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Rsrvd: Annotated[int, ("SunSpecPoint", {'name': 'Rsrvd', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    repeating: Annotated[Model220RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model220RepeatingGroup})]

