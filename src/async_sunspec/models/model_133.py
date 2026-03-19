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


class Model133IntvTyp(IntEnum):
    """
    The repetition frequency for time-based schedules: no repeat=0

    Members:
        ONETIME (int): ONETIME
        DAILY (int): DAILY
        WEEKLY (int): WEEKLY
        MONTHLY (int): MONTHLY
        WEEKDAY (int): WEEKDAY
        HOLIDAY (int): HOLIDAY
        WEEKEND (int): WEEKEND
        YEARLY (int): YEARLY
    """
    ONETIME = 0
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    WEEKDAY = 4
    HOLIDAY = 5
    WEEKEND = 6
    YEARLY = 7



class Model133XTyp(IntEnum):
    """
    The meaning of the X-values in the array. 

    Members:
        UNSET (int): UNSET
        TIME (int): TIME
        TEMP (int): TEMP
        PRICE (int): PRICE
        OTHER (int): OTHER
    """
    UNSET = 0
    TIME = 1
    TEMP = 2
    PRICE = 3
    OTHER = 99



class Model133YTyp(IntEnum):
    """
    The meaning of the Y-values in the array.

    Members:
        UNSET (int): UNSET
        WMax (int): WMax
        RSRVD2 (int): RSRVD2
        PF (int): PF
        RSRVD4 (int): RSRVD4
        WATT_PRICE (int): WATT_PRICE
        VAR_PRICE (int): VAR_PRICE
        RSRVD7 (int): RSRVD7
        VOLT_VAR_ARRAY (int): VOLT_VAR_ARRAY
        WChaGra (int): WChaGra
        WDisChaGra (int): WDisChaGra
        VArAval (int): VArAval
        Schedule (int): Schedule
        OTHER (int): OTHER
    """
    UNSET = 0
    WMax = 1
    RSRVD2 = 2
    PF = 3
    RSRVD4 = 4
    WATT_PRICE = 5
    VAR_PRICE = 6
    RSRVD7 = 7
    VOLT_VAR_ARRAY = 8
    WChaGra = 9
    WDisChaGra = 10
    VArAval = 11
    Schedule = 12
    OTHER = 99



class Model133RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        ActPts (int): Number of active entries in schedule.
        StrTms (int): Schedule start in seconds since 2000 JAN 01 00:00:00 UTC.
        RepPer (int): The repetition count for time-based schedules (0=repeat forever)
        IntvTyp (Model133IntvTyp): The repetition frequency for time-based schedules: no repeat=0
        XTyp (Model133XTyp): The meaning of the X-values in the array. 
        X_SF (int): Scale factor for schedule range values.
        YTyp (Model133YTyp): The meaning of the Y-values in the array.
        Y_SF (int): Scale factor for schedule target values.
        X1 (int): Entry 1 range.
        Y1 (int): Entry 1 target.
        X2 (int): Entry 2 range.
        Y2 (int): Entry 2 target.
        X3 (int): Entry 3 range.
        Y3 (int): Entry 3 target.
        X4 (int): Entry 4 range.
        Y4 (int): Entry 4 target.
        X5 (int): Entry 15range.
        Y5 (int): Entry 5 target.
        X6 (int): Entry 6 range.
        Y6 (int): Entry 6 target.
        X7 (int): Entry 7 range.
        Y7 (int): Entry 7 target.
        X8 (int): Entry 8 range.
        Y8 (int): Entry 8 target.
        X9 (int): Entry 9 range.
        Y9 (int): Entry 9 target.
        X10 (int): Entry 10 range.
        Y10 (int): Entry 10 target.
        Nam (str): Optional description for schedule.
        WinTms (int): Time window for schedule entry change.
        RmpTms (int): Ramp time for moving from current target to new target.
        ActIndx (int): Index of active entry in the active schedule.
    """

    ActPts: Annotated[int, ("SunSpecPoint", {'name': 'ActPts', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    StrTms: Annotated[int, ("SunSpecPoint", {'name': 'StrTms', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    RepPer: Annotated[int, ("SunSpecPoint", {'name': 'RepPer', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    IntvTyp: Annotated[int, ("SunSpecPoint", {'name': 'IntvTyp', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    XTyp: Annotated[int, ("SunSpecPoint", {'name': 'XTyp', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    X_SF: Annotated[int, ("SunSpecPoint", {'name': 'X_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False, 'access': 'RW'})]
    YTyp: Annotated[int, ("SunSpecPoint", {'name': 'YTyp', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Y_SF: Annotated[int, ("SunSpecPoint", {'name': 'Y_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False, 'access': 'RW'})]
    X1: Annotated[int, ("SunSpecPoint", {'name': 'X1', 'ptype': 'int32', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y1: Annotated[int, ("SunSpecPoint", {'name': 'Y1', 'ptype': 'int32', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X2: Annotated[int, ("SunSpecPoint", {'name': 'X2', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y2: Annotated[int, ("SunSpecPoint", {'name': 'Y2', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X3: Annotated[int, ("SunSpecPoint", {'name': 'X3', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y3: Annotated[int, ("SunSpecPoint", {'name': 'Y3', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X4: Annotated[int, ("SunSpecPoint", {'name': 'X4', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y4: Annotated[int, ("SunSpecPoint", {'name': 'Y4', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X5: Annotated[int, ("SunSpecPoint", {'name': 'X5', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y5: Annotated[int, ("SunSpecPoint", {'name': 'Y5', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X6: Annotated[int, ("SunSpecPoint", {'name': 'X6', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y6: Annotated[int, ("SunSpecPoint", {'name': 'Y6', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X7: Annotated[int, ("SunSpecPoint", {'name': 'X7', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y7: Annotated[int, ("SunSpecPoint", {'name': 'Y7', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X8: Annotated[int, ("SunSpecPoint", {'name': 'X8', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y8: Annotated[int, ("SunSpecPoint", {'name': 'Y8', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X9: Annotated[int, ("SunSpecPoint", {'name': 'X9', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y9: Annotated[int, ("SunSpecPoint", {'name': 'Y9', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    X10: Annotated[int, ("SunSpecPoint", {'name': 'X10', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: X_SF
    Y10: Annotated[int, ("SunSpecPoint", {'name': 'Y10', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Y_SF
    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ActIndx: Annotated[int, ("SunSpecPoint", {'name': 'ActIndx', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model133ActSchd(IntFlag):
    """
    Bitfield of active schedules

    Members:
        SCHED1 (int): SCHED1
        SCHED2 (int): SCHED2
        SCHED3 (int): SCHED3
        SCHED4 (int): SCHED4
        SCHED5 (int): SCHED5
        SCHED6 (int): SCHED6
        SCHED7 (int): SCHED7
        SCHED8 (int): SCHED8
        SCHED9 (int): SCHED9
        SCHED10 (int): SCHED10
        SCHED12 (int): SCHED12
        SCHED13 (int): SCHED13
        SCHED14 (int): SCHED14
        SCHED15 (int): SCHED15
        SCHED16 (int): SCHED16
        SCHED17 (int): SCHED17
        SCHED18 (int): SCHED18
        SCHED19 (int): SCHED19
        SCHED20 (int): SCHED20
        SCHED21 (int): SCHED21
        SCHED22 (int): SCHED22
        SCHED23 (int): SCHED23
        SCHED24 (int): SCHED24
        SCHED25 (int): SCHED25
        SCHED26 (int): SCHED26
        SCHED27 (int): SCHED27
        SCHED28 (int): SCHED28
        SCHED29 (int): SCHED29
        SCHED30 (int): SCHED30
        SCHED31 (int): SCHED31
        SCHED32 (int): SCHED32
    """
    SCHED1 = 1 << 0
    SCHED2 = 1 << 1
    SCHED3 = 1 << 2
    SCHED4 = 1 << 3
    SCHED5 = 1 << 4
    SCHED6 = 1 << 5
    SCHED7 = 1 << 6
    SCHED8 = 1 << 7
    SCHED9 = 1 << 8
    SCHED10 = 1 << 9
    SCHED12 = 1 << 10
    SCHED13 = 1 << 11
    SCHED14 = 1 << 12
    SCHED15 = 1 << 13
    SCHED16 = 1 << 14
    SCHED17 = 1 << 15
    SCHED18 = 1 << 16
    SCHED19 = 1 << 17
    SCHED20 = 1 << 18
    SCHED21 = 1 << 19
    SCHED22 = 1 << 21
    SCHED23 = 1 << 22
    SCHED24 = 1 << 23
    SCHED25 = 1 << 24
    SCHED26 = 1 << 25
    SCHED27 = 1 << 26
    SCHED28 = 1 << 27
    SCHED29 = 1 << 28
    SCHED30 = 1 << 29
    SCHED31 = 1 << 30
    SCHED32 = 1 << 31



class Model133ModEna(IntFlag):
    """
    Is basic scheduling active.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model133(SunSpecModel, model_name="schedule", id=133):
    """
    Basic Scheduling 

    Attributes:
        ActSchd (Model133ActSchd): Bitfield of active schedules
        ModEna (Model133ModEna): Is basic scheduling active.
        NSchd (int): Number of schedules supported (recommend min. 4, max 32)
        NPts (int): Number of schedule entries supported (maximum of 10).
        Pad (int): Pad register.
    """

    ActSchd: Annotated[int, ("SunSpecPoint", {'name': 'ActSchd', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    NSchd: Annotated[int, ("SunSpecPoint", {'name': 'NSchd', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPts: Annotated[int, ("SunSpecPoint", {'name': 'NPts', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    repeating: Annotated[Model133RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model133RepeatingGroup})]

