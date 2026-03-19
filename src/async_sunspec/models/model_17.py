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


class Model17Pty(IntEnum):
    """
    Bitmask value.  Parity setting

    Members:
        NONE (int): NONE
        ODD (int): ODD
        EVEN (int): EVEN
    """
    NONE = 0
    ODD = 1
    EVEN = 2



class Model17Dup(IntEnum):
    """
    Enumerated value.  Duplex mode

    Members:
        FULL (int): FULL
        HALF (int): HALF
    """
    FULL = 0
    HALF = 1



class Model17Flw(IntEnum):
    """
    Flow Control Method

    Members:
        NONE (int): NONE
        HW (int): HW
        XONXOFF (int): XONXOFF
    """
    NONE = 0
    HW = 1
    XONXOFF = 2



class Model17Typ(IntEnum):
    """
    Enumerated value.  Interface type

    Members:
        UNKNOWN (int): UNKNOWN
        RS232 (int): RS232
        RS485 (int): RS485
    """
    UNKNOWN = 0
    RS232 = 1
    RS485 = 2



class Model17Pcol(IntEnum):
    """
    Enumerated value. Serial protocol selection

    Members:
        UNKNOWN (int): UNKNOWN
        MODBUS (int): MODBUS
        VENDOR (int): VENDOR
    """
    UNKNOWN = 0
    MODBUS = 1
    VENDOR = 2



class Model17(SunSpecModel, model_name="model_17", id=17):
    """
    Include this model for serial interface configuration support

    Attributes:
        Nam (str): Interface name (8 chars)
        Rte (int): Interface baud rate in bits per second
        Bits (int): Number of data bits per character
        Pty (Model17Pty): Bitmask value.  Parity setting
        Dup (Model17Dup): Enumerated value.  Duplex mode
        Flw (Model17Flw): Flow Control Method
        Typ (Model17Typ): Enumerated value.  Interface type
        Pcol (Model17Pcol): Enumerated value. Serial protocol selection
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Rte: Annotated[int, ("SunSpecPoint", {'name': 'Rte', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Bits: Annotated[int, ("SunSpecPoint", {'name': 'Bits', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Pty: Annotated[int, ("SunSpecPoint", {'name': 'Pty', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Dup: Annotated[int, ("SunSpecPoint", {'name': 'Dup', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Flw: Annotated[int, ("SunSpecPoint", {'name': 'Flw', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Typ: Annotated[int, ("SunSpecPoint", {'name': 'Typ', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Pcol: Annotated[int, ("SunSpecPoint", {'name': 'Pcol', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

