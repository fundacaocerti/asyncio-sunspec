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


class Model63001RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        sunssf_8 (int)
        int16_11 (int)
        int16_12 (int)
        int16_u (int)
        uint16_11 (int)
        uint16_12 (int)
        uint16_13 (int)
        uint16_u (int)
        int32 (int)
        int32_u (int)
        uint32 (int)
        uint32_u (int)
        sunssf_9 (int)
        pad_2 (int)
    """

    sunssf_8: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_8', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    int16_11: Annotated[int, ("SunSpecPoint", {'name': 'int16_11', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_8
    int16_12: Annotated[int, ("SunSpecPoint", {'name': 'int16_12', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: sunssf_9
    int16_u: Annotated[int, ("SunSpecPoint", {'name': 'int16_u', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    uint16_11: Annotated[int, ("SunSpecPoint", {'name': 'uint16_11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_8
    uint16_12: Annotated[int, ("SunSpecPoint", {'name': 'uint16_12', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: sunssf_9
    uint16_13: Annotated[int, ("SunSpecPoint", {'name': 'uint16_13', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    uint16_u: Annotated[int, ("SunSpecPoint", {'name': 'uint16_u', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    int32: Annotated[int, ("SunSpecPoint", {'name': 'int32', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_1
    int32_u: Annotated[int, ("SunSpecPoint", {'name': 'int32_u', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    uint32: Annotated[int, ("SunSpecPoint", {'name': 'uint32', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_9
    uint32_u: Annotated[int, ("SunSpecPoint", {'name': 'uint32_u', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    sunssf_9: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_9', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    pad_2: Annotated[int, ("SunSpecPoint", {'name': 'pad_2', 'ptype': 'uint16', 'mandatory': False, 'static': False})]


class Model63001(SunSpecModel, model_name="model_63001", id=63001):
    """
    Attributes:
        sunssf_1 (int)
        sunssf_2 (int)
        sunssf_3 (int)
        sunssf_4 (int)
        int16_1 (int)
        int16_2 (int)
        int16_3 (int)
        int16_4 (int)
        int16_5 (int)
        int16_u (int)
        uint16_1 (int)
        uint16_2 (int)
        uint16_3 (int)
        uint16_4 (int)
        uint16_5 (int)
        uint16_u (int)
        acc16 (int)
        acc16_u (int)
        enum16 (int)
        enum16_u (int)
        bitfield16 (int)
        bitfield16_u (int)
        int32_1 (int)
        int32_2 (int)
        int32_3 (int)
        int32_4 (int)
        int32_5 (int)
        int32_u (int)
        uint32_1 (int)
        uint32_2 (int)
        uint32_3 (int)
        uint32_4 (int)
        uint32_5 (int)
        uint32_u (int)
        acc32 (int)
        acc32_u (int)
        enum32 (int)
        enum32_u (int)
        bitfield32 (int)
        bitfield32_u (int)
        ipaddr (int)
        ipaddr_u (int)
        int64 (int)
        int64_u (int)
        acc64 (int)
        acc64_u (int)
        ipv6addr (str)
        ipv6addr_u (str)
        float32 (float)
        float32_u (float)
        string (str)
        string_u (str)
        sunssf_5 (int)
        sunssf_6 (int)
        sunssf_7 (int)
        pad_1 (int)
    """

    sunssf_1: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_1', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    sunssf_2: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_2', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    sunssf_3: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_3', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    sunssf_4: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_4', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    int16_1: Annotated[int, ("SunSpecPoint", {'name': 'int16_1', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: sunssf_1
    int16_2: Annotated[int, ("SunSpecPoint", {'name': 'int16_2', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: sunssf_2
    int16_3: Annotated[int, ("SunSpecPoint", {'name': 'int16_3', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: sunssf_3
    int16_4: Annotated[int, ("SunSpecPoint", {'name': 'int16_4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_4
    int16_5: Annotated[int, ("SunSpecPoint", {'name': 'int16_5', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    int16_u: Annotated[int, ("SunSpecPoint", {'name': 'int16_u', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    uint16_1: Annotated[int, ("SunSpecPoint", {'name': 'uint16_1', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: sunssf_1
    uint16_2: Annotated[int, ("SunSpecPoint", {'name': 'uint16_2', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: sunssf_2
    uint16_3: Annotated[int, ("SunSpecPoint", {'name': 'uint16_3', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: sunssf_3
    uint16_4: Annotated[int, ("SunSpecPoint", {'name': 'uint16_4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_4
    uint16_5: Annotated[int, ("SunSpecPoint", {'name': 'uint16_5', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    uint16_u: Annotated[int, ("SunSpecPoint", {'name': 'uint16_u', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    acc16: Annotated[int, ("SunSpecPoint", {'name': 'acc16', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    acc16_u: Annotated[int, ("SunSpecPoint", {'name': 'acc16_u', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    enum16: Annotated[int, ("SunSpecPoint", {'name': 'enum16', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    enum16_u: Annotated[int, ("SunSpecPoint", {'name': 'enum16_u', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    bitfield16: Annotated[int, ("SunSpecPoint", {'name': 'bitfield16', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    bitfield16_u: Annotated[int, ("SunSpecPoint", {'name': 'bitfield16_u', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    int32_1: Annotated[int, ("SunSpecPoint", {'name': 'int32_1', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: sunssf_5
    int32_2: Annotated[int, ("SunSpecPoint", {'name': 'int32_2', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: sunssf_6
    int32_3: Annotated[int, ("SunSpecPoint", {'name': 'int32_3', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_7
    int32_4: Annotated[int, ("SunSpecPoint", {'name': 'int32_4', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    int32_5: Annotated[int, ("SunSpecPoint", {'name': 'int32_5', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    int32_u: Annotated[int, ("SunSpecPoint", {'name': 'int32_u', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    uint32_1: Annotated[int, ("SunSpecPoint", {'name': 'uint32_1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: sunssf_5
    uint32_2: Annotated[int, ("SunSpecPoint", {'name': 'uint32_2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: sunssf_6
    uint32_3: Annotated[int, ("SunSpecPoint", {'name': 'uint32_3', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: sunssf_7
    uint32_4: Annotated[int, ("SunSpecPoint", {'name': 'uint32_4', 'ptype': 'uint32', 'mandatory': False, 'static': False})]  # sf: 1
    uint32_5: Annotated[int, ("SunSpecPoint", {'name': 'uint32_5', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    uint32_u: Annotated[int, ("SunSpecPoint", {'name': 'uint32_u', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    acc32: Annotated[int, ("SunSpecPoint", {'name': 'acc32', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    acc32_u: Annotated[int, ("SunSpecPoint", {'name': 'acc32_u', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    enum32: Annotated[int, ("SunSpecPoint", {'name': 'enum32', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    enum32_u: Annotated[int, ("SunSpecPoint", {'name': 'enum32_u', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    bitfield32: Annotated[int, ("SunSpecPoint", {'name': 'bitfield32', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    bitfield32_u: Annotated[int, ("SunSpecPoint", {'name': 'bitfield32_u', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    ipaddr: Annotated[int, ("SunSpecPoint", {'name': 'ipaddr', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ipaddr_u: Annotated[int, ("SunSpecPoint", {'name': 'ipaddr_u', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    int64: Annotated[int, ("SunSpecPoint", {'name': 'int64', 'ptype': 'int64', 'mandatory': False, 'static': False, 'access': 'RW'})]
    int64_u: Annotated[int, ("SunSpecPoint", {'name': 'int64_u', 'ptype': 'int64', 'mandatory': False, 'static': False})]
    acc64: Annotated[int, ("SunSpecPoint", {'name': 'acc64', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    acc64_u: Annotated[int, ("SunSpecPoint", {'name': 'acc64_u', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    ipv6addr: Annotated[str, ("SunSpecPoint", {'name': 'ipv6addr', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False})]
    ipv6addr_u: Annotated[str, ("SunSpecPoint", {'name': 'ipv6addr_u', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False})]
    float32: Annotated[float, ("SunSpecPoint", {'name': 'float32', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    float32_u: Annotated[float, ("SunSpecPoint", {'name': 'float32_u', 'ptype': 'float32', 'mandatory': False, 'static': False})]
    string: Annotated[str, ("SunSpecPoint", {'name': 'string', 'ptype': 'string', 'size': 16, 'mandatory': False, 'static': False, 'access': 'RW'})]
    string_u: Annotated[str, ("SunSpecPoint", {'name': 'string_u', 'ptype': 'string', 'size': 16, 'mandatory': False, 'static': False})]
    sunssf_5: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_5', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    sunssf_6: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_6', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    sunssf_7: Annotated[int, ("SunSpecPoint", {'name': 'sunssf_7', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    pad_1: Annotated[int, ("SunSpecPoint", {'name': 'pad_1', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    repeating: Annotated[Model63001RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model63001RepeatingGroup})]

