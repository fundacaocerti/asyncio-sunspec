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


class Model5RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        DS (int): Digital Signature
    """

    DS: Annotated[int, ("SunSpecPoint", {'name': 'DS', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]


class Model5Alg(IntEnum):
    """
    Algorithm used to compute the digital signature

    Members:
        NONE (int): NONE
        AES_GMAC_64 (int): AES_GMAC_64
        ECC_256 (int): ECC_256
    """
    NONE = 0
    AES_GMAC_64 = 1
    ECC_256 = 2



class Model5(SunSpecModel, model_name="model_5", id=5):
    """
    Include a digital signature along with the control data

    Attributes:
        X (int): Number of (offset, value) pairs being written
        Off1 (int): Offset of control register to write value to
        Val1 (int): Value to write to control register at offset
        Off2 (int)
        Val2 (int)
        Off3 (int)
        Val3 (int)
        Off4 (int)
        Val4 (int)
        Off5 (int)
        Val5 (int)
        Off6 (int)
        Val6 (int)
        Off7 (int)
        Val7 (int)
        Off8 (int)
        Val8 (int)
        Off9 (int)
        Val9 (int)
        Off10 (int)
        Val10 (int)
        Off11 (int)
        Val11 (int)
        Off12 (int)
        Val12 (int)
        Off13 (int)
        Val13 (int)
        Off14 (int)
        Val14 (int)
        Off15 (int)
        Val15 (int)
        Off16 (int)
        Val16 (int)
        Off17 (int)
        Val17 (int)
        Off18 (int)
        Val18 (int)
        Off19 (int)
        Val19 (int)
        Off20 (int)
        Val20 (int)
        Off21 (int)
        Val21 (int)
        Off22 (int)
        Val22 (int)
        Off23 (int)
        Val23 (int)
        Off24 (int)
        Val24 (int)
        Off25 (int)
        Val25 (int)
        Off26 (int)
        Val26 (int)
        Off27 (int)
        Val27 (int)
        Off28 (int)
        Val28 (int)
        Off29 (int)
        Val29 (int)
        Off30 (int)
        Val30 (int)
        Off31 (int)
        Val31 (int)
        Off32 (int)
        Val32 (int)
        Off33 (int)
        Val33 (int)
        Off34 (int)
        Val34 (int)
        Off35 (int)
        Val35 (int)
        Off36 (int)
        Val36 (int)
        Off37 (int)
        Val37 (int)
        Off38 (int)
        Val38 (int)
        Off39 (int)
        Val39 (int)
        Off40 (int)
        Val40 (int)
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of request
        Role (int): Signing key used 0-5
        Alg (Model5Alg): Algorithm used to compute the digital signature
        N (int): Number of registers comprising the digital signature.
    """

    X: Annotated[int, ("SunSpecPoint", {'name': 'X', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off1: Annotated[int, ("SunSpecPoint", {'name': 'Off1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val1: Annotated[int, ("SunSpecPoint", {'name': 'Val1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off2: Annotated[int, ("SunSpecPoint", {'name': 'Off2', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val2: Annotated[int, ("SunSpecPoint", {'name': 'Val2', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off3: Annotated[int, ("SunSpecPoint", {'name': 'Off3', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val3: Annotated[int, ("SunSpecPoint", {'name': 'Val3', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off4: Annotated[int, ("SunSpecPoint", {'name': 'Off4', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val4: Annotated[int, ("SunSpecPoint", {'name': 'Val4', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off5: Annotated[int, ("SunSpecPoint", {'name': 'Off5', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val5: Annotated[int, ("SunSpecPoint", {'name': 'Val5', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off6: Annotated[int, ("SunSpecPoint", {'name': 'Off6', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val6: Annotated[int, ("SunSpecPoint", {'name': 'Val6', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off7: Annotated[int, ("SunSpecPoint", {'name': 'Off7', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val7: Annotated[int, ("SunSpecPoint", {'name': 'Val7', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off8: Annotated[int, ("SunSpecPoint", {'name': 'Off8', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val8: Annotated[int, ("SunSpecPoint", {'name': 'Val8', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off9: Annotated[int, ("SunSpecPoint", {'name': 'Off9', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val9: Annotated[int, ("SunSpecPoint", {'name': 'Val9', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off10: Annotated[int, ("SunSpecPoint", {'name': 'Off10', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val10: Annotated[int, ("SunSpecPoint", {'name': 'Val10', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off11: Annotated[int, ("SunSpecPoint", {'name': 'Off11', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val11: Annotated[int, ("SunSpecPoint", {'name': 'Val11', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off12: Annotated[int, ("SunSpecPoint", {'name': 'Off12', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val12: Annotated[int, ("SunSpecPoint", {'name': 'Val12', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off13: Annotated[int, ("SunSpecPoint", {'name': 'Off13', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val13: Annotated[int, ("SunSpecPoint", {'name': 'Val13', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off14: Annotated[int, ("SunSpecPoint", {'name': 'Off14', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val14: Annotated[int, ("SunSpecPoint", {'name': 'Val14', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off15: Annotated[int, ("SunSpecPoint", {'name': 'Off15', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val15: Annotated[int, ("SunSpecPoint", {'name': 'Val15', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off16: Annotated[int, ("SunSpecPoint", {'name': 'Off16', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val16: Annotated[int, ("SunSpecPoint", {'name': 'Val16', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off17: Annotated[int, ("SunSpecPoint", {'name': 'Off17', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val17: Annotated[int, ("SunSpecPoint", {'name': 'Val17', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off18: Annotated[int, ("SunSpecPoint", {'name': 'Off18', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val18: Annotated[int, ("SunSpecPoint", {'name': 'Val18', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off19: Annotated[int, ("SunSpecPoint", {'name': 'Off19', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val19: Annotated[int, ("SunSpecPoint", {'name': 'Val19', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off20: Annotated[int, ("SunSpecPoint", {'name': 'Off20', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val20: Annotated[int, ("SunSpecPoint", {'name': 'Val20', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off21: Annotated[int, ("SunSpecPoint", {'name': 'Off21', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val21: Annotated[int, ("SunSpecPoint", {'name': 'Val21', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off22: Annotated[int, ("SunSpecPoint", {'name': 'Off22', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val22: Annotated[int, ("SunSpecPoint", {'name': 'Val22', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off23: Annotated[int, ("SunSpecPoint", {'name': 'Off23', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val23: Annotated[int, ("SunSpecPoint", {'name': 'Val23', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off24: Annotated[int, ("SunSpecPoint", {'name': 'Off24', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val24: Annotated[int, ("SunSpecPoint", {'name': 'Val24', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off25: Annotated[int, ("SunSpecPoint", {'name': 'Off25', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val25: Annotated[int, ("SunSpecPoint", {'name': 'Val25', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off26: Annotated[int, ("SunSpecPoint", {'name': 'Off26', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val26: Annotated[int, ("SunSpecPoint", {'name': 'Val26', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off27: Annotated[int, ("SunSpecPoint", {'name': 'Off27', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val27: Annotated[int, ("SunSpecPoint", {'name': 'Val27', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off28: Annotated[int, ("SunSpecPoint", {'name': 'Off28', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val28: Annotated[int, ("SunSpecPoint", {'name': 'Val28', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off29: Annotated[int, ("SunSpecPoint", {'name': 'Off29', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val29: Annotated[int, ("SunSpecPoint", {'name': 'Val29', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off30: Annotated[int, ("SunSpecPoint", {'name': 'Off30', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val30: Annotated[int, ("SunSpecPoint", {'name': 'Val30', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off31: Annotated[int, ("SunSpecPoint", {'name': 'Off31', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val31: Annotated[int, ("SunSpecPoint", {'name': 'Val31', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off32: Annotated[int, ("SunSpecPoint", {'name': 'Off32', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val32: Annotated[int, ("SunSpecPoint", {'name': 'Val32', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off33: Annotated[int, ("SunSpecPoint", {'name': 'Off33', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val33: Annotated[int, ("SunSpecPoint", {'name': 'Val33', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off34: Annotated[int, ("SunSpecPoint", {'name': 'Off34', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val34: Annotated[int, ("SunSpecPoint", {'name': 'Val34', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off35: Annotated[int, ("SunSpecPoint", {'name': 'Off35', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val35: Annotated[int, ("SunSpecPoint", {'name': 'Val35', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off36: Annotated[int, ("SunSpecPoint", {'name': 'Off36', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val36: Annotated[int, ("SunSpecPoint", {'name': 'Val36', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off37: Annotated[int, ("SunSpecPoint", {'name': 'Off37', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val37: Annotated[int, ("SunSpecPoint", {'name': 'Val37', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off38: Annotated[int, ("SunSpecPoint", {'name': 'Off38', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val38: Annotated[int, ("SunSpecPoint", {'name': 'Val38', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off39: Annotated[int, ("SunSpecPoint", {'name': 'Off39', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val39: Annotated[int, ("SunSpecPoint", {'name': 'Val39', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off40: Annotated[int, ("SunSpecPoint", {'name': 'Off40', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val40: Annotated[int, ("SunSpecPoint", {'name': 'Val40', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Role: Annotated[int, ("SunSpecPoint", {'name': 'Role', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    repeating: Annotated[Model5RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model5RepeatingGroup})]

