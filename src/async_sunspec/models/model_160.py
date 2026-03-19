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


class Model160DCSt(IntEnum):
    """
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
        RESERVED_10 (int): RESERVED_10
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
    RESERVED_10 = 10



class Model160DCEvt(IntFlag):
    """
    Members:
        GROUND_FAULT (int): GROUND_FAULT
        INPUT_OVER_VOLTAGE (int): INPUT_OVER_VOLTAGE
        RESERVED_2 (int): RESERVED_2
        DC_DISCONNECT (int): DC_DISCONNECT
        RESERVED_4 (int): RESERVED_4
        CABINET_OPEN (int): CABINET_OPEN
        MANUAL_SHUTDOWN (int): MANUAL_SHUTDOWN
        OVER_TEMP (int): OVER_TEMP
        RESERVED_8 (int): RESERVED_8
        RESERVED_9 (int): RESERVED_9
        RESERVED_10 (int): RESERVED_10
        RESERVED_11 (int): RESERVED_11
        BLOWN_FUSE (int): BLOWN_FUSE
        UNDER_TEMP (int): UNDER_TEMP
        MEMORY_LOSS (int): MEMORY_LOSS
        ARC_DETECTION (int): ARC_DETECTION
        RESERVED_16 (int): RESERVED_16
        RESERVED_17 (int): RESERVED_17
        RESERVED_18 (int): RESERVED_18
        RESERVED_19 (int): RESERVED_19
        TEST_FAILED (int): TEST_FAILED
        INPUT_UNDER_VOLTAGE (int): INPUT_UNDER_VOLTAGE
        INPUT_OVER_CURRENT (int): INPUT_OVER_CURRENT
    """
    GROUND_FAULT = 1 << 0
    INPUT_OVER_VOLTAGE = 1 << 1
    RESERVED_2 = 1 << 2
    DC_DISCONNECT = 1 << 3
    RESERVED_4 = 1 << 4
    CABINET_OPEN = 1 << 5
    MANUAL_SHUTDOWN = 1 << 6
    OVER_TEMP = 1 << 7
    RESERVED_8 = 1 << 8
    RESERVED_9 = 1 << 9
    RESERVED_10 = 1 << 10
    RESERVED_11 = 1 << 11
    BLOWN_FUSE = 1 << 12
    UNDER_TEMP = 1 << 13
    MEMORY_LOSS = 1 << 14
    ARC_DETECTION = 1 << 15
    RESERVED_16 = 1 << 16
    RESERVED_17 = 1 << 17
    RESERVED_18 = 1 << 18
    RESERVED_19 = 1 << 19
    TEST_FAILED = 1 << 20
    INPUT_UNDER_VOLTAGE = 1 << 21
    INPUT_OVER_CURRENT = 1 << 22



class Model160ModuleGroup(SunSpecGroup):
    """
    Attributes:
        ID (int)
        IDStr (str)
        DCA (int)
        DCV (int)
        DCW (int)
        DCWH (int)
        Tms (int)
        Tmp (int)
        DCSt (Model160DCSt)
        DCEvt (Model160DCEvt)
    """

    ID: Annotated[int, ("SunSpecPoint", {'name': 'ID', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    IDStr: Annotated[str, ("SunSpecPoint", {'name': 'IDStr', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False})]
    DCA: Annotated[int, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCA_SF
    DCV: Annotated[int, ("SunSpecPoint", {'name': 'DCV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCV_SF
    DCW: Annotated[int, ("SunSpecPoint", {'name': 'DCW', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCW_SF
    DCWH: Annotated[int, ("SunSpecPoint", {'name': 'DCWH', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: DCWH_SF
    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    DCSt: Annotated[int, ("SunSpecPoint", {'name': 'DCSt', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    DCEvt: Annotated[int, ("SunSpecPoint", {'name': 'DCEvt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]


class Model160Evt(IntFlag):
    """
    Members:
        GROUND_FAULT (int): GROUND_FAULT
        INPUT_OVER_VOLTAGE (int): INPUT_OVER_VOLTAGE
        RESERVED_2 (int): RESERVED_2
        DC_DISCONNECT (int): DC_DISCONNECT
        RESERVED_4 (int): RESERVED_4
        CABINET_OPEN (int): CABINET_OPEN
        MANUAL_SHUTDOWN (int): MANUAL_SHUTDOWN
        OVER_TEMP (int): OVER_TEMP
        RESERVED_8 (int): RESERVED_8
        RESERVED_9 (int): RESERVED_9
        RESERVED_10 (int): RESERVED_10
        RESERVED_11 (int): RESERVED_11
        BLOWN_FUSE (int): BLOWN_FUSE
        UNDER_TEMP (int): UNDER_TEMP
        MEMORY_LOSS (int): MEMORY_LOSS
        ARC_DETECTION (int): ARC_DETECTION
        RESERVED_16 (int): RESERVED_16
        RESERVED_17 (int): RESERVED_17
        RESERVED_18 (int): RESERVED_18
        RESERVED_19 (int): RESERVED_19
        TEST_FAILED (int): TEST_FAILED
        INPUT_UNDER_VOLTAGE (int): INPUT_UNDER_VOLTAGE
        INPUT_OVER_CURRENT (int): INPUT_OVER_CURRENT
    """
    GROUND_FAULT = 1 << 0
    INPUT_OVER_VOLTAGE = 1 << 1
    RESERVED_2 = 1 << 2
    DC_DISCONNECT = 1 << 3
    RESERVED_4 = 1 << 4
    CABINET_OPEN = 1 << 5
    MANUAL_SHUTDOWN = 1 << 6
    OVER_TEMP = 1 << 7
    RESERVED_8 = 1 << 8
    RESERVED_9 = 1 << 9
    RESERVED_10 = 1 << 10
    RESERVED_11 = 1 << 11
    BLOWN_FUSE = 1 << 12
    UNDER_TEMP = 1 << 13
    MEMORY_LOSS = 1 << 14
    ARC_DETECTION = 1 << 15
    RESERVED_16 = 1 << 16
    RESERVED_17 = 1 << 17
    RESERVED_18 = 1 << 18
    RESERVED_19 = 1 << 19
    TEST_FAILED = 1 << 20
    INPUT_UNDER_VOLTAGE = 1 << 21
    INPUT_OVER_CURRENT = 1 << 22



class Model160(SunSpecModel, model_name="mppt", id=160):
    """
    Attributes:
        DCA_SF (int)
        DCV_SF (int)
        DCW_SF (int)
        DCWH_SF (int)
        Evt (Model160Evt)
        N (int)
        TmsPer (int)
    """

    DCA_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCV_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCV_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCW_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCW_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCWH_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCWH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    TmsPer: Annotated[int, ("SunSpecPoint", {'name': 'TmsPer', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    module: Annotated[Model160ModuleGroup, ("SunSpecGroup", {"name": "module", "group_type": Model160ModuleGroup})]

