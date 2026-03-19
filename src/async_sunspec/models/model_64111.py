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


class Model64111ChargerSt(IntEnum):
    """
    Members:
        Off (int): Off
        Float (int): Float
        Bulk (int): Bulk
        Absorb (int): Absorb
        EQ (int): EQ
    """
    Off = 0
    Float = 1
    Bulk = 2
    Absorb = 3
    EQ = 4



class Model64111(SunSpecModel, model_name="model_64111", id=64111):
    """
    Attributes:
        Port (int)
        V_SF (int)
        A_SF (int)
        P_SF (int)
        AH_SF (int)
        KWH_SF (int)
        BattV (int)
        ArrayV (int)
        OutputA (int)
        InputA (int)
        ChargerSt (Model64111ChargerSt)
        OutputW (int)
        TodayMinBatV (int)
        TodayMaxBatV (int)
        VOCV (int)
        TodayMaxVOC (int)
        TodaykWhOutput (int)
        TodayAHOutput (int)
        LifeTimeKWHOut (int)
        LifeTimeAHOut (int)
        LifeTimeMaxOut (int)
        LifeTimeMaxBatt (int)
        LifeTimeMaxVOC (int)
    """

    Port: Annotated[int, ("SunSpecPoint", {'name': 'Port', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    P_SF: Annotated[int, ("SunSpecPoint", {'name': 'P_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    AH_SF: Annotated[int, ("SunSpecPoint", {'name': 'AH_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    KWH_SF: Annotated[int, ("SunSpecPoint", {'name': 'KWH_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    BattV: Annotated[int, ("SunSpecPoint", {'name': 'BattV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    ArrayV: Annotated[int, ("SunSpecPoint", {'name': 'ArrayV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    OutputA: Annotated[int, ("SunSpecPoint", {'name': 'OutputA', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: A_SF
    InputA: Annotated[int, ("SunSpecPoint", {'name': 'InputA', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: P_SF
    ChargerSt: Annotated[int, ("SunSpecPoint", {'name': 'ChargerSt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    OutputW: Annotated[int, ("SunSpecPoint", {'name': 'OutputW', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: P_SF
    TodayMinBatV: Annotated[int, ("SunSpecPoint", {'name': 'TodayMinBatV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    TodayMaxBatV: Annotated[int, ("SunSpecPoint", {'name': 'TodayMaxBatV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    VOCV: Annotated[int, ("SunSpecPoint", {'name': 'VOCV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    TodayMaxVOC: Annotated[int, ("SunSpecPoint", {'name': 'TodayMaxVOC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    TodaykWhOutput: Annotated[int, ("SunSpecPoint", {'name': 'TodaykWhOutput', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: KWH_SF
    TodayAHOutput: Annotated[int, ("SunSpecPoint", {'name': 'TodayAHOutput', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: AH_SF
    LifeTimeKWHOut: Annotated[int, ("SunSpecPoint", {'name': 'LifeTimeKWHOut', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: P_SF
    LifeTimeAHOut: Annotated[int, ("SunSpecPoint", {'name': 'LifeTimeAHOut', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: KWH_SF
    LifeTimeMaxOut: Annotated[int, ("SunSpecPoint", {'name': 'LifeTimeMaxOut', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: P_SF
    LifeTimeMaxBatt: Annotated[int, ("SunSpecPoint", {'name': 'LifeTimeMaxBatt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    LifeTimeMaxVOC: Annotated[int, ("SunSpecPoint", {'name': 'LifeTimeMaxVOC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF

