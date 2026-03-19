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


class Model145(SunSpecModel, model_name="ext_settings", id=145):
    """
    Inverter controls extended settings 

    Attributes:
        NomRmpUpRte (int): Ramp up rate as a percentage of max current.
        NomRmpDnRte (int): Ramp down rate as a percentage of max current.
        EmgRmpUpRte (int): Emergency ramp up rate as a percentage of max current.
        EmgRmpDnRte (int): Emergency ramp down rate as a percentage of max current.
        ConnRmpUpRte (int): Connect ramp up rate as a percentage of max current.
        ConnRmpDnRte (int): Connect ramp down rate as a percentage of max current.
        AGra (int): Ramp rate specified in percent of max current.
        Rmp_SF (int): Ramp Rate Scale Factor
    """

    NomRmpUpRte: Annotated[int, ("SunSpecPoint", {'name': 'NomRmpUpRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    NomRmpDnRte: Annotated[int, ("SunSpecPoint", {'name': 'NomRmpDnRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    EmgRmpUpRte: Annotated[int, ("SunSpecPoint", {'name': 'EmgRmpUpRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    EmgRmpDnRte: Annotated[int, ("SunSpecPoint", {'name': 'EmgRmpDnRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    ConnRmpUpRte: Annotated[int, ("SunSpecPoint", {'name': 'ConnRmpUpRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    ConnRmpDnRte: Annotated[int, ("SunSpecPoint", {'name': 'ConnRmpDnRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    AGra: Annotated[int, ("SunSpecPoint", {'name': 'AGra', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Rmp_SF
    Rmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'Rmp_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]

