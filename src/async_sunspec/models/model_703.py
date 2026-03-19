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


class Model703ES(IntEnum):
    """
    Permit enter service.

    Members:
        DISABLED (int): DISABLED
        ENABLED (int): ENABLED
    """
    DISABLED = 0
    ENABLED = 1



class Model703(SunSpecModel, model_name="DEREnterService", id=703):
    """
    Enter service model.

    Attributes:
        ES (Model703ES): Permit enter service.
        ESVHi (int): Enter service voltage high threshold as percent of normal voltage.
        ESVLo (int): Enter service voltage low threshold as percent of normal voltage.
        ESHzHi (int): Enter service frequency high threshold.
        ESHzLo (int): Enter service frequency low threshold.
        ESDlyTms (int): Enter service delay time in seconds.
        ESRndTms (int): Enter service random delay in seconds.
        ESRmpTms (int): Enter service ramp time in seconds.
        ESDlyRemTms (int): Enter service delay time remaining in seconds.
        V_SF (int): Voltage percentage scale factor.
        Hz_SF (int): Frequency scale factor.
    """

    ES: Annotated[int, ("SunSpecPoint", {'name': 'ES', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ESVHi: Annotated[int, ("SunSpecPoint", {'name': 'ESVHi', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    ESVLo: Annotated[int, ("SunSpecPoint", {'name': 'ESVLo', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    ESHzHi: Annotated[int, ("SunSpecPoint", {'name': 'ESHzHi', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    ESHzLo: Annotated[int, ("SunSpecPoint", {'name': 'ESHzLo', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    ESDlyTms: Annotated[int, ("SunSpecPoint", {'name': 'ESDlyTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ESRndTms: Annotated[int, ("SunSpecPoint", {'name': 'ESRndTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ESRmpTms: Annotated[int, ("SunSpecPoint", {'name': 'ESRmpTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ESDlyRemTms: Annotated[int, ("SunSpecPoint", {'name': 'ESDlyRemTms', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]

