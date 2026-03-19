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


class Model306(SunSpecModel, model_name="ref_point", id=306):
    """
    Include to support a standard reference point

    Attributes:
        GHI (int): Global Horizontal Irradiance
        A (int): Current measurement at reference point
        V (int): Voltage  measurement at reference point
        Tmp (int): Temperature measurement at reference point
    """

    GHI: Annotated[int, ("SunSpecPoint", {'name': 'GHI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Tmp', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

