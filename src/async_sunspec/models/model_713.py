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
from enum import IntEnum


class Model713Sta(IntEnum):
    """
    Storage status.

    Members:
        OK (int): No warnings or errors pending.
        WARNING (int): One or more warnings pending.
        ERROR (int): One or more errors pending.
    """
    OK = 0
    WARNING = 1
    ERROR = 2



class Model713(SunSpecModel, model_name="DERStorageCapacity", id=713):
    """
    DER storage capacity.

    Attributes:
        WHRtg (int): Energy rating of the DER storage.
        WHAvail (int): Energy available of the DER storage (WHAvail = WHRtg * SoC * SoH)
        SoC (int): State of charge of the DER storage.
        SoH (int): State of health of the DER storage.
        Sta (Model713Sta): Storage status.
        WH_SF (int): Scale factor for energy capacity.
        Pct_SF (int): Scale factor for percentage.
    """

    WHRtg: Annotated[int, ("SunSpecPoint", {'name': 'WHRtg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: WH_SF
    WHAvail: Annotated[int, ("SunSpecPoint", {'name': 'WHAvail', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: WH_SF
    SoC: Annotated[int, ("SunSpecPoint", {'name': 'SoC', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: Pct_SF
    SoH: Annotated[int, ("SunSpecPoint", {'name': 'SoH', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: Pct_SF
    Sta: Annotated[int, ("SunSpecPoint", {'name': 'Sta', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    WH_SF: Annotated[int, ("SunSpecPoint", {'name': 'WH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Pct_SF: Annotated[int, ("SunSpecPoint", {'name': 'Pct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]

