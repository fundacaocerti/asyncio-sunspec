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


class Model303TempGroup(SunSpecGroup):
    """
    Attributes:
        TmpBOM (int): Back of module temperature measurement
    """

    TmpBOM: Annotated[int, ("SunSpecPoint", {'name': 'TmpBOM', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: -1


class Model303(SunSpecModel, model_name="bom_temp", id=303):
    """
    Include to support variable number of  back of module temperature measurements
    """

    temp: Annotated[Model303TempGroup, ("SunSpecGroup", {"name": "temp", "group_type": Model303TempGroup})]

