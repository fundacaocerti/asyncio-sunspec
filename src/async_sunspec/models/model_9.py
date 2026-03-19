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


class Model9RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        Cert (int)
    """

    Cert: Annotated[int, ("SunSpecPoint", {'name': 'Cert', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]


class Model9Fmt(IntEnum):
    """
    Format of this certificate

    Members:
        NONE (int): NONE
        X509_PEM (int): X509_PEM
        X509_DER (int): X509_DER
    """
    NONE = 0
    X509_PEM = 1
    X509_DER = 2



class Model9Typ(IntEnum):
    """
    Type of this certificate

    Members:
        DEV_KEY_PAIR (int): DEV_KEY_PAIR
        DEV_SHARED_KEY (int): DEV_SHARED_KEY
        OPERATOR_PUB (int): OPERATOR_PUB
        OPERATOR_SHARED (int): OPERATOR_SHARED
        CA_PUB (int): CA_PUB
    """
    DEV_KEY_PAIR = 0
    DEV_SHARED_KEY = 1
    OPERATOR_PUB = 2
    OPERATOR_SHARED = 3
    CA_PUB = 4



class Model9Alg(IntEnum):
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



class Model9(SunSpecModel, model_name="model_9", id=9):
    """
    Security model for PKI

    Attributes:
        CertUID (int): User ID for this certificate
        CertRole (int): Role for this certificate
        Fmt (Model9Fmt): Format of this certificate
        Typ (Model9Typ): Type of this certificate
        TotLn (int): Total Length of the Certificate
        FrgLn (int): Length of this fragment
        Frg1 (int): First word of this fragment
        Frg2 (int)
        Frg3 (int)
        Frg4 (int)
        Frg5 (int)
        Frg6 (int)
        Frg7 (int)
        Frg8 (int)
        Frg9 (int)
        Frg10 (int)
        Frg11 (int)
        Frg12 (int)
        Frg13 (int)
        Frg14 (int)
        Frg15 (int)
        Frg16 (int)
        Frg17 (int)
        Frg18 (int)
        Frg19 (int)
        Frg20 (int)
        Frg21 (int)
        Frg22 (int)
        Frg23 (int)
        Frg24 (int)
        Frg25 (int)
        Frg26 (int)
        Frg27 (int)
        Frg28 (int)
        Frg29 (int)
        Frg30 (int)
        Frg31 (int)
        Frg32 (int)
        Frg33 (int)
        Frg34 (int)
        Frg35 (int)
        Frg36 (int)
        Frg37 (int)
        Frg38 (int)
        Frg39 (int)
        Frg40 (int)
        Frg41 (int)
        Frg42 (int)
        Frg43 (int)
        Frg44 (int)
        Frg45 (int)
        Frg46 (int)
        Frg47 (int)
        Frg48 (int)
        Frg49 (int)
        Frg50 (int)
        Frg51 (int)
        Frg52 (int)
        Frg53 (int)
        Frg54 (int)
        Frg55 (int)
        Frg56 (int)
        Frg57 (int)
        Frg58 (int)
        Frg59 (int)
        Frg60 (int)
        Frg61 (int)
        Frg62 (int)
        Frg63 (int)
        Frg64 (int)
        Frg65 (int)
        Frg66 (int)
        Frg67 (int)
        Frg68 (int)
        Frg69 (int)
        Frg70 (int)
        Frg71 (int)
        Frg72 (int)
        Frg73 (int)
        Frg74 (int)
        Frg75 (int)
        Frg78 (int)
        Frg79 (int)
        Frg80 (int): Last word of this fragment
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of request
        UID (int): User ID for the request signature
        Role (int): Signing key used 0-5
        Alg (Model9Alg): Algorithm used to compute the digital signature
        N (int): Number of registers to follow for the certificate
    """

    CertUID: Annotated[int, ("SunSpecPoint", {'name': 'CertUID', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    CertRole: Annotated[int, ("SunSpecPoint", {'name': 'CertRole', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Fmt: Annotated[int, ("SunSpecPoint", {'name': 'Fmt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Typ: Annotated[int, ("SunSpecPoint", {'name': 'Typ', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    TotLn: Annotated[int, ("SunSpecPoint", {'name': 'TotLn', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    FrgLn: Annotated[int, ("SunSpecPoint", {'name': 'FrgLn', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg1: Annotated[int, ("SunSpecPoint", {'name': 'Frg1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg2: Annotated[int, ("SunSpecPoint", {'name': 'Frg2', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg3: Annotated[int, ("SunSpecPoint", {'name': 'Frg3', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg4: Annotated[int, ("SunSpecPoint", {'name': 'Frg4', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg5: Annotated[int, ("SunSpecPoint", {'name': 'Frg5', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg6: Annotated[int, ("SunSpecPoint", {'name': 'Frg6', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg7: Annotated[int, ("SunSpecPoint", {'name': 'Frg7', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg8: Annotated[int, ("SunSpecPoint", {'name': 'Frg8', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg9: Annotated[int, ("SunSpecPoint", {'name': 'Frg9', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg10: Annotated[int, ("SunSpecPoint", {'name': 'Frg10', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg11: Annotated[int, ("SunSpecPoint", {'name': 'Frg11', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg12: Annotated[int, ("SunSpecPoint", {'name': 'Frg12', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg13: Annotated[int, ("SunSpecPoint", {'name': 'Frg13', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg14: Annotated[int, ("SunSpecPoint", {'name': 'Frg14', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg15: Annotated[int, ("SunSpecPoint", {'name': 'Frg15', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg16: Annotated[int, ("SunSpecPoint", {'name': 'Frg16', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg17: Annotated[int, ("SunSpecPoint", {'name': 'Frg17', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg18: Annotated[int, ("SunSpecPoint", {'name': 'Frg18', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg19: Annotated[int, ("SunSpecPoint", {'name': 'Frg19', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg20: Annotated[int, ("SunSpecPoint", {'name': 'Frg20', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg21: Annotated[int, ("SunSpecPoint", {'name': 'Frg21', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg22: Annotated[int, ("SunSpecPoint", {'name': 'Frg22', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg23: Annotated[int, ("SunSpecPoint", {'name': 'Frg23', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg24: Annotated[int, ("SunSpecPoint", {'name': 'Frg24', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg25: Annotated[int, ("SunSpecPoint", {'name': 'Frg25', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg26: Annotated[int, ("SunSpecPoint", {'name': 'Frg26', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg27: Annotated[int, ("SunSpecPoint", {'name': 'Frg27', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg28: Annotated[int, ("SunSpecPoint", {'name': 'Frg28', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg29: Annotated[int, ("SunSpecPoint", {'name': 'Frg29', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg30: Annotated[int, ("SunSpecPoint", {'name': 'Frg30', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg31: Annotated[int, ("SunSpecPoint", {'name': 'Frg31', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg32: Annotated[int, ("SunSpecPoint", {'name': 'Frg32', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg33: Annotated[int, ("SunSpecPoint", {'name': 'Frg33', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg34: Annotated[int, ("SunSpecPoint", {'name': 'Frg34', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg35: Annotated[int, ("SunSpecPoint", {'name': 'Frg35', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg36: Annotated[int, ("SunSpecPoint", {'name': 'Frg36', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg37: Annotated[int, ("SunSpecPoint", {'name': 'Frg37', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg38: Annotated[int, ("SunSpecPoint", {'name': 'Frg38', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg39: Annotated[int, ("SunSpecPoint", {'name': 'Frg39', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg40: Annotated[int, ("SunSpecPoint", {'name': 'Frg40', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg41: Annotated[int, ("SunSpecPoint", {'name': 'Frg41', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg42: Annotated[int, ("SunSpecPoint", {'name': 'Frg42', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg43: Annotated[int, ("SunSpecPoint", {'name': 'Frg43', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg44: Annotated[int, ("SunSpecPoint", {'name': 'Frg44', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg45: Annotated[int, ("SunSpecPoint", {'name': 'Frg45', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg46: Annotated[int, ("SunSpecPoint", {'name': 'Frg46', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg47: Annotated[int, ("SunSpecPoint", {'name': 'Frg47', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg48: Annotated[int, ("SunSpecPoint", {'name': 'Frg48', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg49: Annotated[int, ("SunSpecPoint", {'name': 'Frg49', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg50: Annotated[int, ("SunSpecPoint", {'name': 'Frg50', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg51: Annotated[int, ("SunSpecPoint", {'name': 'Frg51', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg52: Annotated[int, ("SunSpecPoint", {'name': 'Frg52', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg53: Annotated[int, ("SunSpecPoint", {'name': 'Frg53', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg54: Annotated[int, ("SunSpecPoint", {'name': 'Frg54', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg55: Annotated[int, ("SunSpecPoint", {'name': 'Frg55', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg56: Annotated[int, ("SunSpecPoint", {'name': 'Frg56', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg57: Annotated[int, ("SunSpecPoint", {'name': 'Frg57', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg58: Annotated[int, ("SunSpecPoint", {'name': 'Frg58', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg59: Annotated[int, ("SunSpecPoint", {'name': 'Frg59', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg60: Annotated[int, ("SunSpecPoint", {'name': 'Frg60', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg61: Annotated[int, ("SunSpecPoint", {'name': 'Frg61', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg62: Annotated[int, ("SunSpecPoint", {'name': 'Frg62', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg63: Annotated[int, ("SunSpecPoint", {'name': 'Frg63', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg64: Annotated[int, ("SunSpecPoint", {'name': 'Frg64', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg65: Annotated[int, ("SunSpecPoint", {'name': 'Frg65', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg66: Annotated[int, ("SunSpecPoint", {'name': 'Frg66', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg67: Annotated[int, ("SunSpecPoint", {'name': 'Frg67', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg68: Annotated[int, ("SunSpecPoint", {'name': 'Frg68', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg69: Annotated[int, ("SunSpecPoint", {'name': 'Frg69', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg70: Annotated[int, ("SunSpecPoint", {'name': 'Frg70', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg71: Annotated[int, ("SunSpecPoint", {'name': 'Frg71', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg72: Annotated[int, ("SunSpecPoint", {'name': 'Frg72', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg73: Annotated[int, ("SunSpecPoint", {'name': 'Frg73', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg74: Annotated[int, ("SunSpecPoint", {'name': 'Frg74', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg75: Annotated[int, ("SunSpecPoint", {'name': 'Frg75', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg78: Annotated[int, ("SunSpecPoint", {'name': 'Frg78', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg79: Annotated[int, ("SunSpecPoint", {'name': 'Frg79', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Frg80: Annotated[int, ("SunSpecPoint", {'name': 'Frg80', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    UID: Annotated[int, ("SunSpecPoint", {'name': 'UID', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Role: Annotated[int, ("SunSpecPoint", {'name': 'Role', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    repeating: Annotated[Model9RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model9RepeatingGroup})]

