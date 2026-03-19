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


class Model64415LogEventEna(IntEnum):
    """
    Enable or disable the LogEvent mode

    Members:
        DISABLED (int): LogEvent Mode Disabled
        ENABLED (int): LogEvent Mode Enabled
    """
    DISABLED = 0
    ENABLED = 1



class Model64415HTTPMsg(IntEnum):
    """
    Enable or disable the HTTP Message mode

    Members:
        DISABLED (int): HTTP Message Mode Disabled
        ENABLED (int): HTTP Message Mode Enabled
    """
    DISABLED = 0
    ENABLED = 1



class Model64415COMM004Cert(IntEnum):
    """
    Select COMM-004 certificate type

    Members:
        Default_Certificate (int): Default Certificate
        COMM_004A (int): Chain Length Two Certificate
        COMM_004B (int): Chain Length Three Certificate
        COMM_004C (int): Chain Length Four Certificate
        COMM_004D (int): Invalid MICA Extended Key Critical Value
        COMM_004E (int): Invalid MICA Name Non-Critical Value
        COMM_004F (int): Invalid MICA Policy Mapping Non-Critical Value
        COMM_004G (int): Self-signed device certificate
    """
    Default_Certificate = 0
    COMM_004A = 1
    COMM_004B = 2
    COMM_004C = 3
    COMM_004D = 4
    COMM_004E = 5
    COMM_004F = 6
    COMM_004G = 7



class Model64415(SunSpecModel, model_name="CSIPControl", id=64415):
    """
    CSIP Client Control for Alarms and Error tests

    Attributes:
        LogEventEna (Model64415LogEventEna): Enable or disable the LogEvent mode
        HTTPMsg (Model64415HTTPMsg): Enable or disable the HTTP Message mode
        COMM004Cert (Model64415COMM004Cert): Select COMM-004 certificate type
    """

    LogEventEna: Annotated[int, ("SunSpecPoint", {'name': 'LogEventEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    HTTPMsg: Annotated[int, ("SunSpecPoint", {'name': 'HTTPMsg', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    COMM004Cert: Annotated[int, ("SunSpecPoint", {'name': 'COMM004Cert', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]

