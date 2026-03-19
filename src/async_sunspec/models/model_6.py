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


class Model6RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        DS (int): Digital Signature
    """

    DS: Annotated[int, ("SunSpecPoint", {'name': 'DS', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]


class Model6Alg(IntEnum):
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



class Model6(SunSpecModel, model_name="model_6", id=6):
    """
    Include a digital signature along with the control data

    Attributes:
        X (int): Number of (offset, value) pairs being written
        Off (int): Starting offset for write operation
        Val1 (int): Value to write to control register at offset
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
        Val51 (int)
        Val52 (int)
        Val53 (int)
        Val54 (int)
        Val55 (int)
        Val56 (int)
        Val57 (int)
        Val58 (int)
        Val59 (int)
        Val60 (int)
        Val61 (int)
        Val62 (int)
        Val63 (int)
        Val64 (int)
        Val65 (int)
        Val66 (int)
        Val67 (int)
        Val68 (int)
        Val69 (int)
        Val70 (int)
        Val71 (int)
        Val72 (int)
        Val73 (int)
        Val74 (int)
        Val75 (int)
        Val76 (int)
        Val77 (int)
        Val78 (int)
        Val79 (int)
        Val80 (int)
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of request
        Role (int): Signing key used 0-5
        Rsrvd (int)
        Alg (Model6Alg): Algorithm used to compute the digital signature
        N (int): Number of registers comprising the digital signature.
    """

    X: Annotated[int, ("SunSpecPoint", {'name': 'X', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Off: Annotated[int, ("SunSpecPoint", {'name': 'Off', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val1: Annotated[int, ("SunSpecPoint", {'name': 'Val1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val2: Annotated[int, ("SunSpecPoint", {'name': 'Val2', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val3: Annotated[int, ("SunSpecPoint", {'name': 'Val3', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val4: Annotated[int, ("SunSpecPoint", {'name': 'Val4', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val5: Annotated[int, ("SunSpecPoint", {'name': 'Val5', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val6: Annotated[int, ("SunSpecPoint", {'name': 'Val6', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val7: Annotated[int, ("SunSpecPoint", {'name': 'Val7', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val8: Annotated[int, ("SunSpecPoint", {'name': 'Val8', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val9: Annotated[int, ("SunSpecPoint", {'name': 'Val9', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val10: Annotated[int, ("SunSpecPoint", {'name': 'Val10', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val11: Annotated[int, ("SunSpecPoint", {'name': 'Val11', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val12: Annotated[int, ("SunSpecPoint", {'name': 'Val12', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val13: Annotated[int, ("SunSpecPoint", {'name': 'Val13', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val14: Annotated[int, ("SunSpecPoint", {'name': 'Val14', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val15: Annotated[int, ("SunSpecPoint", {'name': 'Val15', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val16: Annotated[int, ("SunSpecPoint", {'name': 'Val16', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val17: Annotated[int, ("SunSpecPoint", {'name': 'Val17', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val18: Annotated[int, ("SunSpecPoint", {'name': 'Val18', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val19: Annotated[int, ("SunSpecPoint", {'name': 'Val19', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val20: Annotated[int, ("SunSpecPoint", {'name': 'Val20', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val21: Annotated[int, ("SunSpecPoint", {'name': 'Val21', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val22: Annotated[int, ("SunSpecPoint", {'name': 'Val22', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val23: Annotated[int, ("SunSpecPoint", {'name': 'Val23', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val24: Annotated[int, ("SunSpecPoint", {'name': 'Val24', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val25: Annotated[int, ("SunSpecPoint", {'name': 'Val25', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val26: Annotated[int, ("SunSpecPoint", {'name': 'Val26', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val27: Annotated[int, ("SunSpecPoint", {'name': 'Val27', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val28: Annotated[int, ("SunSpecPoint", {'name': 'Val28', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val29: Annotated[int, ("SunSpecPoint", {'name': 'Val29', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val30: Annotated[int, ("SunSpecPoint", {'name': 'Val30', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val31: Annotated[int, ("SunSpecPoint", {'name': 'Val31', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val32: Annotated[int, ("SunSpecPoint", {'name': 'Val32', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val33: Annotated[int, ("SunSpecPoint", {'name': 'Val33', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val34: Annotated[int, ("SunSpecPoint", {'name': 'Val34', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val35: Annotated[int, ("SunSpecPoint", {'name': 'Val35', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val36: Annotated[int, ("SunSpecPoint", {'name': 'Val36', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val37: Annotated[int, ("SunSpecPoint", {'name': 'Val37', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val38: Annotated[int, ("SunSpecPoint", {'name': 'Val38', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val39: Annotated[int, ("SunSpecPoint", {'name': 'Val39', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val40: Annotated[int, ("SunSpecPoint", {'name': 'Val40', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val41: Annotated[int, ("SunSpecPoint", {'name': 'Val41', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val42: Annotated[int, ("SunSpecPoint", {'name': 'Val42', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val43: Annotated[int, ("SunSpecPoint", {'name': 'Val43', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val44: Annotated[int, ("SunSpecPoint", {'name': 'Val44', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val45: Annotated[int, ("SunSpecPoint", {'name': 'Val45', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val46: Annotated[int, ("SunSpecPoint", {'name': 'Val46', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val47: Annotated[int, ("SunSpecPoint", {'name': 'Val47', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val48: Annotated[int, ("SunSpecPoint", {'name': 'Val48', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val49: Annotated[int, ("SunSpecPoint", {'name': 'Val49', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val50: Annotated[int, ("SunSpecPoint", {'name': 'Val50', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val51: Annotated[int, ("SunSpecPoint", {'name': 'Val51', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val52: Annotated[int, ("SunSpecPoint", {'name': 'Val52', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val53: Annotated[int, ("SunSpecPoint", {'name': 'Val53', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val54: Annotated[int, ("SunSpecPoint", {'name': 'Val54', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val55: Annotated[int, ("SunSpecPoint", {'name': 'Val55', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val56: Annotated[int, ("SunSpecPoint", {'name': 'Val56', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val57: Annotated[int, ("SunSpecPoint", {'name': 'Val57', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val58: Annotated[int, ("SunSpecPoint", {'name': 'Val58', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val59: Annotated[int, ("SunSpecPoint", {'name': 'Val59', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val60: Annotated[int, ("SunSpecPoint", {'name': 'Val60', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val61: Annotated[int, ("SunSpecPoint", {'name': 'Val61', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val62: Annotated[int, ("SunSpecPoint", {'name': 'Val62', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val63: Annotated[int, ("SunSpecPoint", {'name': 'Val63', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val64: Annotated[int, ("SunSpecPoint", {'name': 'Val64', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val65: Annotated[int, ("SunSpecPoint", {'name': 'Val65', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val66: Annotated[int, ("SunSpecPoint", {'name': 'Val66', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val67: Annotated[int, ("SunSpecPoint", {'name': 'Val67', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val68: Annotated[int, ("SunSpecPoint", {'name': 'Val68', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val69: Annotated[int, ("SunSpecPoint", {'name': 'Val69', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val70: Annotated[int, ("SunSpecPoint", {'name': 'Val70', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val71: Annotated[int, ("SunSpecPoint", {'name': 'Val71', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val72: Annotated[int, ("SunSpecPoint", {'name': 'Val72', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val73: Annotated[int, ("SunSpecPoint", {'name': 'Val73', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val74: Annotated[int, ("SunSpecPoint", {'name': 'Val74', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val75: Annotated[int, ("SunSpecPoint", {'name': 'Val75', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val76: Annotated[int, ("SunSpecPoint", {'name': 'Val76', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val77: Annotated[int, ("SunSpecPoint", {'name': 'Val77', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val78: Annotated[int, ("SunSpecPoint", {'name': 'Val78', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val79: Annotated[int, ("SunSpecPoint", {'name': 'Val79', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Val80: Annotated[int, ("SunSpecPoint", {'name': 'Val80', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Role: Annotated[int, ("SunSpecPoint", {'name': 'Role', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Rsrvd: Annotated[int, ("SunSpecPoint", {'name': 'Rsrvd', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    repeating: Annotated[Model6RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model6RepeatingGroup})]

