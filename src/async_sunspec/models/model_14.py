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
from enum import IntFlag


class Model14Cap(IntFlag):
    """
    Bitmask value.  Proxy configuration capabilities

    Members:
        NO_PROXY (int): NO_PROXY
        IPV4_PROXY (int): IPV4_PROXY
        IPV6_PROXY (int): IPV6_PROXY
    """
    NO_PROXY = 1 << 0
    IPV4_PROXY = 1 << 1
    IPV6_PROXY = 1 << 2



class Model14(SunSpecModel, model_name="model_14", id=14):
    """
    Include this block to allow for a proxy server

    Attributes:
        Nam (str): Interface name (8 chars)
        Cap (Model14Cap): Bitmask value.  Proxy configuration capabilities
        Cfg (int): Enumerated value.  Set proxy address type
        Typ (int): Enumerate value.  Proxy server type
        Addr (str): IPv4 or IPv6 proxy hostname or dotted address (40 chars)
        Port (int): Proxy port number
        User (str): Proxy user name
        Pw (str): Proxy password
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Cap: Annotated[int, ("SunSpecPoint", {'name': 'Cap', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Cfg: Annotated[int, ("SunSpecPoint", {'name': 'Cfg', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Typ: Annotated[int, ("SunSpecPoint", {'name': 'Typ', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Addr: Annotated[str, ("SunSpecPoint", {'name': 'Addr', 'ptype': 'string', 'size': 20, 'mandatory': True, 'static': False, 'access': 'RW'})]
    Port: Annotated[int, ("SunSpecPoint", {'name': 'Port', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    User: Annotated[str, ("SunSpecPoint", {'name': 'User', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pw: Annotated[str, ("SunSpecPoint", {'name': 'Pw', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False, 'access': 'RW'})]

