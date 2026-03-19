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
from enum import IntFlag


class Model122PVConn(IntFlag):
    """
    PV inverter present/available status. Enumerated value.

    Members:
        CONNECTED (int): CONNECTED
        AVAILABLE (int): AVAILABLE
        OPERATING (int): OPERATING
        TEST (int): TEST
    """
    CONNECTED = 1 << 0
    AVAILABLE = 1 << 1
    OPERATING = 1 << 2
    TEST = 1 << 3



class Model122StorConn(IntFlag):
    """
    Storage inverter present/available status. Enumerated value.

    Members:
        CONNECTED (int): CONNECTED
        AVAILABLE (int): AVAILABLE
        OPERATING (int): OPERATING
        TEST (int): TEST
    """
    CONNECTED = 1 << 0
    AVAILABLE = 1 << 1
    OPERATING = 1 << 2
    TEST = 1 << 3



class Model122ECPConn(IntFlag):
    """
    ECP connection status: disconnected=0  connected=1.

    Members:
        DISCONNECTED (int): DISCONNECTED
        CONNECTED (int): CONNECTED
    """
    DISCONNECTED = 1 << 0
    CONNECTED = 1 << 1



class Model122StSetLimMsk(IntFlag):
    """
    Bit Mask indicating setpoint limit(s) reached.

    Members:
        WMax (int): WMax
        VAMax (int): VAMax
        VArAval (int): VArAval
        VArMaxQ1 (int): VArMaxQ1
        VArMaxQ2 (int): VArMaxQ2
        VArMaxQ3 (int): VArMaxQ3
        VArMaxQ4 (int): VArMaxQ4
        PFMinQ1 (int): PFMinQ1
        PFMinQ2 (int): PFMinQ2
        PFMinQ3 (int): PFMinQ3
        PFMinQ4 (int): PFMinQ4
    """
    WMax = 1 << 0
    VAMax = 1 << 1
    VArAval = 1 << 2
    VArMaxQ1 = 1 << 3
    VArMaxQ2 = 1 << 4
    VArMaxQ3 = 1 << 5
    VArMaxQ4 = 1 << 6
    PFMinQ1 = 1 << 7
    PFMinQ2 = 1 << 8
    PFMinQ3 = 1 << 9
    PFMinQ4 = 1 << 10



class Model122StActCtl(IntFlag):
    """
    Bit Mask indicating which inverter controls are currently active.

    Members:
        FixedW (int): FixedW
        FixedVAR (int): FixedVAR
        FixedPF (int): FixedPF
        Volt_VAr (int): Volt_VAr
        Freq_Watt_Param (int): Freq_Watt_Param
        Freq_Watt_Curve (int): Freq_Watt_Curve
        Dyn_Reactive_Current (int): Dyn_Reactive_Current
        LVRT (int): LVRT
        HVRT (int): HVRT
        Watt_PF (int): Watt_PF
        Volt_Watt (int): Volt_Watt
        Scheduled (int): Scheduled
        LFRT (int): LFRT
        HFRT (int): HFRT
    """
    FixedW = 1 << 0
    FixedVAR = 1 << 1
    FixedPF = 1 << 2
    Volt_VAr = 1 << 3
    Freq_Watt_Param = 1 << 4
    Freq_Watt_Curve = 1 << 5
    Dyn_Reactive_Current = 1 << 6
    LVRT = 1 << 7
    HVRT = 1 << 8
    Watt_PF = 1 << 9
    Volt_Watt = 1 << 10
    Scheduled = 1 << 12
    LFRT = 1 << 13
    HFRT = 1 << 14



class Model122RtSt(IntFlag):
    """
    Bit Mask indicating active ride-through status.

    Members:
        LVRT_ACTIVE (int): LVRT_ACTIVE
        HVRT_ACTIVE (int): HVRT_ACTIVE
        LFRT_ACTIVE (int): LFRT_ACTIVE
        HFRT_ACTIVE (int): HFRT_ACTIVE
    """
    LVRT_ACTIVE = 1 << 0
    HVRT_ACTIVE = 1 << 1
    LFRT_ACTIVE = 1 << 2
    HFRT_ACTIVE = 1 << 3



class Model122(SunSpecModel, model_name="status", id=122):
    """
    Inverter Controls Extended Measurements and Status 

    Attributes:
        PVConn (Model122PVConn): PV inverter present/available status. Enumerated value.
        StorConn (Model122StorConn): Storage inverter present/available status. Enumerated value.
        ECPConn (Model122ECPConn): ECP connection status: disconnected=0  connected=1.
        ActWh (int): AC lifetime active (real) energy output.
        ActVAh (int): AC lifetime apparent energy output.
        ActVArhQ1 (int): AC lifetime reactive energy output in quadrant 1.
        ActVArhQ2 (int): AC lifetime reactive energy output in quadrant 2.
        ActVArhQ3 (int): AC lifetime negative energy output  in quadrant 3.
        ActVArhQ4 (int): AC lifetime reactive energy output  in quadrant 4.
        VArAval (int): Amount of VARs available without impacting watts output.
        VArAval_SF (int): Scale factor for available VARs.
        WAval (int): Amount of Watts available.
        WAval_SF (int): Scale factor for available Watts.
        StSetLimMsk (Model122StSetLimMsk): Bit Mask indicating setpoint limit(s) reached.
        StActCtl (Model122StActCtl): Bit Mask indicating which inverter controls are currently active.
        TmSrc (str): Source of time synchronization.
        Tms (int): Seconds since 01-01-2000 00:00 UTC
        RtSt (Model122RtSt): Bit Mask indicating active ride-through status.
        Ris (int): Isolation resistance.
        Ris_SF (int): Scale factor for isolation resistance.
    """

    PVConn: Annotated[int, ("SunSpecPoint", {'name': 'PVConn', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StorConn: Annotated[int, ("SunSpecPoint", {'name': 'StorConn', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ECPConn: Annotated[int, ("SunSpecPoint", {'name': 'ECPConn', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ActWh: Annotated[int, ("SunSpecPoint", {'name': 'ActWh', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    ActVAh: Annotated[int, ("SunSpecPoint", {'name': 'ActVAh', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    ActVArhQ1: Annotated[int, ("SunSpecPoint", {'name': 'ActVArhQ1', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    ActVArhQ2: Annotated[int, ("SunSpecPoint", {'name': 'ActVArhQ2', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    ActVArhQ3: Annotated[int, ("SunSpecPoint", {'name': 'ActVArhQ3', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    ActVArhQ4: Annotated[int, ("SunSpecPoint", {'name': 'ActVArhQ4', 'ptype': 'uint64', 'mandatory': False, 'static': False})]
    VArAval: Annotated[int, ("SunSpecPoint", {'name': 'VArAval', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: VArAval_SF
    VArAval_SF: Annotated[int, ("SunSpecPoint", {'name': 'VArAval_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    WAval: Annotated[int, ("SunSpecPoint", {'name': 'WAval', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: WAval_SF
    WAval_SF: Annotated[int, ("SunSpecPoint", {'name': 'WAval_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    StSetLimMsk: Annotated[int, ("SunSpecPoint", {'name': 'StSetLimMsk', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    StActCtl: Annotated[int, ("SunSpecPoint", {'name': 'StActCtl', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    TmSrc: Annotated[str, ("SunSpecPoint", {'name': 'TmSrc', 'ptype': 'string', 'size': 4, 'mandatory': False, 'static': False})]
    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    RtSt: Annotated[int, ("SunSpecPoint", {'name': 'RtSt', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Ris: Annotated[int, ("SunSpecPoint", {'name': 'Ris', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: Ris_SF
    Ris_SF: Annotated[int, ("SunSpecPoint", {'name': 'Ris_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]

