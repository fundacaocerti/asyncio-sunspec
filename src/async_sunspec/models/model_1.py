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


class Model1(SunSpecModel, model_name="common", id=1):
    """
    All SunSpec compliant devices must include this as the first model

    Attributes:
        Mn (str): Well known value registered with SunSpec for compliance
        Md (str): Manufacturer specific value (32 chars)
        Opt (str): Manufacturer specific value (16 chars)
        Vr (str): Manufacturer specific value (16 chars)
        SN (str): Manufacturer specific value (32 chars)
        DA (int): Modbus device address
        Pad (int): Force even alignment
    """

    Mn: Annotated[str, ("SunSpecPoint", {'name': 'Mn', 'ptype': 'string', 'size': 16, 'mandatory': True, 'static': True})]
    Md: Annotated[str, ("SunSpecPoint", {'name': 'Md', 'ptype': 'string', 'size': 16, 'mandatory': True, 'static': True})]
    Opt: Annotated[str, ("SunSpecPoint", {'name': 'Opt', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': True})]
    Vr: Annotated[str, ("SunSpecPoint", {'name': 'Vr', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': True})]
    SN: Annotated[str, ("SunSpecPoint", {'name': 'SN', 'ptype': 'string', 'size': 16, 'mandatory': True, 'static': True})]
    DA: Annotated[int, ("SunSpecPoint", {'name': 'DA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': True})]

