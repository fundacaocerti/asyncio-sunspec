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


class Model501Stat(IntEnum):
    """
    Enumerated value.  Module Status Code

    Members:
        OFF (int): OFF
        SLEEPING (int): SLEEPING
        STARTING (int): STARTING
        MPPT (int): MPPT
        THROTTLED (int): THROTTLED
        SHUTTING_DOWN (int): SHUTTING_DOWN
        FAULT (int): FAULT
        STANDBY (int): STANDBY
        TEST (int): TEST
        OTHER (int): OTHER
    """
    OFF = 1
    SLEEPING = 2
    STARTING = 3
    MPPT = 4
    THROTTLED = 5
    SHUTTING_DOWN = 6
    FAULT = 7
    STANDBY = 8
    TEST = 9
    OTHER = 10



class Model501Evt(IntFlag):
    """
    Bitmask value.  Module Event Flags

    Members:
        GROUND_FAULT (int): GROUND_FAULT
        INPUT_OVER_VOLTAGE (int): INPUT_OVER_VOLTAGE
        RESERVED_2 (int): RESERVED_2
        DC_DISCONNECT (int): DC_DISCONNECT
        RESERVED_4 (int): RESERVED_4
        RESERVED_5 (int): RESERVED_5
        MANUAL_SHUTDOWN (int): MANUAL_SHUTDOWN
        OVER_TEMPERATURE (int): OVER_TEMPERATURE
        RESERVED_8 (int): RESERVED_8
        RESERVED_9 (int): RESERVED_9
        RESERVED_10 (int): RESERVED_10
        RESERVED_11 (int): RESERVED_11
        BLOWN_FUSE (int): BLOWN_FUSE
        UNDER_TEMPERATURE (int): UNDER_TEMPERATURE
        MEMORY_LOSS (int): MEMORY_LOSS
        ARC_DETECTION (int): ARC_DETECTION
        THEFT_DETECTION (int): THEFT_DETECTION
        OUTPUT_OVER_CURRENT (int): OUTPUT_OVER_CURRENT
        OUTPUT_OVER_VOLTAGE (int): OUTPUT_OVER_VOLTAGE
        OUTPUT_UNDER_VOLTAGE (int): OUTPUT_UNDER_VOLTAGE
        TEST_FAILED (int): TEST_FAILED
    """
    GROUND_FAULT = 1 << 0
    INPUT_OVER_VOLTAGE = 1 << 1
    RESERVED_2 = 1 << 2
    DC_DISCONNECT = 1 << 3
    RESERVED_4 = 1 << 4
    RESERVED_5 = 1 << 5
    MANUAL_SHUTDOWN = 1 << 6
    OVER_TEMPERATURE = 1 << 7
    RESERVED_8 = 1 << 8
    RESERVED_9 = 1 << 9
    RESERVED_10 = 1 << 10
    RESERVED_11 = 1 << 11
    BLOWN_FUSE = 1 << 12
    UNDER_TEMPERATURE = 1 << 13
    MEMORY_LOSS = 1 << 14
    ARC_DETECTION = 1 << 15
    THEFT_DETECTION = 1 << 16
    OUTPUT_OVER_CURRENT = 1 << 17
    OUTPUT_OVER_VOLTAGE = 1 << 18
    OUTPUT_UNDER_VOLTAGE = 1 << 19
    TEST_FAILED = 1 << 20



class Model501(SunSpecModel, model_name="solar_module_float", id=501):
    """
    A solar module model supporting DC-DC converter

    Attributes:
        Stat (Model501Stat): Enumerated value.  Module Status Code
        StatVend (int): Module Vendor Status Code
        Evt (Model501Evt): Bitmask value.  Module Event Flags
        EvtVend (int): Vendor specific flags
        Ctl (int): Module Control
        CtlVend (int): Vendor Module Control
        CtlVal (int): Module Control Value
        Tms (int): Time in seconds since 2000 epoch
        OutA (float): Output Current
        OutV (float): Output Voltage
        OutWh (float): Output Energy
        OutW (float): Output Power
        Tmp (float): Module Temperature
        InA (float): Input Current
        InV (float): Input Voltage
        InWh (float): Input Energy
        InW (float): Input Power
    """

    Stat: Annotated[int, ("SunSpecPoint", {'name': 'Stat', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StatVend: Annotated[int, ("SunSpecPoint", {'name': 'StatVend', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVend: Annotated[int, ("SunSpecPoint", {'name': 'EvtVend', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    CtlVend: Annotated[int, ("SunSpecPoint", {'name': 'CtlVend', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    CtlVal: Annotated[int, ("SunSpecPoint", {'name': 'CtlVal', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    OutA: Annotated[float, ("SunSpecPoint", {'name': 'OutA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    OutV: Annotated[float, ("SunSpecPoint", {'name': 'OutV', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    OutWh: Annotated[float, ("SunSpecPoint", {'name': 'OutWh', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    OutW: Annotated[float, ("SunSpecPoint", {'name': 'OutW', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    Tmp: Annotated[float, ("SunSpecPoint", {'name': 'Tmp', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    InA: Annotated[float, ("SunSpecPoint", {'name': 'InA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    InV: Annotated[float, ("SunSpecPoint", {'name': 'InV', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    InWh: Annotated[float, ("SunSpecPoint", {'name': 'InWh', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    InW: Annotated[float, ("SunSpecPoint", {'name': 'InW', 'ptype': 'float32', 'mandatory': False, 'static': False})]

