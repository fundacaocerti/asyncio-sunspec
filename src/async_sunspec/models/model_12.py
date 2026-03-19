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


class Model12CfgSt(IntEnum):
    """
    Enumerated value.  Configuration status

    Members:
        NOT_CONFIGURED (int): NOT_CONFIGURED
        VALID_SETTING (int): VALID_SETTING
        VALID_HW (int): VALID_HW
    """
    NOT_CONFIGURED = 0
    VALID_SETTING = 1
    VALID_HW = 2



class Model12ChgSt(IntFlag):
    """
    Bitmask value.  A configuration change is pending

    Members:
        PENDING (int): PENDING
    """
    PENDING = 1 << 0



class Model12Cap(IntFlag):
    """
    Bitmask value. Identify capable sources of configuration

    Members:
        DHCP (int): DHCP
        BOOTP (int): BOOTP
        ZEROCONF (int): ZEROCONF
        DNS (int): DNS
        CFG_SETTABLE (int): CFG_SETTABLE
        HW_CONFIG (int): HW_CONFIG
        NTP_CLIENT (int): NTP_CLIENT
        RESET_REQUIRED (int): RESET_REQUIRED
    """
    DHCP = 1 << 0
    BOOTP = 1 << 1
    ZEROCONF = 1 << 2
    DNS = 1 << 3
    CFG_SETTABLE = 1 << 4
    HW_CONFIG = 1 << 5
    NTP_CLIENT = 1 << 6
    RESET_REQUIRED = 1 << 7



class Model12Cfg(IntEnum):
    """
    Enumerated value.  Configuration method used.

    Members:
        STATIC (int): STATIC
        DHCP (int): DHCP
        BOOTP (int): BOOTP
        ZEROCONF (int): ZEROCONF
    """
    STATIC = 0
    DHCP = 1
    BOOTP = 2
    ZEROCONF = 3



class Model12Ctl(IntEnum):
    """
    Configure use of services

    Members:
        ENABLE_DNS (int): ENABLE_DNS
        ENABLE_NTP (int): ENABLE_NTP
    """
    ENABLE_DNS = 0
    ENABLE_NTP = 1



class Model12(SunSpecModel, model_name="model_12", id=12):
    """
    Include to support an IPv4 protocol stack on this interface

    Attributes:
        Nam (str): Interface name
        CfgSt (Model12CfgSt): Enumerated value.  Configuration status
        ChgSt (Model12ChgSt): Bitmask value.  A configuration change is pending
        Cap (Model12Cap): Bitmask value. Identify capable sources of configuration
        Cfg (Model12Cfg): Enumerated value.  Configuration method used.
        Ctl (Model12Ctl): Configure use of services
        Addr (str): IPv4 numeric address as a dotted string xxx.xxx.xxx.xxx
        Msk (str): IPv4 numeric netmask as a dotted string xxx.xxx.xxx.xxx
        Gw (str): IPv4 numeric gateway address as a dotted string xxx.xxx.xxx.xxx
        DNS1 (str): IPv4 numeric DNS address as a dotted string xxx.xxx.xxx.xxx
        DNS2 (str): IPv4 numeric DNS address as a dotted string xxx.xxx.xxx.xxx
        NTP1 (str): IPv4 numeric NTP address as a dotted string xxx.xxx.xxx.xxx
        NTP2 (str): IPv4 numeric NTP address as a dotted string xxx.xxx.xxx.xxx
        DomNam (str): Domain name (24 chars max)
        HostNam (str): Host name (24 chars max)
        Pad (int)
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    CfgSt: Annotated[int, ("SunSpecPoint", {'name': 'CfgSt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ChgSt: Annotated[int, ("SunSpecPoint", {'name': 'ChgSt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Cap: Annotated[int, ("SunSpecPoint", {'name': 'Cap', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Cfg: Annotated[int, ("SunSpecPoint", {'name': 'Cfg', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Addr: Annotated[str, ("SunSpecPoint", {'name': 'Addr', 'ptype': 'string', 'size': 8, 'mandatory': True, 'static': False, 'access': 'RW'})]
    Msk: Annotated[str, ("SunSpecPoint", {'name': 'Msk', 'ptype': 'string', 'size': 8, 'mandatory': True, 'static': False, 'access': 'RW'})]
    Gw: Annotated[str, ("SunSpecPoint", {'name': 'Gw', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    DNS1: Annotated[str, ("SunSpecPoint", {'name': 'DNS1', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    DNS2: Annotated[str, ("SunSpecPoint", {'name': 'DNS2', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    NTP1: Annotated[str, ("SunSpecPoint", {'name': 'NTP1', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False, 'access': 'RW'})]
    NTP2: Annotated[str, ("SunSpecPoint", {'name': 'NTP2', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False, 'access': 'RW'})]
    DomNam: Annotated[str, ("SunSpecPoint", {'name': 'DomNam', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False, 'access': 'RW'})]
    HostNam: Annotated[str, ("SunSpecPoint", {'name': 'HostNam', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

