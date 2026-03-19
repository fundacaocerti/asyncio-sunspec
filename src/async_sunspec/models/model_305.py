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


class Model305(SunSpecModel, model_name="location", id=305):
    """
    Include to support location measurements

    Attributes:
        Tm (str): UTC 24 hour time stamp to millisecond hhmmss.sssZ format
        Date (str): UTC Date string YYYYMMDD format
        Loc (str): Location string (40 chars max)
        Lat (int): Latitude with seven degrees of precision
        Long (int): Longitude with seven degrees of precision
        Alt (int): Altitude measurement in meters
    """

    Tm: Annotated[str, ("SunSpecPoint", {'name': 'Tm', 'ptype': 'string', 'size': 6, 'mandatory': False, 'static': False})]
    Date: Annotated[str, ("SunSpecPoint", {'name': 'Date', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False})]
    Loc: Annotated[str, ("SunSpecPoint", {'name': 'Loc', 'ptype': 'string', 'size': 20, 'mandatory': False, 'static': False})]
    Lat: Annotated[int, ("SunSpecPoint", {'name': 'Lat', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: -7
    Long: Annotated[int, ("SunSpecPoint", {'name': 'Long', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: -7
    Alt: Annotated[int, ("SunSpecPoint", {'name': 'Alt', 'ptype': 'int32', 'mandatory': False, 'static': False})]

