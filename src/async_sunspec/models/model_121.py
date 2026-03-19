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


class Model121VArAct(IntEnum):
    """
    VAR action on change between charging and discharging: 1=switch 2=maintain VAR characterization.

    Members:
        SWITCH (int): SWITCH
        MAINTAIN (int): MAINTAIN
    """
    SWITCH = 1
    MAINTAIN = 2



class Model121ClcTotVA(IntEnum):
    """
    Calculation method for total apparent power. 1=vector 2=arithmetic.

    Members:
        VECTOR (int): VECTOR
        ARITHMETIC (int): ARITHMETIC
    """
    VECTOR = 1
    ARITHMETIC = 2



class Model121ConnPh(IntEnum):
    """
    Identity of connected phase for single phase inverters. A=1 B=2 C=3.

    Members:
        A (int): A
        B (int): B
        C (int): C
    """
    A = 1
    B = 2
    C = 3



class Model121(SunSpecModel, model_name="settings", id=121):
    """
    Inverter Controls Basic Settings 

    Attributes:
        WMax (int): Setting for maximum power output. Default to WRtg.
        VRef (int): Voltage at the PCC.
        VRefOfs (int): Offset  from PCC to inverter.
        VMax (int): Setpoint for maximum voltage.
        VMin (int): Setpoint for minimum voltage.
        VAMax (int): Setpoint for maximum apparent power. Default to VARtg.
        VArMaxQ1 (int): Setting for maximum reactive power in quadrant 1. Default to VArRtgQ1.
        VArMaxQ2 (int): Setting for maximum reactive power in quadrant 2. Default to VArRtgQ2.
        VArMaxQ3 (int): Setting for maximum reactive power in quadrant 3. Default to VArRtgQ3.
        VArMaxQ4 (int): Setting for maximum reactive power in quadrant 4. Default to VArRtgQ4.
        WGra (int): Default ramp rate of change of active power due to command or internal action.
        PFMinQ1 (int): Setpoint for minimum power factor value in quadrant 1. Default to PFRtgQ1.
        PFMinQ2 (int): Setpoint for minimum power factor value in quadrant 2. Default to PFRtgQ2.
        PFMinQ3 (int): Setpoint for minimum power factor value in quadrant 3. Default to PFRtgQ3.
        PFMinQ4 (int): Setpoint for minimum power factor value in quadrant 4. Default to PFRtgQ4.
        VArAct (Model121VArAct): VAR action on change between charging and discharging: 1=switch 2=maintain VAR characterization.
        ClcTotVA (Model121ClcTotVA): Calculation method for total apparent power. 1=vector 2=arithmetic.
        MaxRmpRte (int): Setpoint for maximum ramp rate as percentage of nominal maximum ramp rate. This setting will limit the rate that watts delivery to the grid can increase or decrease in response to intermittent PV generation.
        ECPNomHz (int): Setpoint for nominal frequency at the ECP.
        ConnPh (Model121ConnPh): Identity of connected phase for single phase inverters. A=1 B=2 C=3.
        WMax_SF (int): Scale factor for real power.
        VRef_SF (int): Scale factor for voltage at the PCC.
        VRefOfs_SF (int): Scale factor for offset voltage.
        VMinMax_SF (int): Scale factor for min/max voltages.
        VAMax_SF (int): Scale factor for apparent power.
        VArMax_SF (int): Scale factor for reactive power.
        WGra_SF (int): Scale factor for default ramp rate.
        PFMin_SF (int): Scale factor for minimum power factor.
        MaxRmpRte_SF (int): Scale factor for maximum ramp percentage.
        ECPNomHz_SF (int): Scale factor for nominal frequency.
    """

    WMax: Annotated[int, ("SunSpecPoint", {'name': 'WMax', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: WMax_SF
    VRef: Annotated[int, ("SunSpecPoint", {'name': 'VRef', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: VRef_SF
    VRefOfs: Annotated[int, ("SunSpecPoint", {'name': 'VRefOfs', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: VRefOfs_SF
    VMax: Annotated[int, ("SunSpecPoint", {'name': 'VMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VMinMax_SF
    VMin: Annotated[int, ("SunSpecPoint", {'name': 'VMin', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VMinMax_SF
    VAMax: Annotated[int, ("SunSpecPoint", {'name': 'VAMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VAMax_SF
    VArMaxQ1: Annotated[int, ("SunSpecPoint", {'name': 'VArMaxQ1', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArMax_SF
    VArMaxQ2: Annotated[int, ("SunSpecPoint", {'name': 'VArMaxQ2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArMax_SF
    VArMaxQ3: Annotated[int, ("SunSpecPoint", {'name': 'VArMaxQ3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArMax_SF
    VArMaxQ4: Annotated[int, ("SunSpecPoint", {'name': 'VArMaxQ4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VArMax_SF
    WGra: Annotated[int, ("SunSpecPoint", {'name': 'WGra', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WGra_SF
    PFMinQ1: Annotated[int, ("SunSpecPoint", {'name': 'PFMinQ1', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PFMin_SF
    PFMinQ2: Annotated[int, ("SunSpecPoint", {'name': 'PFMinQ2', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PFMin_SF
    PFMinQ3: Annotated[int, ("SunSpecPoint", {'name': 'PFMinQ3', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PFMin_SF
    PFMinQ4: Annotated[int, ("SunSpecPoint", {'name': 'PFMinQ4', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PFMin_SF
    VArAct: Annotated[int, ("SunSpecPoint", {'name': 'VArAct', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ClcTotVA: Annotated[int, ("SunSpecPoint", {'name': 'ClcTotVA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MaxRmpRte: Annotated[int, ("SunSpecPoint", {'name': 'MaxRmpRte', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: MaxRmpRte_SF
    ECPNomHz: Annotated[int, ("SunSpecPoint", {'name': 'ECPNomHz', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: ECPNomHz_SF
    ConnPh: Annotated[int, ("SunSpecPoint", {'name': 'ConnPh', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'WMax_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VRef_SF: Annotated[int, ("SunSpecPoint", {'name': 'VRef_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VRefOfs_SF: Annotated[int, ("SunSpecPoint", {'name': 'VRefOfs_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VMinMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'VMinMax_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    VAMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'VAMax_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    VArMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'VArMax_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    WGra_SF: Annotated[int, ("SunSpecPoint", {'name': 'WGra_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    PFMin_SF: Annotated[int, ("SunSpecPoint", {'name': 'PFMin_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    MaxRmpRte_SF: Annotated[int, ("SunSpecPoint", {'name': 'MaxRmpRte_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    ECPNomHz_SF: Annotated[int, ("SunSpecPoint", {'name': 'ECPNomHz_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]

