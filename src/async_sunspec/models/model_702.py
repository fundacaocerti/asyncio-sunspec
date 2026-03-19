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


class Model702NorOpCatRtg(IntEnum):
    """
    Normal operating performance category as specified in IEEE 1547-2018.

    Members:
        CAT_A (int): Category A
        CAT_B (int): Category B
    """
    CAT_A = 0
    CAT_B = 1



class Model702AbnOpCatRtg(IntEnum):
    """
    Abnormal operating performance category as specified in IEEE 1547-2018.

    Members:
        CAT_1 (int): Category I
        CAT_2 (int): Category II
        CAT_3 (int): Category III
    """
    CAT_1 = 0
    CAT_2 = 1
    CAT_3 = 2



class Model702CtrlModes(IntFlag):
    """
    Supported control mode functions.

    Members:
        MAX_W (int): Limit Maximum Active Power
        FIXED_W (int): Fixed Active Power
        FIXED_VAR (int): Fixed Reactive Power
        FIXED_PF (int): Fixed Power Factor
        VOLT_VAR (int): Volt-Var Function
        FREQ_WATT (int): Freq-Watt Function
        DYN_REACT_CURR (int): Dynamic Reactive Current Function
        LV_TRIP (int): Low-Voltage Trip
        HV_TRIP (int): High-Voltage Trip
        WATT_VAR (int): Watt-Var Function
        VOLT_WATT (int): Volt-Watt Function
        SCHEDULED (int): Scheduling
        LF_TRIP (int): Low-Frequency Trip
        HF_TRIP (int): High-Frequency Trip
    """
    MAX_W = 1 << 0
    FIXED_W = 1 << 1
    FIXED_VAR = 1 << 2
    FIXED_PF = 1 << 3
    VOLT_VAR = 1 << 4
    FREQ_WATT = 1 << 5
    DYN_REACT_CURR = 1 << 6
    LV_TRIP = 1 << 7
    HV_TRIP = 1 << 8
    WATT_VAR = 1 << 9
    VOLT_WATT = 1 << 10
    SCHEDULED = 1 << 11
    LF_TRIP = 1 << 12
    HF_TRIP = 1 << 13



class Model702IntIslandCatRtg(IntFlag):
    """
    Intentional island categories.

    Members:
        UNCATEGORIZED (int): Uncategorized
        INT_ISL_CAPABLE (int): Intentional Island-Capable
        BLACK_START_CAPABLE (int): Black Start-Capable
        ISOCH_CAPABLE (int): Isochronous-Capable
    """
    UNCATEGORIZED = 1 << 0
    INT_ISL_CAPABLE = 1 << 1
    BLACK_START_CAPABLE = 1 << 2
    ISOCH_CAPABLE = 1 << 3



class Model702IntIslandCat(IntFlag):
    """
    Intentional island categories.

    Members:
        UNCATEGORIZED (int): Uncategorized
        INT_ISL_CAPABLE (int): Intentional Island-Capable
        BLACK_START_CAPABLE (int): Black Start-Capable
        ISOCH_CAPABLE (int): Isochronous-Capable
    """
    UNCATEGORIZED = 1 << 0
    INT_ISL_CAPABLE = 1 << 1
    BLACK_START_CAPABLE = 1 << 2
    ISOCH_CAPABLE = 1 << 3



class Model702(SunSpecModel, model_name="DERCapacity", id=702):
    """
    DER capacity model.

    Attributes:
        WMaxRtg (int): Maximum active power rating at unity power factor in watts.
        WOvrExtRtg (int): Active power rating at specified over-excited power factor in watts.
        WOvrExtRtgPF (int): Specified over-excited power factor.
        WUndExtRtg (int): Active power rating at specified under-excited power factor in watts.
        WUndExtRtgPF (int): Specified under-excited power factor.
        VAMaxRtg (int): Maximum apparent power rating in voltamperes.
        VarMaxInjRtg (int): Maximum injected reactive power rating in vars.
        VarMaxAbsRtg (int): Maximum absorbed reactive power rating in vars.
        WChaRteMaxRtg (int): Maximum active power charge rate in watts.
        WDisChaRteMaxRtg (int): Maximum active power discharge rate in watts.
        VAChaRteMaxRtg (int): Maximum apparent power charge rate in voltamperes.
        VADisChaRteMaxRtg (int): Maximum apparent power discharge rate in voltamperes.
        VNomRtg (int): AC voltage nominal rating.
        VMaxRtg (int): AC voltage maximum rating.
        VMinRtg (int): AC voltage minimum rating.
        AMaxRtg (int): AC current maximum rating in amps.
        PFOvrExtRtg (int): Unused. Please use WOvrExtRtgPF.
        PFUndExtRtg (int): Unused. Please use WUndExtRtgPF.
        ReactSusceptRtg (int): Reactive susceptance that remains connected to the Area EPS in the cease to energize and trip state.
        NorOpCatRtg (Model702NorOpCatRtg): Normal operating performance category as specified in IEEE 1547-2018.
        AbnOpCatRtg (Model702AbnOpCatRtg): Abnormal operating performance category as specified in IEEE 1547-2018.
        CtrlModes (Model702CtrlModes): Supported control mode functions.
        IntIslandCatRtg (Model702IntIslandCatRtg): Intentional island categories.
        WMax (int): Maximum active power setting used to adjust maximum active power setting.
        WMaxOvrExt (int): Active power setting at specified over-excited power factor in watts.
        WOvrExtPF (int): Specified over-excited power factor.
        WMaxUndExt (int): Active power setting at specified under-excited power factor in watts.
        WUndExtPF (int): Specified under-excited power factor.
        VAMax (int): Maximum apparent power setting used to adjust maximum apparent power rating.
        VarMaxInj (int): Maximum injected reactive power setting used to adjust maximum injected reactive power rating.
        VarMaxAbs (int): Maximum absorbed reactive power setting used to adjust maximum absorbed reactive power rating.
        WChaRteMax (int): Maximum active power charge rate setting used to adjust maximum active power charge rate rating.
        WDisChaRteMax (int): Maximum active power discharge rate setting used to adjust maximum active power discharge rate rating.
        VAChaRteMax (int): Maximum apparent power charge rate setting used to adjust maximum apparent power charge rate rating.
        VADisChaRteMax (int): Maximum apparent power discharge rate setting used to adjust maximum apparent power discharge rate rating.
        VNom (int): Nominal AC voltage setting.
        VMax (int): AC voltage maximum setting used to adjust AC voltage maximum rating.
        VMin (int): AC voltage minimum setting used to adjust AC voltage minimum rating.
        AMax (int): Maximum AC current setting used to adjust maximum AC current rating.
        PFOvrExt (int): Unused. Please use WOvrExtPF.
        PFUndExt (int): Unused. Please use WUndExtPF.
        IntIslandCat (Model702IntIslandCat): Intentional island categories.
        W_SF (int): Active power scale factor.
        PF_SF (int): Power factor scale factor.
        VA_SF (int): Apparent power scale factor.
        Var_SF (int): Reactive power scale factor.
        V_SF (int): Voltage scale factor.
        A_SF (int): Current scale factor.
        S_SF (int): Susceptance scale factor.
    """

    WMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'WMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: W_SF
    WOvrExtRtg: Annotated[int, ("SunSpecPoint", {'name': 'WOvrExtRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: W_SF
    WOvrExtRtgPF: Annotated[int, ("SunSpecPoint", {'name': 'WOvrExtRtgPF', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: PF_SF
    WUndExtRtg: Annotated[int, ("SunSpecPoint", {'name': 'WUndExtRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: W_SF
    WUndExtRtgPF: Annotated[int, ("SunSpecPoint", {'name': 'WUndExtRtgPF', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: PF_SF
    VAMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'VAMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: VA_SF
    VarMaxInjRtg: Annotated[int, ("SunSpecPoint", {'name': 'VarMaxInjRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: Var_SF
    VarMaxAbsRtg: Annotated[int, ("SunSpecPoint", {'name': 'VarMaxAbsRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: Var_SF
    WChaRteMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'WChaRteMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: W_SF
    WDisChaRteMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'WDisChaRteMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: W_SF
    VAChaRteMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'VAChaRteMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: VA_SF
    VADisChaRteMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'VADisChaRteMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: VA_SF
    VNomRtg: Annotated[int, ("SunSpecPoint", {'name': 'VNomRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: V_SF
    VMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'VMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: V_SF
    VMinRtg: Annotated[int, ("SunSpecPoint", {'name': 'VMinRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: V_SF
    AMaxRtg: Annotated[int, ("SunSpecPoint", {'name': 'AMaxRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: A_SF
    PFOvrExtRtg: Annotated[int, ("SunSpecPoint", {'name': 'PFOvrExtRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: PF_SF
    PFUndExtRtg: Annotated[int, ("SunSpecPoint", {'name': 'PFUndExtRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: PF_SF
    ReactSusceptRtg: Annotated[int, ("SunSpecPoint", {'name': 'ReactSusceptRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]  # sf: S_SF
    NorOpCatRtg: Annotated[int, ("SunSpecPoint", {'name': 'NorOpCatRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]
    AbnOpCatRtg: Annotated[int, ("SunSpecPoint", {'name': 'AbnOpCatRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]
    CtrlModes: Annotated[int, ("SunSpecPoint", {'name': 'CtrlModes', 'ptype': 'uint32', 'mandatory': False, 'static': True})]
    IntIslandCatRtg: Annotated[int, ("SunSpecPoint", {'name': 'IntIslandCatRtg', 'ptype': 'uint16', 'mandatory': False, 'static': True})]
    WMax: Annotated[int, ("SunSpecPoint", {'name': 'WMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    WMaxOvrExt: Annotated[int, ("SunSpecPoint", {'name': 'WMaxOvrExt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    WOvrExtPF: Annotated[int, ("SunSpecPoint", {'name': 'WOvrExtPF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    WMaxUndExt: Annotated[int, ("SunSpecPoint", {'name': 'WMaxUndExt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    WUndExtPF: Annotated[int, ("SunSpecPoint", {'name': 'WUndExtPF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    VAMax: Annotated[int, ("SunSpecPoint", {'name': 'VAMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VA_SF
    VarMaxInj: Annotated[int, ("SunSpecPoint", {'name': 'VarMaxInj', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Var_SF
    VarMaxAbs: Annotated[int, ("SunSpecPoint", {'name': 'VarMaxAbs', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Var_SF
    WChaRteMax: Annotated[int, ("SunSpecPoint", {'name': 'WChaRteMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    WDisChaRteMax: Annotated[int, ("SunSpecPoint", {'name': 'WDisChaRteMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    VAChaRteMax: Annotated[int, ("SunSpecPoint", {'name': 'VAChaRteMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VA_SF
    VADisChaRteMax: Annotated[int, ("SunSpecPoint", {'name': 'VADisChaRteMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VA_SF
    VNom: Annotated[int, ("SunSpecPoint", {'name': 'VNom', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VMax: Annotated[int, ("SunSpecPoint", {'name': 'VMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VMin: Annotated[int, ("SunSpecPoint", {'name': 'VMin', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    AMax: Annotated[int, ("SunSpecPoint", {'name': 'AMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: A_SF
    PFOvrExt: Annotated[int, ("SunSpecPoint", {'name': 'PFOvrExt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    PFUndExt: Annotated[int, ("SunSpecPoint", {'name': 'PFUndExt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    IntIslandCat: Annotated[int, ("SunSpecPoint", {'name': 'IntIslandCat', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    VA_SF: Annotated[int, ("SunSpecPoint", {'name': 'VA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Var_SF: Annotated[int, ("SunSpecPoint", {'name': 'Var_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    S_SF: Annotated[int, ("SunSpecPoint", {'name': 'S_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]

