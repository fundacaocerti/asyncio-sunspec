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


class Model131ReadOnly(IntEnum):
    """
    Enumerated value indicates if curve is read-only or can be modified.

    Members:
        READWRITE (int): READWRITE
        READONLY (int): READONLY
    """
    READWRITE = 0
    READONLY = 1



class Model131CurveGroup(SunSpecGroup):
    """
    Attributes:
        ActPt (int): Number of active points in array.
        W1 (int): Point 1 Watts.
        PF1 (int): Point 1 PF in EEI notation.
        W2 (int): Point 2 Watts.
        PF2 (int): Point 2 PF in EEI notation.
        W3 (int): Point 3 Watts.
        PF3 (int): Point 3 PF in EEI notation.
        W4 (int): Point 4 Watts.
        PF4 (int): Point 4 PF in EEI notation.
        W5 (int): Point 5 Watts.
        PF5 (int): Point 5 PF in EEI notation.
        W6 (int): Point 6 Watts.
        PF6 (int): Point 6 PF in EEI notation.
        W7 (int): Point 7 Watts.
        PF7 (int): Point 7 PF in EEI notation.
        W8 (int): Point 8 Watts.
        PF8 (int): Point 8 PF in EEI notation.
        W9 (int): Point 9 Watts.
        PF9 (int): Point 9 PF in EEI notation.
        W10 (int): Point 10 Watts.
        PF10 (int): Point 10 PF in EEI notation.
        W11 (int): Point 11 Watts.
        PF11 (int): Point 11 PF in EEI notation.
        W12 (int): Point 12 Watts.
        PF12 (int): Point 12 PF in EEI notation.
        W13 (int): Point 13 Watts.
        PF13 (int): Point 13 PF in EEI notation.
        W14 (int): Point 14 Watts.
        PF14 (int): Point 14 PF in EEI notation.
        W15 (int): Point 15 Watts.
        PF15 (int): Point 15 PF in EEI notation.
        W16 (int): Point 16 Watts.
        PF16 (int): Point 16 PF in EEI notation.
        W17 (int): Point 17 Watts.
        PF17 (int): Point 17 PF in EEI notation.
        W18 (int): Point 18 Watts.
        PF18 (int): Point 18 PF in EEI notation.
        W19 (int): Point 19 Watts.
        PF19 (int): Point 19 PF in EEI notation.
        W20 (int): Point 20 Watts.
        PF20 (int): Point 20 PF in EEI notation.
        CrvNam (str): Optional description for curve.
        RmpPT1Tms (int): The time of the PT1 in seconds (time to accomplish a change of 95%).
        RmpDecTmm (int): The maximum rate at which the power factor may be reduced in response to changes in the power value.
        RmpIncTmm (int): The maximum rate at which the power factor may be increased in response to changes in the power value.
        ReadOnly (Model131ReadOnly): Enumerated value indicates if curve is read-only or can be modified.
        Pad (int)
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    W1: Annotated[int, ("SunSpecPoint", {'name': 'W1', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF1: Annotated[int, ("SunSpecPoint", {'name': 'PF1', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W2: Annotated[int, ("SunSpecPoint", {'name': 'W2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF2: Annotated[int, ("SunSpecPoint", {'name': 'PF2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W3: Annotated[int, ("SunSpecPoint", {'name': 'W3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF3: Annotated[int, ("SunSpecPoint", {'name': 'PF3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W4: Annotated[int, ("SunSpecPoint", {'name': 'W4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF4: Annotated[int, ("SunSpecPoint", {'name': 'PF4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W5: Annotated[int, ("SunSpecPoint", {'name': 'W5', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF5: Annotated[int, ("SunSpecPoint", {'name': 'PF5', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W6: Annotated[int, ("SunSpecPoint", {'name': 'W6', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF6: Annotated[int, ("SunSpecPoint", {'name': 'PF6', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W7: Annotated[int, ("SunSpecPoint", {'name': 'W7', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF7: Annotated[int, ("SunSpecPoint", {'name': 'PF7', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W8: Annotated[int, ("SunSpecPoint", {'name': 'W8', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF8: Annotated[int, ("SunSpecPoint", {'name': 'PF8', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W9: Annotated[int, ("SunSpecPoint", {'name': 'W9', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF9: Annotated[int, ("SunSpecPoint", {'name': 'PF9', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W10: Annotated[int, ("SunSpecPoint", {'name': 'W10', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF10: Annotated[int, ("SunSpecPoint", {'name': 'PF10', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W11: Annotated[int, ("SunSpecPoint", {'name': 'W11', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF11: Annotated[int, ("SunSpecPoint", {'name': 'PF11', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W12: Annotated[int, ("SunSpecPoint", {'name': 'W12', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF12: Annotated[int, ("SunSpecPoint", {'name': 'PF12', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W13: Annotated[int, ("SunSpecPoint", {'name': 'W13', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF13: Annotated[int, ("SunSpecPoint", {'name': 'PF13', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W14: Annotated[int, ("SunSpecPoint", {'name': 'W14', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF14: Annotated[int, ("SunSpecPoint", {'name': 'PF14', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W15: Annotated[int, ("SunSpecPoint", {'name': 'W15', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF15: Annotated[int, ("SunSpecPoint", {'name': 'PF15', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W16: Annotated[int, ("SunSpecPoint", {'name': 'W16', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF16: Annotated[int, ("SunSpecPoint", {'name': 'PF16', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W17: Annotated[int, ("SunSpecPoint", {'name': 'W17', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF17: Annotated[int, ("SunSpecPoint", {'name': 'PF17', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W18: Annotated[int, ("SunSpecPoint", {'name': 'W18', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF18: Annotated[int, ("SunSpecPoint", {'name': 'PF18', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W19: Annotated[int, ("SunSpecPoint", {'name': 'W19', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF19: Annotated[int, ("SunSpecPoint", {'name': 'PF19', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    W20: Annotated[int, ("SunSpecPoint", {'name': 'W20', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    PF20: Annotated[int, ("SunSpecPoint", {'name': 'PF20', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    CrvNam: Annotated[str, ("SunSpecPoint", {'name': 'CrvNam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpPT1Tms: Annotated[int, ("SunSpecPoint", {'name': 'RmpPT1Tms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpDecTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpDecTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    RmpIncTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]


class Model131ModEna(IntFlag):
    """
    Is watt-PF mode active.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model131(SunSpecModel, model_name="watt_pf", id=131):
    """
    Watt-Power Factor 

    Attributes:
        ActCrv (int): Index of active curve. 0=no active curve.
        ModEna (Model131ModEna): Is watt-PF mode active.
        WinTms (int): Time window for watt-PF change.
        RvrtTms (int): Timeout period for watt-PF curve selection.
        RmpTms (int): Ramp time for moving from current mode to new mode.
        NCrv (int): Number of curves supported (recommend 4).
        NPt (int): Max number of points in array.
        W_SF (int): Scale factor for percent WMax.
        PF_SF (int): Scale factor for PF.
        RmpIncDec_SF (int): Scale factor for increment and decrement ramps.
    """

    ActCrv: Annotated[int, ("SunSpecPoint", {'name': 'ActCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NCrv: Annotated[int, ("SunSpecPoint", {'name': 'NCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    RmpIncDec_SF: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncDec_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    curve: Annotated[Model131CurveGroup, ("SunSpecGroup", {"name": "curve", "group_type": Model131CurveGroup})]

