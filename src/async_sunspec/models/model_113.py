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


class Model113St(IntEnum):
    """
    Enumerated value.  Operating state

    Members:
        OFF (int): OFF
        SLEEPING (int): SLEEPING
        STARTING (int): STARTING
        MPPT (int): MPPT
        THROTTLED (int): THROTTLED
        SHUTTING_DOWN (int): SHUTTING_DOWN
        FAULT (int): FAULT
        STANDBY (int): STANDBY
    """
    OFF = 1
    SLEEPING = 2
    STARTING = 3
    MPPT = 4
    THROTTLED = 5
    SHUTTING_DOWN = 6
    FAULT = 7
    STANDBY = 8



class Model113Evt1(IntFlag):
    """
    Bitmask value. Event fields

    Members:
        GROUND_FAULT (int): GROUND_FAULT
        DC_OVER_VOLT (int): DC_OVER_VOLT
        AC_DISCONNECT (int): AC_DISCONNECT
        DC_DISCONNECT (int): DC_DISCONNECT
        GRID_DISCONNECT (int): GRID_DISCONNECT
        CABINET_OPEN (int): CABINET_OPEN
        MANUAL_SHUTDOWN (int): MANUAL_SHUTDOWN
        OVER_TEMP (int): OVER_TEMP
        OVER_FREQUENCY (int): OVER_FREQUENCY
        UNDER_FREQUENCY (int): UNDER_FREQUENCY
        AC_OVER_VOLT (int): AC_OVER_VOLT
        AC_UNDER_VOLT (int): AC_UNDER_VOLT
        BLOWN_STRING_FUSE (int): BLOWN_STRING_FUSE
        UNDER_TEMP (int): UNDER_TEMP
        MEMORY_LOSS (int): MEMORY_LOSS
        HW_TEST_FAILURE (int): HW_TEST_FAILURE
    """
    GROUND_FAULT = 1 << 0
    DC_OVER_VOLT = 1 << 1
    AC_DISCONNECT = 1 << 2
    DC_DISCONNECT = 1 << 3
    GRID_DISCONNECT = 1 << 4
    CABINET_OPEN = 1 << 5
    MANUAL_SHUTDOWN = 1 << 6
    OVER_TEMP = 1 << 7
    OVER_FREQUENCY = 1 << 8
    UNDER_FREQUENCY = 1 << 9
    AC_OVER_VOLT = 1 << 10
    AC_UNDER_VOLT = 1 << 11
    BLOWN_STRING_FUSE = 1 << 12
    UNDER_TEMP = 1 << 13
    MEMORY_LOSS = 1 << 14
    HW_TEST_FAILURE = 1 << 15



class Model113(SunSpecModel, model_name="inverter_three_phase_float", id=113):
    """
    Include this model for three phase inverter monitoring using float values

    Attributes:
        A (float): AC Current
        AphA (float): Phase A Current
        AphB (float): Phase B Current
        AphC (float): Phase C Current
        PPVphAB (float): Phase Voltage AB
        PPVphBC (float): Phase Voltage BC
        PPVphCA (float): Phase Voltage CA
        PhVphA (float): Phase Voltage AN
        PhVphB (float): Phase Voltage BN
        PhVphC (float): Phase Voltage CN
        W (float): AC Power
        Hz (float): Line Frequency
        VA (float): AC Apparent Power
        VAr (float): AC Reactive Power
        PF (float): AC Power Factor
        WH (float): AC Energy
        DCA (float): DC Current
        DCV (float): DC Voltage
        DCW (float): DC Power
        TmpCab (float): Cabinet Temperature
        TmpSnk (float): Heat Sink Temperature
        TmpTrns (float): Transformer Temperature
        TmpOt (float): Other Temperature
        St (Model113St): Enumerated value.  Operating state
        StVnd (int): Vendor specific operating state code
        Evt1 (Model113Evt1): Bitmask value. Event fields
        Evt2 (int): Reserved for future use
        EvtVnd1 (int): Vendor defined events
        EvtVnd2 (int): Vendor defined events
        EvtVnd3 (int): Vendor defined events
        EvtVnd4 (int): Vendor defined events
    """

    A: Annotated[float, ("SunSpecPoint", {'name': 'A', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    AphA: Annotated[float, ("SunSpecPoint", {'name': 'AphA', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    AphB: Annotated[float, ("SunSpecPoint", {'name': 'AphB', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    AphC: Annotated[float, ("SunSpecPoint", {'name': 'AphC', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PPVphAB: Annotated[float, ("SunSpecPoint", {'name': 'PPVphAB', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PPVphBC: Annotated[float, ("SunSpecPoint", {'name': 'PPVphBC', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PPVphCA: Annotated[float, ("SunSpecPoint", {'name': 'PPVphCA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PhVphA: Annotated[float, ("SunSpecPoint", {'name': 'PhVphA', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PhVphB: Annotated[float, ("SunSpecPoint", {'name': 'PhVphB', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    PhVphC: Annotated[float, ("SunSpecPoint", {'name': 'PhVphC', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    W: Annotated[float, ("SunSpecPoint", {'name': 'W', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    Hz: Annotated[float, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    VA: Annotated[float, ("SunSpecPoint", {'name': 'VA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    VAr: Annotated[float, ("SunSpecPoint", {'name': 'VAr', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    PF: Annotated[float, ("SunSpecPoint", {'name': 'PF', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    WH: Annotated[float, ("SunSpecPoint", {'name': 'WH', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    DCA: Annotated[float, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    DCV: Annotated[float, ("SunSpecPoint", {'name': 'DCV', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    DCW: Annotated[float, ("SunSpecPoint", {'name': 'DCW', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TmpCab: Annotated[float, ("SunSpecPoint", {'name': 'TmpCab', 'ptype': 'float32', 'mandatory': True, 'static': False})]
    TmpSnk: Annotated[float, ("SunSpecPoint", {'name': 'TmpSnk', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TmpTrns: Annotated[float, ("SunSpecPoint", {'name': 'TmpTrns', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    TmpOt: Annotated[float, ("SunSpecPoint", {'name': 'TmpOt', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StVnd: Annotated[int, ("SunSpecPoint", {'name': 'StVnd', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Evt1: Annotated[int, ("SunSpecPoint", {'name': 'Evt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Evt2: Annotated[int, ("SunSpecPoint", {'name': 'Evt2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd1: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd2: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd3: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd3', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd4: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd4', 'ptype': 'uint32', 'mandatory': False, 'static': False})]

