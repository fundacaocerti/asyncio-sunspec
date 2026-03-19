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


class Model134ReadOnly(IntEnum):
    """
    Enumerated value indicates if curve is read-only or can be modified.

    Members:
        READWRITE (int): READWRITE
        READONLY (int): READONLY
    """
    READWRITE = 0
    READONLY = 1



class Model134CurveGroup(SunSpecGroup):
    """
    Attributes:
        ActPt (int): Number of active points in array.
        Hz1 (int): Point 1 Hertz.
        W1 (int): Point 1 Watts.
        Hz2 (int): Point 2 Hertz.
        W2 (int): Point 2 Watts.
        Hz3 (int): Point 3 Hertz.
        W3 (int): Point 3 Watts.
        Hz4 (int): Point 4 Hertz.
        W4 (int): Point 4 Watts.
        Hz5 (int): Point 5 Hertz.
        W5 (int): Point 5 Watts.
        Hz6 (int): Point 6 Hertz.
        W6 (int): Point 6 Watts.
        Hz7 (int): Point 7 Hertz.
        W7 (int): Point 7 Watts.
        Hz8 (int): Point 8 Hertz.
        W8 (int): Point 8 Watts.
        Hz9 (int): Point 9 Hertz.
        W9 (int): Point 9 Watts.
        Hz10 (int): Point 10 Hertz.
        W10 (int): Point 10 Watts.
        Hz11 (int): Point 11 Hertz.
        W11 (int): Point 11 Watts.
        Hz12 (int): Point 12 Hertz.
        W12 (int): Point 12 Watts.
        Hz13 (int): Point 13 Hertz.
        W13 (int): Point 13 Watts.
        Hz14 (int): Point 14 Hertz.
        W14 (int): Point 14 Watts.
        Hz15 (int): Point 15 Hertz.
        W15 (int): Point 15 Watts.
        Hz16 (int): Point 16 Hertz.
        W16 (int): Point 16 Watts.
        Hz17 (int): Point 17 Hertz.
        W17 (int): Point 17 Watts.
        Hz18 (int): Point 18 Hertz.
        W18 (int): Point 18 Watts.
        Hz19 (int): Point 19 Hertz.
        W19 (int): Point 19 Watts.
        Hz20 (int): Point 20 Hertz.
        W20 (int): Point 20 Watts.
        CrvNam (str): Optional description for curve. (Max 16 chars)
        RmpPT1Tms (int): The time of the PT1 in seconds (time to accomplish a change of 95%).
        RmpDecTmm (int): The maximum rate at which the power value may be reduced in response to changes in the frequency value.
        RmpIncTmm (int): The maximum rate at which the power value may be increased in response to changes in the frequency value.
        RmpRsUp (int): The maximum rate at which the power may be increased after releasing the frozen value of snap shot function. 
        SnptW (int): 1=enable snapshot/capture mode
        WRef (int): Reference active power (default = WMax).
        WRefStrHz (int): Frequency deviation from nominal frequency at the time of the snapshot to start constraining power output.
        WRefStopHz (int): Frequency deviation from nominal frequency at which to release the power output.
        ReadOnly (Model134ReadOnly): Enumerated value indicates if curve is read-only or can be modified.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Hz1: Annotated[int, ("SunSpecPoint", {'name': 'Hz1', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W1: Annotated[int, ("SunSpecPoint", {'name': 'W1', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz2: Annotated[int, ("SunSpecPoint", {'name': 'Hz2', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W2: Annotated[int, ("SunSpecPoint", {'name': 'W2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz3: Annotated[int, ("SunSpecPoint", {'name': 'Hz3', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W3: Annotated[int, ("SunSpecPoint", {'name': 'W3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz4: Annotated[int, ("SunSpecPoint", {'name': 'Hz4', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W4: Annotated[int, ("SunSpecPoint", {'name': 'W4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz5: Annotated[int, ("SunSpecPoint", {'name': 'Hz5', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W5: Annotated[int, ("SunSpecPoint", {'name': 'W5', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz6: Annotated[int, ("SunSpecPoint", {'name': 'Hz6', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W6: Annotated[int, ("SunSpecPoint", {'name': 'W6', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz7: Annotated[int, ("SunSpecPoint", {'name': 'Hz7', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W7: Annotated[int, ("SunSpecPoint", {'name': 'W7', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz8: Annotated[int, ("SunSpecPoint", {'name': 'Hz8', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W8: Annotated[int, ("SunSpecPoint", {'name': 'W8', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz9: Annotated[int, ("SunSpecPoint", {'name': 'Hz9', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W9: Annotated[int, ("SunSpecPoint", {'name': 'W9', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz10: Annotated[int, ("SunSpecPoint", {'name': 'Hz10', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W10: Annotated[int, ("SunSpecPoint", {'name': 'W10', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz11: Annotated[int, ("SunSpecPoint", {'name': 'Hz11', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W11: Annotated[int, ("SunSpecPoint", {'name': 'W11', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz12: Annotated[int, ("SunSpecPoint", {'name': 'Hz12', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W12: Annotated[int, ("SunSpecPoint", {'name': 'W12', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz13: Annotated[int, ("SunSpecPoint", {'name': 'Hz13', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W13: Annotated[int, ("SunSpecPoint", {'name': 'W13', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz14: Annotated[int, ("SunSpecPoint", {'name': 'Hz14', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W14: Annotated[int, ("SunSpecPoint", {'name': 'W14', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz15: Annotated[int, ("SunSpecPoint", {'name': 'Hz15', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W15: Annotated[int, ("SunSpecPoint", {'name': 'W15', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz16: Annotated[int, ("SunSpecPoint", {'name': 'Hz16', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W16: Annotated[int, ("SunSpecPoint", {'name': 'W16', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz17: Annotated[int, ("SunSpecPoint", {'name': 'Hz17', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W17: Annotated[int, ("SunSpecPoint", {'name': 'W17', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz18: Annotated[int, ("SunSpecPoint", {'name': 'Hz18', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W18: Annotated[int, ("SunSpecPoint", {'name': 'W18', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz19: Annotated[int, ("SunSpecPoint", {'name': 'Hz19', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W19: Annotated[int, ("SunSpecPoint", {'name': 'W19', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Hz20: Annotated[int, ("SunSpecPoint", {'name': 'Hz20', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    W20: Annotated[int, ("SunSpecPoint", {'name': 'W20', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    CrvNam: Annotated[str, ("SunSpecPoint", {'name': 'CrvNam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpPT1Tms: Annotated[int, ("SunSpecPoint", {'name': 'RmpPT1Tms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpDecTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpDecTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    RmpIncTmm: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncTmm', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    RmpRsUp: Annotated[int, ("SunSpecPoint", {'name': 'RmpRsUp', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    SnptW: Annotated[int, ("SunSpecPoint", {'name': 'SnptW', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WRef: Annotated[int, ("SunSpecPoint", {'name': 'WRef', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    WRefStrHz: Annotated[int, ("SunSpecPoint", {'name': 'WRefStrHz', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    WRefStopHz: Annotated[int, ("SunSpecPoint", {'name': 'WRefStopHz', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model134ModEna(IntFlag):
    """
    Is curve-based Frequency-Watt control active.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model134(SunSpecModel, model_name="freq_watt", id=134):
    """
    Curve-Based Frequency-Watt 

    Attributes:
        ActCrv (int): Index of active curve. 0=no active curve.
        ModEna (Model134ModEna): Is curve-based Frequency-Watt control active.
        WinTms (int): Time window for freq-watt change.
        RvrtTms (int): Timeout period for freq-watt curve selection.
        RmpTms (int): Ramp time for moving from current mode to new mode.
        NCrv (int): Number of curves supported (recommend min. 4).
        NPt (int): Number of curve points supported (maximum of 20).
        Hz_SF (int): Scale factor for frequency.
        W_SF (int): Scale factor for percent WRef.
        RmpIncDec_SF (int): Scale factor for increment and decrement ramps.
    """

    ActCrv: Annotated[int, ("SunSpecPoint", {'name': 'ActCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    WinTms: Annotated[int, ("SunSpecPoint", {'name': 'WinTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RmpTms: Annotated[int, ("SunSpecPoint", {'name': 'RmpTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NCrv: Annotated[int, ("SunSpecPoint", {'name': 'NCrv', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    RmpIncDec_SF: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncDec_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    curve: Annotated[Model134CurveGroup, ("SunSpecGroup", {"name": "curve", "group_type": Model134CurveGroup})]

