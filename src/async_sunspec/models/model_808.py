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


class Model808StackGroup(SunSpecGroup):
    """
    Attributes:
        StackTBD (int)
    """

    StackTBD: Annotated[int, ("SunSpecPoint", {'name': 'StackTBD', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model808(SunSpecModel, model_name="flow_battery_module", id=808):
    """
    Attributes:
        ModuleTBD (int)
    """

    ModuleTBD: Annotated[int, ("SunSpecPoint", {'name': 'ModuleTBD', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    stack: Annotated[Model808StackGroup, ("SunSpecGroup", {"name": "stack", "group_type": Model808StackGroup})]

