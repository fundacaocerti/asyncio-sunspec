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


class Model401InEvt(IntFlag):
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



class Model401StringGroup(SunSpecGroup):
    """
    Attributes:
        InID (int): Uniquely identifies this input set
        InEvt (Model401InEvt): String Input Event Flags
        InEvtVnd (int): String Input Vendor Event Flags
        InDCA (int): String Input Current
        InDCAhr (int): String Input Amp-Hours
    """

    InID: Annotated[int, ("SunSpecPoint", {'name': 'InID', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    InEvt: Annotated[int, ("SunSpecPoint", {'name': 'InEvt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    InEvtVnd: Annotated[int, ("SunSpecPoint", {'name': 'InEvtVnd', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InDCA: Annotated[int, ("SunSpecPoint", {'name': 'InDCA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: DCA_SF
    InDCAhr: Annotated[int, ("SunSpecPoint", {'name': 'InDCAhr', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: DCAhr_SF


class Model401Evt(IntFlag):
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



class Model401(SunSpecModel, model_name="string_combiner_current", id=401):
    """
    A basic string combiner

    Attributes:
        DCA_SF (int): Current scale factor
        DCAhr_SF (int): Amp-hour scale factor
        DCV_SF (int): Voltage scale factor
        DCAMax (int): Maximum DC Current Rating
        N (int): Number of Inputs
        Evt (Model401Evt): Bitmask value.  Events
        EvtVnd (int): Bitmask value.  Vendor defined events
        DCA (int): Total measured current
        DCAhr (int): Total metered Amp-hours
        DCV (int): Output Voltage
        Tmp (int): Internal operating temperature
    """

    DCA_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCA_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DCAhr_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCAhr_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCV_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCV_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DCAMax: Annotated[int, ("SunSpecPoint", {'name': 'DCAMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: DCA_SF
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Evt: Annotated[int, ("SunSpecPoint", {'name': 'Evt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    DCA: Annotated[int, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: DCA_SF
    DCAhr: Annotated[int, ("SunSpecPoint", {'name': 'DCAhr', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: DCAhr_SF
    DCV: Annotated[int, ("SunSpecPoint", {'name': 'DCV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCV_SF
    Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    string: Annotated[Model401StringGroup, ("SunSpecGroup", {"name": "string", "group_type": Model401StringGroup})]

