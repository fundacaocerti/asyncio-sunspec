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


class Model8RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        Cert (int): X.509 Certificate of the device
    """

    Cert: Annotated[int, ("SunSpecPoint", {'name': 'Cert', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model8Fmt(IntEnum):
    """
    X.509 format of the certificate. DER or PEM.

    Members:
        NONE (int): NONE
        X509_PEM (int): X509_PEM
        X509_DER (int): X509_DER
    """
    NONE = 0
    X509_PEM = 1
    X509_DER = 2



class Model8(SunSpecModel, model_name="model_8", id=8):
    """
    Security model for PKI

    Attributes:
        Fmt (Model8Fmt): X.509 format of the certificate. DER or PEM.
        N (int): Number of registers to follow for the certificate
    """

    Fmt: Annotated[int, ("SunSpecPoint", {'name': 'Fmt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    repeating: Annotated[Model8RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model8RepeatingGroup})]

