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


class Model308(SunSpecModel, model_name="mini_met", id=308):
    """
    Include to support a few basic measurements

    Attributes:
        GHI (int): Global Horizontal Irradiance
        TmpBOM (int): Back of module temperature measurement
        TmpAmb (int)
        WndSpd (int)
    """

    GHI: Annotated[int, ("SunSpecPoint", {'name': 'GHI', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    TmpBOM: Annotated[int, ("SunSpecPoint", {'name': 'TmpBOM', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: -1
    TmpAmb: Annotated[int, ("SunSpecPoint", {'name': 'TmpAmb', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: -1
    WndSpd: Annotated[int, ("SunSpecPoint", {'name': 'WndSpd', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

