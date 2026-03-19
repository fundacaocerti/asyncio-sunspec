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


class Model4RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        DS (int): Digital Signature
    """

    DS: Annotated[int, ("SunSpecPoint", {'name': 'DS', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model4Sts(IntEnum):
    """
    Status of last read operation

    Members:
        SUCCESS (int): SUCCESS
        DS (int): DS
        ACL (int): ACL
        OFF (int): OFF
    """
    SUCCESS = 0
    DS = 1
    ACL = 2
    OFF = 3



class Model4Alm(IntEnum):
    """
    Bitmask alarm code

    Members:
        NONE (int): NONE
        ALM (int): ALM
    """
    NONE = 0
    ALM = 1



class Model4Alg(IntEnum):
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



class Model4(SunSpecModel, model_name="model_4", id=4):
    """
    Compute a digital signature over a specified set of data registers

    Attributes:
        RqSeq (int): Sequence number from the request
        Sts (Model4Sts): Status of last read operation
        X (int): Number of values from the request
        Val1 (int): Copy of value from register Off1.
        Val2 (int)
        Val3 (int)
        Val4 (int)
        Val5 (int)
        Val6 (int)
        Val7 (int)
        Val8 (int)
        Val9 (int)
        Val10 (int)
        Val11 (int)
        Val12 (int)
        Val13 (int)
        Val14 (int)
        Val15 (int)
        Val16 (int)
        Val17 (int)
        Val18 (int)
        Val19 (int)
        Val20 (int)
        Val21 (int)
        Val22 (int)
        Val23 (int)
        Val24 (int)
        Val25 (int)
        Val26 (int)
        Val27 (int)
        Val28 (int)
        Val29 (int)
        Val30 (int)
        Val31 (int)
        Val32 (int)
        Val33 (int)
        Val34 (int)
        Val35 (int)
        Val36 (int)
        Val37 (int)
        Val38 (int)
        Val39 (int)
        Val40 (int)
        Val41 (int)
        Val42 (int)
        Val43 (int)
        Val44 (int)
        Val45 (int)
        Val46 (int)
        Val47 (int)
        Val48 (int)
        Val49 (int)
        Val50 (int)
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of response
        Alm (Model4Alm): Bitmask alarm code
        Alg (Model4Alg): Algorithm used to compute the digital signature
        N (int): Number of registers comprising the digital signature.
    """

    RqSeq: Annotated[int, ("SunSpecPoint", {'name': 'RqSeq', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Sts: Annotated[int, ("SunSpecPoint", {'name': 'Sts', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    X: Annotated[int, ("SunSpecPoint", {'name': 'X', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val1: Annotated[int, ("SunSpecPoint", {'name': 'Val1', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val2: Annotated[int, ("SunSpecPoint", {'name': 'Val2', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val3: Annotated[int, ("SunSpecPoint", {'name': 'Val3', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val4: Annotated[int, ("SunSpecPoint", {'name': 'Val4', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val5: Annotated[int, ("SunSpecPoint", {'name': 'Val5', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val6: Annotated[int, ("SunSpecPoint", {'name': 'Val6', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val7: Annotated[int, ("SunSpecPoint", {'name': 'Val7', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val8: Annotated[int, ("SunSpecPoint", {'name': 'Val8', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val9: Annotated[int, ("SunSpecPoint", {'name': 'Val9', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val10: Annotated[int, ("SunSpecPoint", {'name': 'Val10', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val11: Annotated[int, ("SunSpecPoint", {'name': 'Val11', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val12: Annotated[int, ("SunSpecPoint", {'name': 'Val12', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val13: Annotated[int, ("SunSpecPoint", {'name': 'Val13', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val14: Annotated[int, ("SunSpecPoint", {'name': 'Val14', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val15: Annotated[int, ("SunSpecPoint", {'name': 'Val15', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val16: Annotated[int, ("SunSpecPoint", {'name': 'Val16', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val17: Annotated[int, ("SunSpecPoint", {'name': 'Val17', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val18: Annotated[int, ("SunSpecPoint", {'name': 'Val18', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val19: Annotated[int, ("SunSpecPoint", {'name': 'Val19', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val20: Annotated[int, ("SunSpecPoint", {'name': 'Val20', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val21: Annotated[int, ("SunSpecPoint", {'name': 'Val21', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val22: Annotated[int, ("SunSpecPoint", {'name': 'Val22', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val23: Annotated[int, ("SunSpecPoint", {'name': 'Val23', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val24: Annotated[int, ("SunSpecPoint", {'name': 'Val24', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val25: Annotated[int, ("SunSpecPoint", {'name': 'Val25', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val26: Annotated[int, ("SunSpecPoint", {'name': 'Val26', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val27: Annotated[int, ("SunSpecPoint", {'name': 'Val27', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val28: Annotated[int, ("SunSpecPoint", {'name': 'Val28', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val29: Annotated[int, ("SunSpecPoint", {'name': 'Val29', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val30: Annotated[int, ("SunSpecPoint", {'name': 'Val30', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val31: Annotated[int, ("SunSpecPoint", {'name': 'Val31', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val32: Annotated[int, ("SunSpecPoint", {'name': 'Val32', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val33: Annotated[int, ("SunSpecPoint", {'name': 'Val33', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val34: Annotated[int, ("SunSpecPoint", {'name': 'Val34', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val35: Annotated[int, ("SunSpecPoint", {'name': 'Val35', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val36: Annotated[int, ("SunSpecPoint", {'name': 'Val36', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val37: Annotated[int, ("SunSpecPoint", {'name': 'Val37', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val38: Annotated[int, ("SunSpecPoint", {'name': 'Val38', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val39: Annotated[int, ("SunSpecPoint", {'name': 'Val39', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val40: Annotated[int, ("SunSpecPoint", {'name': 'Val40', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val41: Annotated[int, ("SunSpecPoint", {'name': 'Val41', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val42: Annotated[int, ("SunSpecPoint", {'name': 'Val42', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val43: Annotated[int, ("SunSpecPoint", {'name': 'Val43', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val44: Annotated[int, ("SunSpecPoint", {'name': 'Val44', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val45: Annotated[int, ("SunSpecPoint", {'name': 'Val45', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val46: Annotated[int, ("SunSpecPoint", {'name': 'Val46', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val47: Annotated[int, ("SunSpecPoint", {'name': 'Val47', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val48: Annotated[int, ("SunSpecPoint", {'name': 'Val48', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val49: Annotated[int, ("SunSpecPoint", {'name': 'Val49', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Val50: Annotated[int, ("SunSpecPoint", {'name': 'Val50', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Alm: Annotated[int, ("SunSpecPoint", {'name': 'Alm', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    repeating: Annotated[Model4RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model4RepeatingGroup})]

