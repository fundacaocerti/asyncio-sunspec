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


class Model19Pty(IntEnum):
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



class Model19Dup(IntEnum):
    """
    Enumerated value.  Duplex mode

    Members:
        FULL (int): FULL
        HALF (int): HALF
    """
    FULL = 0
    HALF = 1



class Model19Flw(IntEnum):
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



class Model19Auth(IntEnum):
    """
    Enumerated value.  Authentication method

    Members:
        NONE (int): NONE
        PAP (int): PAP
        CHAP (int): CHAP
    """
    NONE = 0
    PAP = 1
    CHAP = 2



class Model19(SunSpecModel, model_name="model_19", id=19):
    """
    Include this model to configure a Point-to-Point Protocol link

    Attributes:
        Nam (str): Interface name
        Rte (int): Interface baud rate in bits per second
        Bits (int): Number of data bits per character
        Pty (Model19Pty): Bitmask value.  Parity setting
        Dup (Model19Dup): Enumerated value.  Duplex mode
        Flw (Model19Flw): Flow Control Method
        Auth (Model19Auth): Enumerated value.  Authentication method
        UsrNam (str): Username for authentication
        Pw (str): Password for authentication
        Pad (int)
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Rte: Annotated[int, ("SunSpecPoint", {'name': 'Rte', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Bits: Annotated[int, ("SunSpecPoint", {'name': 'Bits', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Pty: Annotated[int, ("SunSpecPoint", {'name': 'Pty', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Dup: Annotated[int, ("SunSpecPoint", {'name': 'Dup', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Flw: Annotated[int, ("SunSpecPoint", {'name': 'Flw', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Auth: Annotated[int, ("SunSpecPoint", {'name': 'Auth', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    UsrNam: Annotated[str, ("SunSpecPoint", {'name': 'UsrNam', 'ptype': 'string', 'size': 12, 'mandatory': False, 'static': False})]
    Pw: Annotated[str, ("SunSpecPoint", {'name': 'Pw', 'ptype': 'string', 'size': 6, 'mandatory': False, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

