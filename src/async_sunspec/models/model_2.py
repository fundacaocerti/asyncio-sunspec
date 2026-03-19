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


class Model2St(IntEnum):
    """
    Enumerated status code

    Members:
        OFF (int): OFF
        ON (int): ON
        FULL (int): FULL
        FAULT (int): FAULT
    """
    OFF = 1
    ON = 2
    FULL = 3
    FAULT = 4



class Model2Evt(IntFlag):
    """
    Bitmask event code

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



class Model2Ctl(IntEnum):
    """
    Control register for all aggregated devices

    Members:
        NONE (int): NONE
        AUTOMATIC (int): AUTOMATIC
        FORCE_OFF (int): FORCE_OFF
        TEST (int): TEST
        THROTTLE (int): THROTTLE
    """
    NONE = 0
    AUTOMATIC = 1
    FORCE_OFF = 2
    TEST = 3
    THROTTLE = 4



class Model2(SunSpecModel, model_name="aggregator", id=2):
    """
    Aggregates a collection of models for a given model id

    Attributes:
        AID (int): Aggregated model id
        N (int): Number of aggregated models
        UN (int): Update Number.  Incrementing number each time the mapping is changed.  If the number is not changed from the last reading the direct access to a specific offset will result in reading the same logical model as before.  Otherwise the entire model must be read to refresh the changes
        St (Model2St): Enumerated status code
        StVnd (int): Vendor specific status code
        Evt (Model2Evt): Bitmask event code
        EvtVnd (int): Vendor specific event code
        Ctl (Model2Ctl): Control register for all aggregated devices
        CtlVnd (int): Vendor control register for all aggregated devices
        CtlVl (int): Numerical value used as a parameter to the control
    """

    AID: Annotated[int, ("SunSpecPoint", {'name': 'AID', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    UN: Annotated[int, ("SunSpecPoint", {'name': 'UN', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StVnd: Annotated[int, ("SunSpecPoint", {'name': 'StVnd', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CtlVnd: Annotated[int, ("SunSpecPoint", {'name': 'CtlVnd', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    CtlVl: Annotated[int, ("SunSpecPoint", {'name': 'CtlVl', 'ptype': 'uint32', 'mandatory': False, 'static': False})]

