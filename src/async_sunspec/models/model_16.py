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
from enum import IntEnum, IntFlag


class Model16Cfg(IntEnum):
    """
    Enumerated value.  Force IPv4 configuration method

    Members:
        STATIC (int): STATIC
        DHCP (int): DHCP
    """
    STATIC = 0
    DHCP = 1



class Model16Ctl(IntFlag):
    """
    Bitmask value Configure use of services

    Members:
        ENABLE_DNS (int): ENABLE_DNS
        ENABLE_NTP (int): ENABLE_NTP
    """
    ENABLE_DNS = 1 << 0
    ENABLE_NTP = 1 << 1



class Model16LnkCtl(IntFlag):
    """
    Bitmask value.  Link control flags

    Members:
        AUTONEGOTIATE (int): AUTONEGOTIATE
        FULL_DUPLEX (int): FULL_DUPLEX
        FORCE_10MB (int): FORCE_10MB
        FORCE_100MB (int): FORCE_100MB
        FORCE_1GB (int): FORCE_1GB
    """
    AUTONEGOTIATE = 1 << 0
    FULL_DUPLEX = 1 << 1
    FORCE_10MB = 1 << 2
    FORCE_100MB = 1 << 3
    FORCE_1GB = 1 << 4



class Model16(SunSpecModel, model_name="model_16", id=16):
    """
    Include this model for a simple IPv4 network stack

    Attributes:
        Nam (str): Interface name.  (8 chars)
        Cfg (Model16Cfg): Enumerated value.  Force IPv4 configuration method
        Ctl (Model16Ctl): Bitmask value Configure use of services
        Addr (str): IP address
        Msk (str): Netmask
        Gw (str): Gateway IP address
        DNS1 (str): 32 bit IP address of DNS server
        DNS2 (str): 32 bit IP address of DNS server
        MAC (str): IEEE MAC address of this interface
        LnkCtl (Model16LnkCtl): Bitmask value.  Link control flags
        Pad (int)
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Cfg: Annotated[int, ("SunSpecPoint", {'name': 'Cfg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Addr: Annotated[str, ("SunSpecPoint", {'name': 'Addr', 'ptype': 'string', 'size': 8, 'mandatory': True, 'static': False, 'access': 'RW'})]
    Msk: Annotated[str, ("SunSpecPoint", {'name': 'Msk', 'ptype': 'string', 'size': 8, 'mandatory': True, 'static': False, 'access': 'RW'})]
    Gw: Annotated[str, ("SunSpecPoint", {'name': 'Gw', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    DNS1: Annotated[str, ("SunSpecPoint", {'name': 'DNS1', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    DNS2: Annotated[str, ("SunSpecPoint", {'name': 'DNS2', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    MAC: Annotated[str, ("SunSpecPoint", {'name': 'MAC', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False})]
    LnkCtl: Annotated[int, ("SunSpecPoint", {'name': 'LnkCtl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

