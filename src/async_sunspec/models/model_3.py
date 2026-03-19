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


class Model3RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        DS (int): Digital Signature
    """

    DS: Annotated[int, ("SunSpecPoint", {'name': 'DS', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model3Alg(IntEnum):
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



class Model3(SunSpecModel, model_name="model_3", id=3):
    """
    Request a digital signature over a specified set of data registers

    Attributes:
        X (int): Number of registers being requested
        Off1 (int): Offset of value to read
        Off2 (int)
        Off3 (int)
        Off4 (int)
        Off5 (int)
        Off6 (int)
        Off7 (int)
        Off8 (int)
        Off9 (int)
        Off10 (int)
        Off11 (int)
        Off12 (int)
        Off13 (int)
        Off14 (int)
        Off15 (int)
        Off16 (int)
        Off17 (int)
        Off18 (int)
        Off19 (int)
        Off20 (int)
        Off21 (int)
        Off22 (int)
        Off23 (int)
        Off24 (int)
        Off25 (int)
        Off26 (int)
        Off27 (int)
        Off28 (int)
        Off29 (int)
        Off30 (int)
        Off31 (int)
        Off32 (int)
        Off33 (int)
        Off34 (int)
        Off35 (int)
        Off36 (int)
        Off37 (int)
        Off38 (int)
        Off39 (int)
        Off40 (int)
        Off41 (int)
        Off42 (int)
        Off43 (int)
        Off44 (int)
        Off45 (int)
        Off46 (int)
        Off47 (int)
        Off48 (int)
        Off49 (int)
        Off50 (int)
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of request
        Role (int): Digital Signature ID
        Alg (Model3Alg): Algorithm used to compute the digital signature
        N (int): Number of registers comprising the digital signature.
    """

    X: Annotated[int, ("SunSpecPoint", {'name': 'X', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off1: Annotated[int, ("SunSpecPoint", {'name': 'Off1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off2: Annotated[int, ("SunSpecPoint", {'name': 'Off2', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off3: Annotated[int, ("SunSpecPoint", {'name': 'Off3', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off4: Annotated[int, ("SunSpecPoint", {'name': 'Off4', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off5: Annotated[int, ("SunSpecPoint", {'name': 'Off5', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off6: Annotated[int, ("SunSpecPoint", {'name': 'Off6', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off7: Annotated[int, ("SunSpecPoint", {'name': 'Off7', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off8: Annotated[int, ("SunSpecPoint", {'name': 'Off8', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off9: Annotated[int, ("SunSpecPoint", {'name': 'Off9', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off10: Annotated[int, ("SunSpecPoint", {'name': 'Off10', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off11: Annotated[int, ("SunSpecPoint", {'name': 'Off11', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off12: Annotated[int, ("SunSpecPoint", {'name': 'Off12', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off13: Annotated[int, ("SunSpecPoint", {'name': 'Off13', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off14: Annotated[int, ("SunSpecPoint", {'name': 'Off14', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off15: Annotated[int, ("SunSpecPoint", {'name': 'Off15', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off16: Annotated[int, ("SunSpecPoint", {'name': 'Off16', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off17: Annotated[int, ("SunSpecPoint", {'name': 'Off17', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off18: Annotated[int, ("SunSpecPoint", {'name': 'Off18', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off19: Annotated[int, ("SunSpecPoint", {'name': 'Off19', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off20: Annotated[int, ("SunSpecPoint", {'name': 'Off20', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off21: Annotated[int, ("SunSpecPoint", {'name': 'Off21', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off22: Annotated[int, ("SunSpecPoint", {'name': 'Off22', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off23: Annotated[int, ("SunSpecPoint", {'name': 'Off23', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off24: Annotated[int, ("SunSpecPoint", {'name': 'Off24', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off25: Annotated[int, ("SunSpecPoint", {'name': 'Off25', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off26: Annotated[int, ("SunSpecPoint", {'name': 'Off26', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off27: Annotated[int, ("SunSpecPoint", {'name': 'Off27', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off28: Annotated[int, ("SunSpecPoint", {'name': 'Off28', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off29: Annotated[int, ("SunSpecPoint", {'name': 'Off29', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off30: Annotated[int, ("SunSpecPoint", {'name': 'Off30', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off31: Annotated[int, ("SunSpecPoint", {'name': 'Off31', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off32: Annotated[int, ("SunSpecPoint", {'name': 'Off32', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off33: Annotated[int, ("SunSpecPoint", {'name': 'Off33', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off34: Annotated[int, ("SunSpecPoint", {'name': 'Off34', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off35: Annotated[int, ("SunSpecPoint", {'name': 'Off35', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off36: Annotated[int, ("SunSpecPoint", {'name': 'Off36', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off37: Annotated[int, ("SunSpecPoint", {'name': 'Off37', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off38: Annotated[int, ("SunSpecPoint", {'name': 'Off38', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off39: Annotated[int, ("SunSpecPoint", {'name': 'Off39', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off40: Annotated[int, ("SunSpecPoint", {'name': 'Off40', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off41: Annotated[int, ("SunSpecPoint", {'name': 'Off41', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off42: Annotated[int, ("SunSpecPoint", {'name': 'Off42', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off43: Annotated[int, ("SunSpecPoint", {'name': 'Off43', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off44: Annotated[int, ("SunSpecPoint", {'name': 'Off44', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off45: Annotated[int, ("SunSpecPoint", {'name': 'Off45', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off46: Annotated[int, ("SunSpecPoint", {'name': 'Off46', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off47: Annotated[int, ("SunSpecPoint", {'name': 'Off47', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off48: Annotated[int, ("SunSpecPoint", {'name': 'Off48', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off49: Annotated[int, ("SunSpecPoint", {'name': 'Off49', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off50: Annotated[int, ("SunSpecPoint", {'name': 'Off50', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Role: Annotated[int, ("SunSpecPoint", {'name': 'Role', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    repeating: Annotated[Model3RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model3RepeatingGroup})]

