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


class Model64001(SunSpecModel, model_name="model_64001", id=64001):
    """
    Attributes:
        Cmd (int)
        HWRev (int)
        RSFWRev (int)
        OSFWRev (int)
        ProdRev (str)
        Boots (int)
        Switch (int)
        Sensors (int)
        Talking (int)
        Status (int)
        Config (int)
        LEDblink (int)
        LEDon (int)
        Reserved (int)
        Loc (str)
        S1ID (int)
        S1Addr (int)
        S1OSVer (int)
        S1Ver (str)
        S1Serial (str)
        S2ID (int)
        S2Addr (int)
        S2OSVer (int)
        S2Ver (str)
        S2Serial (str)
        S3ID (int)
        S3Addr (int)
        S3OSVer (int)
        S3Ver (str)
        S3Serial (str)
        S4ID (int)
        S4Addr (int)
        S4OSVer (int)
        S4Ver (str)
        S4Serial (str)
    """

    Cmd: Annotated[int, ("SunSpecPoint", {'name': 'Cmd', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    HWRev: Annotated[int, ("SunSpecPoint", {'name': 'HWRev', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    RSFWRev: Annotated[int, ("SunSpecPoint", {'name': 'RSFWRev', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    OSFWRev: Annotated[int, ("SunSpecPoint", {'name': 'OSFWRev', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ProdRev: Annotated[str, ("SunSpecPoint", {'name': 'ProdRev', 'ptype': 'string', 'size': 2, 'mandatory': False, 'static': False})]
    Boots: Annotated[int, ("SunSpecPoint", {'name': 'Boots', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Switch: Annotated[int, ("SunSpecPoint", {'name': 'Switch', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Sensors: Annotated[int, ("SunSpecPoint", {'name': 'Sensors', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Talking: Annotated[int, ("SunSpecPoint", {'name': 'Talking', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Status: Annotated[int, ("SunSpecPoint", {'name': 'Status', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Config: Annotated[int, ("SunSpecPoint", {'name': 'Config', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    LEDblink: Annotated[int, ("SunSpecPoint", {'name': 'LEDblink', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    LEDon: Annotated[int, ("SunSpecPoint", {'name': 'LEDon', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Reserved: Annotated[int, ("SunSpecPoint", {'name': 'Reserved', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Loc: Annotated[str, ("SunSpecPoint", {'name': 'Loc', 'ptype': 'string', 'size': 16, 'mandatory': False, 'static': False})]
    S1ID: Annotated[int, ("SunSpecPoint", {'name': 'S1ID', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S1Addr: Annotated[int, ("SunSpecPoint", {'name': 'S1Addr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S1OSVer: Annotated[int, ("SunSpecPoint", {'name': 'S1OSVer', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S1Ver: Annotated[str, ("SunSpecPoint", {'name': 'S1Ver', 'ptype': 'string', 'size': 2, 'mandatory': False, 'static': False})]
    S1Serial: Annotated[str, ("SunSpecPoint", {'name': 'S1Serial', 'ptype': 'string', 'size': 5, 'mandatory': False, 'static': False})]
    S2ID: Annotated[int, ("SunSpecPoint", {'name': 'S2ID', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S2Addr: Annotated[int, ("SunSpecPoint", {'name': 'S2Addr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S2OSVer: Annotated[int, ("SunSpecPoint", {'name': 'S2OSVer', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S2Ver: Annotated[str, ("SunSpecPoint", {'name': 'S2Ver', 'ptype': 'string', 'size': 2, 'mandatory': False, 'static': False})]
    S2Serial: Annotated[str, ("SunSpecPoint", {'name': 'S2Serial', 'ptype': 'string', 'size': 5, 'mandatory': False, 'static': False})]
    S3ID: Annotated[int, ("SunSpecPoint", {'name': 'S3ID', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S3Addr: Annotated[int, ("SunSpecPoint", {'name': 'S3Addr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S3OSVer: Annotated[int, ("SunSpecPoint", {'name': 'S3OSVer', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S3Ver: Annotated[str, ("SunSpecPoint", {'name': 'S3Ver', 'ptype': 'string', 'size': 2, 'mandatory': False, 'static': False})]
    S3Serial: Annotated[str, ("SunSpecPoint", {'name': 'S3Serial', 'ptype': 'string', 'size': 5, 'mandatory': False, 'static': False})]
    S4ID: Annotated[int, ("SunSpecPoint", {'name': 'S4ID', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S4Addr: Annotated[int, ("SunSpecPoint", {'name': 'S4Addr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S4OSVer: Annotated[int, ("SunSpecPoint", {'name': 'S4OSVer', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    S4Ver: Annotated[str, ("SunSpecPoint", {'name': 'S4Ver', 'ptype': 'string', 'size': 2, 'mandatory': False, 'static': False})]
    S4Serial: Annotated[str, ("SunSpecPoint", {'name': 'S4Serial', 'ptype': 'string', 'size': 5, 'mandatory': False, 'static': False})]

