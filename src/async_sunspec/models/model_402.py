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


class Model402InEvt(IntFlag):
    """
    String Input Event Flags

    Members:
        LOW_VOLTAGE (int): LOW_VOLTAGE
        LOW_POWER (int): LOW_POWER
        LOW_EFFICIENCY (int): LOW_EFFICIENCY
        CURRENT (int): CURRENT
        VOLTAGE (int): VOLTAGE
        POWER (int): POWER
        PR (int): PR
        DISCONNECTED (int): DISCONNECTED
        FUSE_FAULT (int): FUSE_FAULT
        COMBINER_FUSE_FAULT (int): COMBINER_FUSE_FAULT
        COMBINER_CABINET_OPEN (int): COMBINER_CABINET_OPEN
        TEMP (int): TEMP
        GROUNDFAULT (int): GROUNDFAULT
        REVERSED_POLARITY (int): REVERSED_POLARITY
        INCOMPATIBLE (int): INCOMPATIBLE
        COMM_ERROR (int): COMM_ERROR
        INTERNAL_ERROR (int): INTERNAL_ERROR
        THEFT (int): THEFT
        ARC_DETECTED (int): ARC_DETECTED
    """
    LOW_VOLTAGE = 1 << 0
    LOW_POWER = 1 << 1
    LOW_EFFICIENCY = 1 << 2
    CURRENT = 1 << 3
    VOLTAGE = 1 << 4
    POWER = 1 << 5
    PR = 1 << 6
    DISCONNECTED = 1 << 7
    FUSE_FAULT = 1 << 8
    COMBINER_FUSE_FAULT = 1 << 9
    COMBINER_CABINET_OPEN = 1 << 10
    TEMP = 1 << 11
    GROUNDFAULT = 1 << 12
    REVERSED_POLARITY = 1 << 13
    INCOMPATIBLE = 1 << 14
    COMM_ERROR = 1 << 15
    INTERNAL_ERROR = 1 << 16
    THEFT = 1 << 17
    ARC_DETECTED = 1 << 18



class Model402StringGroup(SunSpecGroup):
    """
    Attributes:
        InID (int): Uniquely identifies this input set
        InEvt (Model402InEvt): String Input Event Flags
        EvtVnd (int): Bitmask value.  Vendor defined events
        InDCA (int): String Input Current
        InDCAhr (int): String Input Amp-Hours
        InDCV (int): String Input Voltage
        InDCW (int): String Input Power
        InDCWh (int): String Input Energy
        InDCPR (int): String Performance Ratio
        InN (int): Number of modules in this input string
    """

    InID: Annotated[int, ("SunSpecPoint", {'name': 'InID', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    InEvt: Annotated[int, ("SunSpecPoint", {'name': 'InEvt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InDCA: Annotated[int, ("SunSpecPoint", {'name': 'InDCA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: DCA_SF
    InDCAhr: Annotated[int, ("SunSpecPoint", {'name': 'InDCAhr', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: DCAhr_SF
    InDCV: Annotated[int, ("SunSpecPoint", {'name': 'InDCV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCV_SF
    InDCW: Annotated[int, ("SunSpecPoint", {'name': 'InDCW', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCWh_SF
    InDCWh: Annotated[int, ("SunSpecPoint", {'name': 'InDCWh', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InDCPR: Annotated[int, ("SunSpecPoint", {'name': 'InDCPR', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    InN: Annotated[int, ("SunSpecPoint", {'name': 'InN', 'ptype': 'uint16', 'mandatory': False, 'static': False})]


class Model402Evt(IntFlag):
    """
    Bitmask value.  Events

    Members:
        LOW_VOLTAGE (int): LOW_VOLTAGE
        LOW_POWER (int): LOW_POWER
        LOW_EFFICIENCY (int): LOW_EFFICIENCY
        CURRENT (int): CURRENT
        VOLTAGE (int): VOLTAGE
        POWER (int): POWER
        PR (int): PR
        DISCONNECTED (int): DISCONNECTED
        FUSE_FAULT (int): FUSE_FAULT
        COMBINER_FUSE_FAULT (int): COMBINER_FUSE_FAULT
        COMBINER_CABINET_OPEN (int): COMBINER_CABINET_OPEN
        TEMP (int): TEMP
        GROUNDFAULT (int): GROUNDFAULT
        REVERSED_POLARITY (int): REVERSED_POLARITY
        INCOMPATIBLE (int): INCOMPATIBLE
        COMM_ERROR (int): COMM_ERROR
        INTERNAL_ERROR (int): INTERNAL_ERROR
        THEFT (int): THEFT
        ARC_DETECTED (int): ARC_DETECTED
    """
    LOW_VOLTAGE = 1 << 0
    LOW_POWER = 1 << 1
    LOW_EFFICIENCY = 1 << 2
    CURRENT = 1 << 3
    VOLTAGE = 1 << 4
    POWER = 1 << 5
    PR = 1 << 6
    DISCONNECTED = 1 << 7
    FUSE_FAULT = 1 << 8
    COMBINER_FUSE_FAULT = 1 << 9
    COMBINER_CABINET_OPEN = 1 << 10
    TEMP = 1 << 11
    GROUNDFAULT = 1 << 12
    REVERSED_POLARITY = 1 << 13
    INCOMPATIBLE = 1 << 14
    COMM_ERROR = 1 << 15
    INTERNAL_ERROR = 1 << 16
    THEFT = 1 << 17
    ARC_DETECTED = 1 << 18



class Model402(SunSpecModel, model_name="string_combiner_advanced", id=402):
    """
    An advanced string combiner

    Attributes:
        DCA_SF (int): Current scale factor
        DCAhr_SF (int): Amp-hour scale factor
        DCV_SF (int): Voltage scale factor
        DCW_SF (int): Power scale factor
        DCWh_SF (int): Energy scale factor
        DCAMax (int): Maximum DC Current Rating
        N (int): Number of Inputs
        Evt (Model402Evt): Bitmask value.  Events
        EvtVnd (int): Bitmask value.  Vendor defined events
        DCA (int): Total measured current
        DCAhr (int): Total metered Amp-hours
        DCV (int): Output Voltage
        Tmp (int): Internal operating temperature
        DCW (int): Output power
        DCPR (int): DC Performance ratio value
        DCWh (int): Output energy
    """

    DCA_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCA_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DCAhr_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCAhr_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCV_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCV_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCW_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCW_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCWh_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCWh_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DCAMax: Annotated[int, ("SunSpecPoint", {'name': 'DCAMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    DCA: Annotated[int, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: DCA_SF
    DCAhr: Annotated[int, ("SunSpecPoint", {'name': 'DCAhr', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: DCAhr_SF
    DCV: Annotated[int, ("SunSpecPoint", {'name': 'DCV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCV_SF
    Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    DCW: Annotated[int, ("SunSpecPoint", {'name': 'DCW', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCW_SF
    DCPR: Annotated[int, ("SunSpecPoint", {'name': 'DCPR', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    DCWh: Annotated[int, ("SunSpecPoint", {'name': 'DCWh', 'ptype': 'uint32', 'mandatory': True, 'static': False})]  # sf: DCWh_SF
    string: Annotated[Model402StringGroup, ("SunSpecGroup", {"name": "string", "group_type": Model402StringGroup})]

