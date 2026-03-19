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


class Model141ReadOnly(IntEnum):
    """
    Enumerated value indicates if curve is read-only or can be modified.

    Members:
        READWRITE (int): READWRITE
        READONLY (int): READONLY
    """
    READWRITE = 0
    READONLY = 1



class Model141CurveGroup(SunSpecGroup):
    """
    Attributes:
        ActPt (int): Number of active points in array.
        Tms1 (int): Point 1 must remain connected duration.
        Hz1 (int): Point 1 must remain connected frequency.
        Tms2 (int): Point 2 must remain connected duration.
        Hz2 (int): Point 2 must remain connected frequency.
        Tms3 (int): Point 3 must remain connected duration.
        Hz3 (int): Point 3 must remain connected frequency.
        Tms4 (int): Point 4 must remain connected duration.
        Hz4 (int): Point 4 must remain connected frequency.
        Tms5 (int): Point 5 must remain connected duration.
        Hz5 (int): Point 5 must remain connected frequency.
        Tms6 (int): Point 6 must remain connected duration.
        Hz6 (int): Point 6 must remain connected frequency.
        Tms7 (int): Point 7 must remain connected duration.
        Hz7 (int): Point 7 must remain connected frequency.
        Tms8 (int): Point 8 must remain connected duration.
        Hz8 (int): Point 8 must remain connected frequency.
        Tms9 (int): Point 9 must remain connected duration.
        Hz9 (int): Point 9 must remain connected frequency.
        Tms10 (int): Point 10 must remain connected duration.
        Hz10 (int): Point 10 must remain connected frequency.
        Tms11 (int): Point 11 must remain connected duration.
        Hz11 (int): Point 11 must remain connected frequency.
        Tms12 (int): Point 12 must remain connected duration.
        Hz12 (int): Point 12 must remain connected frequency.
        Tms13 (int): Point 13 must remain connected duration.
        Hz13 (int): Point 13 must remain connected frequency.
        Tms14 (int): Point 14 must remain connected duration.
        Hz14 (int): Point 14 must remain connected frequency.
        Tms15 (int): Point 15 must remain connected duration.
        Hz15 (int): Point 15 must remain connected frequency.
        Tms16 (int): Point 16 must remain connected duration.
        Hz16 (int): Point 16 must remain connected frequency.
        Tms17 (int): Point 17 must remain connected duration.
        Hz17 (int): Point 17 must remain connected frequency.
        Tms18 (int): Point 18 must remain connected duration.
        Hz18 (int): Point 18 must remain connected frequency.
        Tms19 (int): Point 19 must remain connected duration.
        Hz19 (int): Point 19 must remain connected frequency.
        Tms20 (int): Point 20 must remain connected duration.
        Hz20 (int): Point 20 must remain connected frequency.
        CrvNam (str): Optional description for curve.
        ReadOnly (Model141ReadOnly): Enumerated value indicates if curve is read-only or can be modified.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Tms1: Annotated[int, ("SunSpecPoint", {'name': 'Tms1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz1: Annotated[int, ("SunSpecPoint", {'name': 'Hz1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms2: Annotated[int, ("SunSpecPoint", {'name': 'Tms2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz2: Annotated[int, ("SunSpecPoint", {'name': 'Hz2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms3: Annotated[int, ("SunSpecPoint", {'name': 'Tms3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz3: Annotated[int, ("SunSpecPoint", {'name': 'Hz3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms4: Annotated[int, ("SunSpecPoint", {'name': 'Tms4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz4: Annotated[int, ("SunSpecPoint", {'name': 'Hz4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms5: Annotated[int, ("SunSpecPoint", {'name': 'Tms5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz5: Annotated[int, ("SunSpecPoint", {'name': 'Hz5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms6: Annotated[int, ("SunSpecPoint", {'name': 'Tms6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz6: Annotated[int, ("SunSpecPoint", {'name': 'Hz6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms7: Annotated[int, ("SunSpecPoint", {'name': 'Tms7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz7: Annotated[int, ("SunSpecPoint", {'name': 'Hz7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms8: Annotated[int, ("SunSpecPoint", {'name': 'Tms8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz8: Annotated[int, ("SunSpecPoint", {'name': 'Hz8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms9: Annotated[int, ("SunSpecPoint", {'name': 'Tms9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz9: Annotated[int, ("SunSpecPoint", {'name': 'Hz9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms10: Annotated[int, ("SunSpecPoint", {'name': 'Tms10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz10: Annotated[int, ("SunSpecPoint", {'name': 'Hz10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms11: Annotated[int, ("SunSpecPoint", {'name': 'Tms11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz11: Annotated[int, ("SunSpecPoint", {'name': 'Hz11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms12: Annotated[int, ("SunSpecPoint", {'name': 'Tms12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz12: Annotated[int, ("SunSpecPoint", {'name': 'Hz12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms13: Annotated[int, ("SunSpecPoint", {'name': 'Tms13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz13: Annotated[int, ("SunSpecPoint", {'name': 'Hz13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms14: Annotated[int, ("SunSpecPoint", {'name': 'Tms14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz14: Annotated[int, ("SunSpecPoint", {'name': 'Hz14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms15: Annotated[int, ("SunSpecPoint", {'name': 'Tms15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz15: Annotated[int, ("SunSpecPoint", {'name': 'Hz15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms16: Annotated[int, ("SunSpecPoint", {'name': 'Tms16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz16: Annotated[int, ("SunSpecPoint", {'name': 'Hz16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms17: Annotated[int, ("SunSpecPoint", {'name': 'Tms17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz17: Annotated[int, ("SunSpecPoint", {'name': 'Hz17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms18: Annotated[int, ("SunSpecPoint", {'name': 'Tms18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz18: Annotated[int, ("SunSpecPoint", {'name': 'Hz18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms19: Annotated[int, ("SunSpecPoint", {'name': 'Tms19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz19: Annotated[int, ("SunSpecPoint", {'name': 'Hz19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms20: Annotated[int, ("SunSpecPoint", {'name': 'Tms20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    Hz20: Annotated[int, ("SunSpecPoint", {'name': 'Hz20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    CrvNam: Annotated[str, ("SunSpecPoint", {'name': 'CrvNam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model141ModEna(IntFlag):
    """
    LHzRT control mode. Enable active curve.  Bitfield value.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model141(SunSpecModel, model_name="lfrtc", id=141):
    """
    LFRT must remain connected

    Attributes:
        ActCrv (int): Index of active curve. 0=no active curve.
        ModEna (Model141ModEna): LHzRT control mode. Enable active curve.  Bitfield value.
        WinTms (int): Time window for LFRT change.
        RvrtTms (int): Timeout period for LFRT curve selection.
        RmpTms (int): Ramp time for moving from current mode to new mode.
        NCrv (int): Number of curves supported (recommend 4).
        NPt (int): Number of curve points supported (maximum of 20).
        Tms_SF (int): Scale factor for duration.
        Hz_SF (int): Scale factor for frequency.
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
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    curve: Annotated[Model141CurveGroup, ("SunSpecGroup", {"name": "curve", "group_type": Model141CurveGroup})]

