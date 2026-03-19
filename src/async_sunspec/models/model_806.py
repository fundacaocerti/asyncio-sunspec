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


class Model806BatteryStringGroup(SunSpecGroup):
    """
    Attributes:
        BatStTBD (int)
    """

    BatStTBD: Annotated[int, ("SunSpecPoint", {'name': 'BatStTBD', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model806(SunSpecModel, model_name="flow_battery", id=806):
    """
    Attributes:
        BatTBD (int)
    """

    BatTBD: Annotated[int, ("SunSpecPoint", {'name': 'BatTBD', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    battery_string: Annotated[Model806BatteryStringGroup, ("SunSpecGroup", {"name": "battery_string", "group_type": Model806BatteryStringGroup})]

