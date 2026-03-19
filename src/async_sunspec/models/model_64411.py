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


class Model64411PtGroup(SunSpecGroup):
    """
    Stored AC profile points.

    Attributes:
        Tms (int): Profile time.
        VA (int): Profile voltage phase A point in Volts.
        VB (int): Profile voltage phase B point in Volts.
        VC (int): Profile voltage phase C point in Volts.
        Hz (int): Profile frequency point in Hz.
        PhaseAngleA (int): Profile phase A angle in degrees.
        PhaseAngleB (int): Profile phase B angle in degrees.
        PhaseAngleC (int): Profile phase C angle in degrees.
    """

    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    VA: Annotated[int, ("SunSpecPoint", {'name': 'VA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VB: Annotated[int, ("SunSpecPoint", {'name': 'VB', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VC: Annotated[int, ("SunSpecPoint", {'name': 'VC', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    PhaseAngleA: Annotated[int, ("SunSpecPoint", {'name': 'PhaseAngleA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PhaseAngleB: Annotated[int, ("SunSpecPoint", {'name': 'PhaseAngleB', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PhaseAngleC: Annotated[int, ("SunSpecPoint", {'name': 'PhaseAngleC', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]


class Model64411ProfGroup(SunSpecGroup):
    """
    Stored AC profile sets.

    Attributes:
        Name (str): Profile name.
        ActPt (int): Number of active points.
    """

    Name: Annotated[str, ("SunSpecPoint", {'name': 'Name', 'ptype': 'string', 'size': 32, 'mandatory': False, 'static': False, 'access': 'RW'})]
    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Pt: Annotated[SunSpecRepeatingBlock[Model64411PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model64411PtGroup, "counter": "NPt"})]


class Model64411Output(IntEnum):
    """
    AC Output State

    Members:
        OFF (int): Output Off
        ON (int): Output On
    """
    OFF = 0
    ON = 1



class Model64411Relay(IntEnum):
    """
    AC Relay State

    Members:
        OPEN (int): Relay Open
        CLOSED (int): Relay Closed
    """
    OPEN = 0
    CLOSED = 1



class Model64411Regen(IntEnum):
    """
    Regeneration State

    Members:
        OFF (int): Regen Off
        ON (int): Regen On
    """
    OFF = 0
    ON = 1



class Model64411EnaProf(IntEnum):
    """
    Start/Stop the AC Profile

    Members:
        STOP (int): Stop Profile
        START (int): Start Profile Immediately
        TRIGGER (int): Start Profile via External Trigger Signal
    """
    STOP = 0
    START = 1
    TRIGGER = 2



class Model64411ProfRslt(IntEnum):
    """
    Result of last profile operation.

    Members:
        IN_PROGRESS (int): Profile update in progress.
        COMPLETED (int): Profile update completed successfully.
        FAILED (int): Profile update failed.
    """
    IN_PROGRESS = 0
    COMPLETED = 1
    FAILED = 2



class Model64411(SunSpecModel, model_name="ACSimInterface", id=64411):
    """
    A generic AC simulator/power supply control interface for DER electrical testing.

    Attributes:
        Phases (int): Set the number of active phases for the power supply
        PhaseAngle (int): Phase angle (deg) between phases. 0 for signle phase, 120 for two phase, 120 for three phase.
        VNom (int): Nominal L-N Voltage
        VMax (int): Maximum Voltage Protection Level
        IMax (int): Maximum Current Protection Level
        Freq (int): Frequency Setpoint
        Output (Model64411Output): AC Output State
        Relay (Model64411Relay): AC Relay State
        Regen (Model64411Regen): Regeneration State
        VSet (int): Voltage Setpoint (all phases)
        VSetA (int): Voltage Setpoint Phase A
        VSetB (int): Voltage Setpoint Phase B
        VSetC (int): Voltage Setpoint Phase C
        FreqSlew (int): Frequency Slew Rate
        VSlew (int): Voltage Slew Rate
        VA (int): Measured Voltage Phase A
        VB (int): Measured Voltage Phase B
        VC (int): Measured Voltage Phase C
        Hz (int): Measured Frequency
        IA (int): Measured Current Phase A
        IB (int): Measured Current Phase B
        IC (int): Measured Current Phase C
        VHarA (str): Voltage Harmonics Pct, Phase A (comma seperated string for harmonics 1-50)
        VHarB (str): Voltage Harmonics Pct, Phase B (comma seperated string for harmonics 1-50)
        VHarC (str): Voltage Harmonics Pct, Phase C (comma seperated string for harmonics 1-50)
        IHarA (str): Current Harmonics Pct, Phase A (comma seperated string for harmonics 1-50)
        IHarB (str): Current Harmonics Pct, Phase B (comma seperated string for harmonics 1-50)
        IHarC (str): Current Harmonics Pct, Phase C (comma seperated string for harmonics 1-50)
        IIntHarA (str): Current Interharmonics Pct, Phase A (comma seperated string for interharmonics 1-50)
        IIntHarB (str): Current Interharmonics Pct, Phase B (comma seperated string for interharmonics 1-50)
        IIntHarC (str): Current Interharmonics Pct, Phase C (comma seperated string for interharmonics 1-50)
        VThdA (int): Voltage THD Phase A
        VThdB (int): Voltage THD Phase B
        VThdC (int): Voltage THD Phase C
        IThdA (int): Current THD Phase A
        IThdB (int): Current THD Phase B
        IThdC (int): Current THD Phase C
        EnaProf (Model64411EnaProf): Start/Stop the AC Profile
        ProfRslt (Model64411ProfRslt): Result of last profile operation.
        NProf (int): Number of stored profiles supported.
        NPt (int): Max profile points in the profiles.
        V_SF (int): Scale factor for voltage points.
        A_SF (int): Scale factor for current points.
        Tms_SF (int): Scale factor for time points.
        Hz_SF (int): Scale factor for frequency points.
        HzSlew_SF (int): Scale factor for frequency slew rate.
        VSlew_SF (int): Scale factor for voltage slew rate.
        THD_SF (int): Scale factor for THD values.
    """

    Phases: Annotated[int, ("SunSpecPoint", {'name': 'Phases', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PhaseAngle: Annotated[int, ("SunSpecPoint", {'name': 'PhaseAngle', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VNom: Annotated[int, ("SunSpecPoint", {'name': 'VNom', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VMax: Annotated[int, ("SunSpecPoint", {'name': 'VMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    IMax: Annotated[int, ("SunSpecPoint", {'name': 'IMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: A_SF
    Freq: Annotated[int, ("SunSpecPoint", {'name': 'Freq', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Output: Annotated[int, ("SunSpecPoint", {'name': 'Output', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Relay: Annotated[int, ("SunSpecPoint", {'name': 'Relay', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Regen: Annotated[int, ("SunSpecPoint", {'name': 'Regen', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VSet: Annotated[int, ("SunSpecPoint", {'name': 'VSet', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VSetA: Annotated[int, ("SunSpecPoint", {'name': 'VSetA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VSetB: Annotated[int, ("SunSpecPoint", {'name': 'VSetB', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VSetC: Annotated[int, ("SunSpecPoint", {'name': 'VSetC', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    FreqSlew: Annotated[int, ("SunSpecPoint", {'name': 'FreqSlew', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: HzSlew_SF
    VSlew: Annotated[int, ("SunSpecPoint", {'name': 'VSlew', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VSlew_SF
    VA: Annotated[int, ("SunSpecPoint", {'name': 'VA', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: V_SF
    VB: Annotated[int, ("SunSpecPoint", {'name': 'VB', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: V_SF
    VC: Annotated[int, ("SunSpecPoint", {'name': 'VC', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: V_SF
    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: Hz_SF
    IA: Annotated[int, ("SunSpecPoint", {'name': 'IA', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: A_SF
    IB: Annotated[int, ("SunSpecPoint", {'name': 'IB', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: A_SF
    IC: Annotated[int, ("SunSpecPoint", {'name': 'IC', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: A_SF
    VHarA: Annotated[str, ("SunSpecPoint", {'name': 'VHarA', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    VHarB: Annotated[str, ("SunSpecPoint", {'name': 'VHarB', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    VHarC: Annotated[str, ("SunSpecPoint", {'name': 'VHarC', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    IHarA: Annotated[str, ("SunSpecPoint", {'name': 'IHarA', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    IHarB: Annotated[str, ("SunSpecPoint", {'name': 'IHarB', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    IHarC: Annotated[str, ("SunSpecPoint", {'name': 'IHarC', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    IIntHarA: Annotated[str, ("SunSpecPoint", {'name': 'IIntHarA', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    IIntHarB: Annotated[str, ("SunSpecPoint", {'name': 'IIntHarB', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    IIntHarC: Annotated[str, ("SunSpecPoint", {'name': 'IIntHarC', 'ptype': 'string', 'size': 150, 'mandatory': False, 'static': False, 'access': 'R'})]
    VThdA: Annotated[int, ("SunSpecPoint", {'name': 'VThdA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'R'})]  # sf: THD_SF
    VThdB: Annotated[int, ("SunSpecPoint", {'name': 'VThdB', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'R'})]  # sf: THD_SF
    VThdC: Annotated[int, ("SunSpecPoint", {'name': 'VThdC', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'R'})]  # sf: THD_SF
    IThdA: Annotated[int, ("SunSpecPoint", {'name': 'IThdA', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'R'})]  # sf: THD_SF
    IThdB: Annotated[int, ("SunSpecPoint", {'name': 'IThdB', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'R'})]  # sf: THD_SF
    IThdC: Annotated[int, ("SunSpecPoint", {'name': 'IThdC', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'R'})]  # sf: THD_SF
    EnaProf: Annotated[int, ("SunSpecPoint", {'name': 'EnaProf', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ProfRslt: Annotated[int, ("SunSpecPoint", {'name': 'ProfRslt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NProf: Annotated[int, ("SunSpecPoint", {'name': 'NProf', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Tms_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tms_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    HzSlew_SF: Annotated[int, ("SunSpecPoint", {'name': 'HzSlew_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    VSlew_SF: Annotated[int, ("SunSpecPoint", {'name': 'VSlew_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    THD_SF: Annotated[int, ("SunSpecPoint", {'name': 'THD_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Prof: Annotated[SunSpecRepeatingBlock[Model64411ProfGroup], ("SunSpecRepeatingBlock", {"name": "Prof", "ptype": "group", "group_type": Model64411ProfGroup, "counter": "NProf"})]

