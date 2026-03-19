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


class Model7RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        DS (int): Digital Signature
    """

    DS: Annotated[int, ("SunSpecPoint", {'name': 'DS', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]


class Model7Sts(IntEnum):
    """
    Status of last write operation

    Members:
        SUCCESS (int): SUCCESS
        DS (int): DS
        ACL (int): ACL
        OFF (int): OFF
        VAL (int): VAL
    """
    SUCCESS = 0
    DS = 1
    ACL = 2
    OFF = 3
    VAL = 4



class Model7Alm(IntEnum):
    """
    Bitmask alarm code

    Members:
        NONE (int): NONE
        ALM (int): ALM
    """
    NONE = 0
    ALM = 1



class Model7Alg(IntEnum):
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



class Model7(SunSpecModel, model_name="model_7", id=7):
    """
    Include a digital signature over the response

    Attributes:
        RqSeq (int): Sequence number from the request
        Sts (Model7Sts): Status of last write operation
        Ts (int): Timestamp value is the number of seconds since January 1, 2000
        Ms (int): Millisecond counter 0-999
        Seq (int): Sequence number of response
        Alm (Model7Alm): Bitmask alarm code
        Rsrvd (int)
        Alg (Model7Alg): Algorithm used to compute the digital signature
        N (int): Number of registers comprising the digital signature.
    """

    RqSeq: Annotated[int, ("SunSpecPoint", {'name': 'RqSeq', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Sts: Annotated[int, ("SunSpecPoint", {'name': 'Sts', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Ts: Annotated[int, ("SunSpecPoint", {'name': 'Ts', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Ms: Annotated[int, ("SunSpecPoint", {'name': 'Ms', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Seq: Annotated[int, ("SunSpecPoint", {'name': 'Seq', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Alm: Annotated[int, ("SunSpecPoint", {'name': 'Alm', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Rsrvd: Annotated[int, ("SunSpecPoint", {'name': 'Rsrvd', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Alg: Annotated[int, ("SunSpecPoint", {'name': 'Alg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    repeating: Annotated[Model7RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model7RepeatingGroup})]

