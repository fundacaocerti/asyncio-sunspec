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


class Model15(SunSpecModel, model_name="model_15", id=15):
    """
    Interface counters

    Attributes:
        Clr (int): Write a "1" to clear all counters
        InCnt (int): Number of bytes received
        InUcCnt (int): Number of Unicast packets received
        InNUcCnt (int): Number of non-Unicast packets received
        InDscCnt (int): Number of inbound packets received on the interface but discarded
        InErrCnt (int): Number of inbound packets that contain errors (excluding discards)
        InUnkCnt (int): Number of inbound packets with unknown protocol
        OutCnt (int): Total number of bytes transmitted on this interface
        OutUcCnt (int): Number of Unicast packets transmitted
        OutNUcCnt (int): Number of Non-Unicast packets transmitted
        OutDscCnt (int): Number of Discarded output packets
        OutErrCnt (int): Number of outbound error packets
        Pad (int)
    """

    Clr: Annotated[int, ("SunSpecPoint", {'name': 'Clr', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    InCnt: Annotated[int, ("SunSpecPoint", {'name': 'InCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InUcCnt: Annotated[int, ("SunSpecPoint", {'name': 'InUcCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InNUcCnt: Annotated[int, ("SunSpecPoint", {'name': 'InNUcCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InDscCnt: Annotated[int, ("SunSpecPoint", {'name': 'InDscCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InErrCnt: Annotated[int, ("SunSpecPoint", {'name': 'InErrCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    InUnkCnt: Annotated[int, ("SunSpecPoint", {'name': 'InUnkCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    OutCnt: Annotated[int, ("SunSpecPoint", {'name': 'OutCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    OutUcCnt: Annotated[int, ("SunSpecPoint", {'name': 'OutUcCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    OutNUcCnt: Annotated[int, ("SunSpecPoint", {'name': 'OutNUcCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    OutDscCnt: Annotated[int, ("SunSpecPoint", {'name': 'OutDscCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    OutErrCnt: Annotated[int, ("SunSpecPoint", {'name': 'OutErrCnt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

