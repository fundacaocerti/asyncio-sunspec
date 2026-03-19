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


class Model304InclGroup(SunSpecGroup):
    """
    Attributes:
        Inclx (int): X-Axis inclination
        Incly (int): Y-Axis inclination
        Inclz (int): Z-Axis inclination
    """

    Inclx: Annotated[int, ("SunSpecPoint", {'name': 'Inclx', 'ptype': 'int32', 'mandatory': True, 'static': False})]  # sf: -2
    Incly: Annotated[int, ("SunSpecPoint", {'name': 'Incly', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: -2
    Inclz: Annotated[int, ("SunSpecPoint", {'name': 'Inclz', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: -2


class Model304(SunSpecModel, model_name="inclinometer", id=304):
    """
    Include to support orientation measurements
    """

    incl: Annotated[Model304InclGroup, ("SunSpecGroup", {"name": "incl", "group_type": Model304InclGroup})]

