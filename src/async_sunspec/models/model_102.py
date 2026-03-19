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


class Model102St(IntEnum):
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



class Model102Evt1(IntFlag):
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



class Model102(SunSpecModel, model_name="inverter_split_phase", id=102):
    """
    Include this model for split phase inverter monitoring

    Attributes:
        A (int): AC Current
        AphA (int): Phase A Current
        AphB (int): Phase B Current
        AphC (int): Phase C Current
        A_SF (int)
        PPVphAB (int): Phase Voltage AB
        PPVphBC (int): Phase Voltage BC
        PPVphCA (int): Phase Voltage CA
        PhVphA (int): Phase Voltage AN
        PhVphB (int): Phase Voltage BN
        PhVphC (int): Phase Voltage CN
        V_SF (int)
        W (int): AC Power
        W_SF (int)
        Hz (int): Line Frequency
        Hz_SF (int)
        VA (int): AC Apparent Power
        VA_SF (int)
        VAr (int): AC Reactive Power
        VAr_SF (int)
        PF (int): AC Power Factor
        PF_SF (int)
        WH (int): AC Energy
        WH_SF (int)
        DCA (int): DC Current
        DCA_SF (int)
        DCV (int): DC Voltage
        DCV_SF (int)
        DCW (int): DC Power
        DCW_SF (int)
        TmpCab (int): Cabinet Temperature
        TmpSnk (int): Heat Sink Temperature
        TmpTrns (int): Transformer Temperature
        TmpOt (int): Other Temperature
        Tmp_SF (int)
        St (Model102St): Enumerated value.  Operating state
        StVnd (int): Vendor specific operating state code
        Evt1 (Model102Evt1): Bitmask value. Event fields
        Evt2 (int): Reserved for future use
        EvtVnd1 (int): Vendor defined events
        EvtVnd2 (int): Vendor defined events
        EvtVnd3 (int): Vendor defined events
        EvtVnd4 (int): Vendor defined events
    """

    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphA: Annotated[int, ("SunSpecPoint", {'name': 'AphA', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphB: Annotated[int, ("SunSpecPoint", {'name': 'AphB', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AphC: Annotated[int, ("SunSpecPoint", {'name': 'AphC', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: A_SF
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    PPVphAB: Annotated[int, ("SunSpecPoint", {'name': 'PPVphAB', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPVphBC: Annotated[int, ("SunSpecPoint", {'name': 'PPVphBC', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PPVphCA: Annotated[int, ("SunSpecPoint", {'name': 'PPVphCA', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    PhVphA: Annotated[int, ("SunSpecPoint", {'name': 'PhVphA', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphB: Annotated[int, ("SunSpecPoint", {'name': 'PhVphB', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    PhVphC: Annotated[int, ("SunSpecPoint", {'name': 'PhVphC', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: W_SF
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: Hz_SF
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VA: Annotated[int, ("SunSpecPoint", {'name': 'VA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VA_SF
    VA_SF: Annotated[int, ("SunSpecPoint", {'name': 'VA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    VAr: Annotated[int, ("SunSpecPoint", {'name': 'VAr', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VAr_SF
    VAr_SF: Annotated[int, ("SunSpecPoint", {'name': 'VAr_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: PF_SF
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    WH: Annotated[int, ("SunSpecPoint", {'name': 'WH', 'ptype': 'uint32', 'mandatory': True, 'static': False})]  # sf: WH_SF
    WH_SF: Annotated[int, ("SunSpecPoint", {'name': 'WH_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DCA: Annotated[int, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCA_SF
    DCA_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCV: Annotated[int, ("SunSpecPoint", {'name': 'DCV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCV_SF
    DCV_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCV_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCW: Annotated[int, ("SunSpecPoint", {'name': 'DCW', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCW_SF
    DCW_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCW_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    TmpCab: Annotated[int, ("SunSpecPoint", {'name': 'TmpCab', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    TmpSnk: Annotated[int, ("SunSpecPoint", {'name': 'TmpSnk', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpTrns: Annotated[int, ("SunSpecPoint", {'name': 'TmpTrns', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    TmpOt: Annotated[int, ("SunSpecPoint", {'name': 'TmpOt', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    Tmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tmp_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StVnd: Annotated[int, ("SunSpecPoint", {'name': 'StVnd', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Evt1: Annotated[int, ("SunSpecPoint", {'name': 'Evt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Evt2: Annotated[int, ("SunSpecPoint", {'name': 'Evt2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd1: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd2: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd3: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd3', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd4: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd4', 'ptype': 'uint32', 'mandatory': False, 'static': False})]

