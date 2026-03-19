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


class Model64101(SunSpecModel, model_name="model_64101", id=64101):
    """
    Attributes:
        Eltek_Country_Code (int)
        Eltek_Feeding_Phase (int)
        Eltek_APD_Method (int)
        Eltek_APD_Power_Ref (int)
        Eltek_RPS_Method (int)
        Eltek_RPS_Q_Ref (int)
        Eltek_RPS_CosPhi_Ref (int)
    """

    Eltek_Country_Code: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_Country_Code', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Eltek_Feeding_Phase: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_Feeding_Phase', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Eltek_APD_Method: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_APD_Method', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Eltek_APD_Power_Ref: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_APD_Power_Ref', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Eltek_RPS_Method: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_RPS_Method', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Eltek_RPS_Q_Ref: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_RPS_Q_Ref', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Eltek_RPS_CosPhi_Ref: Annotated[int, ("SunSpecPoint", {'name': 'Eltek_RPS_CosPhi_Ref', 'ptype': 'int16', 'mandatory': False, 'static': False})]

