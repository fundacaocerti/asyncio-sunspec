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


class Model18(SunSpecModel, model_name="model_18", id=18):
    """
    Include this model to support a cellular interface link

    Attributes:
        Nam (str): Interface name
        IMEI (int): International Mobile Equipment Identifier for the interface
        APN (str): Access Point Name for the interface
        Num (str): Phone number for the interface
        Pin (str): Personal Identification Number for the interface
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    IMEI: Annotated[int, ("SunSpecPoint", {'name': 'IMEI', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    APN: Annotated[str, ("SunSpecPoint", {'name': 'APN', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Num: Annotated[str, ("SunSpecPoint", {'name': 'Num', 'ptype': 'string', 'size': 6, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pin: Annotated[str, ("SunSpecPoint", {'name': 'Pin', 'ptype': 'string', 'size': 6, 'mandatory': False, 'static': False, 'access': 'RW'})]

