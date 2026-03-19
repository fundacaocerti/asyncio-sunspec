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
from enum import IntEnum, IntFlag


class Model138ReadOnly(IntEnum):
    """
    Enumerated value indicates if curve is read-only or can be modified.

    Members:
        READWRITE (int): READWRITE
        READONLY (int): READONLY
    """
    READWRITE = 0
    READONLY = 1



class Model138CurveGroup(SunSpecGroup):
    """
    Attributes:
        ActPt (int): Number of active points in array.
        Tms1 (int): Point 1 must remain connected duration.
        V1 (int): Point 1 must remain connected voltage.
        Tms2 (int): Point 2 must remain connected duration.
        V2 (int): Point 2 must remain connected voltage.
        Tms3 (int): Point 3 must remain connected duration.
        V3 (int): Point 3 must remain connected voltage.
        Tms4 (int): Point 4 must remain connected duration.
        V4 (int): Point 4 must remain connected voltage.
        Tms5 (int): Point 5 must remain connected duration.
        V5 (int): Point 5 must remain connected voltage.
        Tms6 (int): Point 6 must remain connected duration.
        V6 (int): Point 6 must remain connected voltage.
        Tms7 (int): Point 7 must remain connected duration.
        V7 (int): Point 7 must remain connected voltage.
        Tms8 (int): Point 8 must remain connected duration.
        V8 (int): Point 8 must remain connected voltage.
        Tms9 (int): Point 9 must remain connected duration.
        V9 (int): Point 9 must remain connected voltage.
        Tms10 (int): Point 10 must remain connected duration.
        V10 (int): Point 10 must remain connected voltage.
        Tms11 (int): Point 11 must remain connected duration.
        V11 (int): Point 11 must remain connected voltage.
        Tms12 (int): Point 12 must remain connected duration.
        V12 (int): Point 12 must remain connected voltage.
        Tms13 (int): Point 13 must remain connected duration.
        V13 (int): Point 13 must remain connected voltage.
        Tms14 (int): Point 14 must remain connected duration.
        V14 (int): Point 14 must remain connected voltage.
        Tms15 (int): Point 15 must remain connected duration.
        V15 (int): Point 15 must remain connected voltage.
        Tms16 (int): Point 16 must remain connected duration.
        V16 (int): Point 16 must remain connected voltage.
        Tms17 (int): Point 17 must remain connected duration.
        V17 (int): Point 17 must remain connected voltage.
        Tms18 (int): Point 18 must remain connected duration.
        V18 (int): Point 18 must remain connected voltage.
        Tms19 (int): Point 19 must remain connected duration.
        V19 (int): Point 19 must remain connected voltage.
        Tms20 (int): Point 20 must remain connected duration.
        V20 (int): Point 20 must remain connected voltage.
        CrvNam (str): Optional description for curve.
        ReadOnly (Model138ReadOnly): Enumerated value indicates if curve is read-only or can be modified.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Tms1: Annotated[int, ("SunSpecPoint", {'name': 'Tms1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V1: Annotated[int, ("SunSpecPoint", {'name': 'V1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms2: Annotated[int, ("SunSpecPoint", {'name': 'Tms2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V2: Annotated[int, ("SunSpecPoint", {'name': 'V2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms3: Annotated[int, ("SunSpecPoint", {'name': 'Tms3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V3: Annotated[int, ("SunSpecPoint", {'name': 'V3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms4: Annotated[int, ("SunSpecPoint", {'name': 'Tms4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V4: Annotated[int, ("SunSpecPoint", {'name': 'V4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms5: Annotated[int, ("SunSpecPoint", {'name': 'Tms5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V5: Annotated[int, ("SunSpecPoint", {'name': 'V5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms6: Annotated[int, ("SunSpecPoint", {'name': 'Tms6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V6: Annotated[int, ("SunSpecPoint", {'name': 'V6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms7: Annotated[int, ("SunSpecPoint", {'name': 'Tms7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V7: Annotated[int, ("SunSpecPoint", {'name': 'V7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms8: Annotated[int, ("SunSpecPoint", {'name': 'Tms8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V8: Annotated[int, ("SunSpecPoint", {'name': 'V8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms9: Annotated[int, ("SunSpecPoint", {'name': 'Tms9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V9: Annotated[int, ("SunSpecPoint", {'name': 'V9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms10: Annotated[int, ("SunSpecPoint", {'name': 'Tms10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V10: Annotated[int, ("SunSpecPoint", {'name': 'V10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms11: Annotated[int, ("SunSpecPoint", {'name': 'Tms11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V11: Annotated[int, ("SunSpecPoint", {'name': 'V11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms12: Annotated[int, ("SunSpecPoint", {'name': 'Tms12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V12: Annotated[int, ("SunSpecPoint", {'name': 'V12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms13: Annotated[int, ("SunSpecPoint", {'name': 'Tms13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V13: Annotated[int, ("SunSpecPoint", {'name': 'V13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms14: Annotated[int, ("SunSpecPoint", {'name': 'Tms14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V14: Annotated[int, ("SunSpecPoint", {'name': 'V14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms15: Annotated[int, ("SunSpecPoint", {'name': 'Tms15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V15: Annotated[int, ("SunSpecPoint", {'name': 'V15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms16: Annotated[int, ("SunSpecPoint", {'name': 'Tms16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V16: Annotated[int, ("SunSpecPoint", {'name': 'V16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms17: Annotated[int, ("SunSpecPoint", {'name': 'Tms17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V17: Annotated[int, ("SunSpecPoint", {'name': 'V17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms18: Annotated[int, ("SunSpecPoint", {'name': 'Tms18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V18: Annotated[int, ("SunSpecPoint", {'name': 'V18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms19: Annotated[int, ("SunSpecPoint", {'name': 'Tms19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V19: Annotated[int, ("SunSpecPoint", {'name': 'V19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Tms20: Annotated[int, ("SunSpecPoint", {'name': 'Tms20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V20: Annotated[int, ("SunSpecPoint", {'name': 'V20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    CrvNam: Annotated[str, ("SunSpecPoint", {'name': 'CrvNam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model138ModEna(IntFlag):
    """
    HVRT control mode. Enable active curve.  Bitfield value.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model138(SunSpecModel, model_name="hvrtc", id=138):
    """
    HVRT must remain connected

    Attributes:
        ActCrv (int): Index of active curve. 0=no active curve.
        ModEna (Model138ModEna): HVRT control mode. Enable active curve.  Bitfield value.
        WinTms (int): Time window for HVRT change.
        RvrtTms (int): Timeout period for HVRT curve selection.
        RmpTms (int): Ramp time for moving from current mode to new mode.
        NCrv (int): Number of curves supported (recommend 4).
        NPt (int): Number of curve points supported (maximum of 20).
        Tms_SF (int): Scale factor for duration.
        V_SF (int): Scale factor for percent VRef.
        Pad (int)
    """

    ActCrv: Annotated[int, ("SunSpecPoint", {'name': 'ActCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NCrv: Annotated[int, ("SunSpecPoint", {'name': 'NCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Tms_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tms_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    curve: Annotated[Model138CurveGroup, ("SunSpecGroup", {"name": "curve", "group_type": Model138CurveGroup})]

