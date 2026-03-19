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


class Model63002RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        sunssf_1 (int)
        int16_1 (int)
        int16_2 (int)
        sunssf_2 (int)
    """

    sunssf_1: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_1', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    int16_1: Annotated[int, ("SunSpecPoint", {'name': 'int16_1', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_1
    int16_2: Annotated[int, ("SunSpecPoint", {'name': 'int16_2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: sunssf_2
    sunssf_2: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_2', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]


class Model63002(SunSpecModel, model_name="model_63002", id=63002):

    repeating: Annotated[Model63002RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model63002RepeatingGroup})]

