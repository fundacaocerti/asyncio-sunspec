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


class Model809CellGroup(SunSpecGroup):
    """
    Attributes:
        CellTBD (int)
    """

    CellTBD: Annotated[int, ("SunSpecPoint", {'name': 'CellTBD', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model809(SunSpecModel, model_name="flow_battery_stack", id=809):
    """
    Attributes:
        StackTBD (int)
    """

    StackTBD: Annotated[int, ("SunSpecPoint", {'name': 'StackTBD', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    cell: Annotated[Model809CellGroup, ("SunSpecGroup", {"name": "cell", "group_type": Model809CellGroup})]

