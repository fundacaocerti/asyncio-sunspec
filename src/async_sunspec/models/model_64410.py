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


class Model64410PtGroup(SunSpecGroup):
    """
    Stored profile points.

    Attributes:
        Tms (int): Profile time.
        V (int): Profile voltage point in Volts.
        P (int): Profile power point in Watts.
        I (int): Profile current point in Amps.
        G (int): Profile irradiance point as percentage.
    """

    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF
    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    P: Annotated[int, ("SunSpecPoint", {'name': 'P', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    I: Annotated[int, ("SunSpecPoint", {'name': 'I', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: A_SF
    G: Annotated[int, ("SunSpecPoint", {'name': 'G', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Pct_SF


class Model64410DeptRef(IntFlag):
    """
    Profile references.

    Members:
        VOLTAGE (int): Voltage
        POWER (int): Power
        CURRENT (int): Current
        IRRADIANCE (int): Irradiance
    """
    VOLTAGE = 1 << 0
    POWER = 1 << 1
    CURRENT = 1 << 2
    IRRADIANCE = 1 << 3



class Model64410ProfGroup(SunSpecGroup):
    """
    Stored profile sets.

    Attributes:
        ActPt (int): Number of active points.
        DeptRef (Model64410DeptRef): Profile references.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    DeptRef: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Pt: Annotated[SunSpecRepeatingBlock[Model64410PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model64410PtGroup, "counter": "NPt"})]


class Model64410Mode(IntEnum):
    """
    Constant Voltage (CV) or Constant Current (CC) Mode

    Members:
        CV (int): Constant Voltage (CV) Mode
        CC (int): Constant Current (CC) Mode.
    """
    CV = 0
    CC = 1



class Model64410Ena(IntEnum):
    """
    Power On/Off

    Members:
        ON (int): Power On
        OFF (int): Power Off
    """
    ON = 1
    OFF = 0



class Model64410Reset(IntEnum):
    """
    Reset Device

    Members:
        RESET (int): Reset Device
        DO_NOT_RESET (int): Do Not Reset Device
    """
    RESET = 1
    DO_NOT_RESET = 0



class Model64410EN50530(IntEnum):
    """
    EN50530 Mode - Enable or disable EN50530 profile mode

    Members:
        EN50530 (int): EN50530 Mode
        DO_NOT_EN50530 (int): Do Not Use EN50530 Mode
    """
    EN50530 = 1
    DO_NOT_EN50530 = 0



class Model64410EnaProf(IntEnum):
    """
    Start/Stop the Profile

    Members:
        START (int): Start the Profile
        STOP (int): Stop the Profile
    """
    START = 1
    STOP = 0



class Model64410AdptProfRslt(IntEnum):
    """
    Result of last adopt profile operation.

    Members:
        IN_PROGRESS (int): Profile update in progress.
        COMPLETED (int): Profile update completed successfully.
        FAILED (int): Profile update failed.
    """
    IN_PROGRESS = 0
    COMPLETED = 1
    FAILED = 2



class Model64410(SunSpecModel, model_name="DCSimInterface", id=64410):
    """
    A generic DC simulator/power supply control interface for DER electrical testing.

    Attributes:
        VMaxLim (int): Upper Voltage Protection Limit
        PMaxLim (int): Upper Power Protection Limit
        IMaxLim (int): Upper Current Protection Limit
        Mode (Model64410Mode): Constant Voltage (CV) or Constant Current (CC) Mode
        Ena (Model64410Ena): Power On/Off
        Reset (Model64410Reset): Reset Device
        VSet (int): Voltage Setpoint
        PSet (int): Power Setpoint
        ISet (int): Current Setpoint
        EN50530 (Model64410EN50530): EN50530 Mode - Enable or disable EN50530 profile mode
        Vmpp (int): EN50530 MPP Voltage
        Pmpp (int): EN50530 MPP Power
        GSet (int): Irradiance Setpoint
        VSlewRate (int): Voltage Slew Rate
        PSlewRate (int): Power Slew Rate
        ISlewRate (int): Current Slew Rate
        EnaProf (Model64410EnaProf): Start/Stop the Profile
        AdptProfReq (int): Index of profile points to adopt. First curve index is 1.
        AdptProfRslt (Model64410AdptProfRslt): Result of last adopt profile operation.
        V (int): Measured Voltage
        P (int): Measured Power
        I (int): Measured Current
        Errors (str): Error States
        NPt (int): Number of profile points supported.
        NProf (int): Number of stored profiles supported.
        W_SF (int): Scale factor for power points.
        V_SF (int): Scale factor for voltage points.
        A_SF (int): Scale factor for current points.
        G_SF (int): Scale factor for irradiance.
        Tms_SF (int): Scale factor for time points.
        VSlew_SF (int): Scale factor for voltage slew rate.
        PSlew_SF (int): Scale factor for power slew rate.
        ISlew_SF (int): Scale factor for current slew rate.
        Pct_SF (int): Scale factor for percentages.
    """

    VMaxLim: Annotated[int, ("SunSpecPoint", {'name': 'VMaxLim', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    PMaxLim: Annotated[int, ("SunSpecPoint", {'name': 'PMaxLim', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    IMaxLim: Annotated[int, ("SunSpecPoint", {'name': 'IMaxLim', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: A_SF
    Mode: Annotated[int, ("SunSpecPoint", {'name': 'Mode', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Ena: Annotated[int, ("SunSpecPoint", {'name': 'Ena', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Reset: Annotated[int, ("SunSpecPoint", {'name': 'Reset', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VSet: Annotated[int, ("SunSpecPoint", {'name': 'VSet', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    PSet: Annotated[int, ("SunSpecPoint", {'name': 'PSet', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    ISet: Annotated[int, ("SunSpecPoint", {'name': 'ISet', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: A_SF
    EN50530: Annotated[int, ("SunSpecPoint", {'name': 'EN50530', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Vmpp: Annotated[int, ("SunSpecPoint", {'name': 'Vmpp', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Pmpp: Annotated[int, ("SunSpecPoint", {'name': 'Pmpp', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    GSet: Annotated[int, ("SunSpecPoint", {'name': 'GSet', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: G_SF
    VSlewRate: Annotated[int, ("SunSpecPoint", {'name': 'VSlewRate', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VSlew_SF
    PSlewRate: Annotated[int, ("SunSpecPoint", {'name': 'PSlewRate', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PSlew_SF
    ISlewRate: Annotated[int, ("SunSpecPoint", {'name': 'ISlewRate', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: ISlew_SF
    EnaProf: Annotated[int, ("SunSpecPoint", {'name': 'EnaProf', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    AdptProfReq: Annotated[int, ("SunSpecPoint", {'name': 'AdptProfReq', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    AdptProfRslt: Annotated[int, ("SunSpecPoint", {'name': 'AdptProfRslt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    P: Annotated[int, ("SunSpecPoint", {'name': 'P', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    I: Annotated[int, ("SunSpecPoint", {'name': 'I', 'ptype': 'int32', 'mandatory': False, 'static': False})]
    Errors: Annotated[str, ("SunSpecPoint", {'name': 'Errors', 'ptype': 'string', 'size': 32, 'mandatory': False, 'static': False, 'access': 'R'})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    NProf: Annotated[int, ("SunSpecPoint", {'name': 'NProf', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    G_SF: Annotated[int, ("SunSpecPoint", {'name': 'G_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Tms_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tms_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    VSlew_SF: Annotated[int, ("SunSpecPoint", {'name': 'VSlew_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    PSlew_SF: Annotated[int, ("SunSpecPoint", {'name': 'PSlew_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    ISlew_SF: Annotated[int, ("SunSpecPoint", {'name': 'ISlew_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Pct_SF: Annotated[int, ("SunSpecPoint", {'name': 'Pct_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Prof: Annotated[SunSpecRepeatingBlock[Model64410ProfGroup], ("SunSpecRepeatingBlock", {"name": "Prof", "ptype": "group", "group_type": Model64410ProfGroup, "counter": "NProf"})]

