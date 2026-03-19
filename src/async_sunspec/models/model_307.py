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


class Model307(SunSpecModel, model_name="base_met", id=307):
    """
    Base Meteorological Model

    Attributes:
        TmpAmb (int)
        RH (int)
        Pres (int)
        WndSpd (int)
        WndDir (int)
        Rain (int)
        Snw (int)
        PPT (int):  Precipitation Type (WMO 4680 SYNOP code reference)
        ElecFld (int)
        SurWet (int)
        SoilWet (int)
    """

    TmpAmb: Annotated[int, ("SunSpecPoint", {'name': 'TmpAmb', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: -1
    RH: Annotated[int, ("SunSpecPoint", {'name': 'RH', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Pres: Annotated[int, ("SunSpecPoint", {'name': 'Pres', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    WndSpd: Annotated[int, ("SunSpecPoint", {'name': 'WndSpd', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    WndDir: Annotated[int, ("SunSpecPoint", {'name': 'WndDir', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Rain: Annotated[int, ("SunSpecPoint", {'name': 'Rain', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Snw: Annotated[int, ("SunSpecPoint", {'name': 'Snw', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    PPT: Annotated[int, ("SunSpecPoint", {'name': 'PPT', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    ElecFld: Annotated[int, ("SunSpecPoint", {'name': 'ElecFld', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    SurWet: Annotated[int, ("SunSpecPoint", {'name': 'SurWet', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    SoilWet: Annotated[int, ("SunSpecPoint", {'name': 'SoilWet', 'ptype': 'int16', 'mandatory': False, 'static': False})]

