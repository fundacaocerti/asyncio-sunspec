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


class Model802ChaSt(IntEnum):
    """
    Charge status of storage device. Enumeration.

    Members:
        OFF (int): OFF
        EMPTY (int): EMPTY
        DISCHARGING (int): DISCHARGING
        CHARGING (int): CHARGING
        FULL (int): FULL
        HOLDING (int): HOLDING
        TESTING (int): TESTING
    """
    OFF = 1
    EMPTY = 2
    DISCHARGING = 3
    CHARGING = 4
    FULL = 5
    HOLDING = 6
    TESTING = 7



class Model802LocRemCtl(IntEnum):
    """
    Battery control mode. Enumeration.

    Members:
        REMOTE (int): REMOTE
        LOCAL (int): LOCAL
    """
    REMOTE = 0
    LOCAL = 1



class Model802Typ(IntEnum):
    """
    Type of battery. Enumeration.

    Members:
        NOT_APPLICABLE_UNKNOWN (int): NOT_APPLICABLE_UNKNOWN
        LEAD_ACID (int): LEAD_ACID
        NICKEL_METAL_HYDRATE (int): NICKEL_METAL_HYDRATE
        NICKEL_CADMIUM (int): NICKEL_CADMIUM
        LITHIUM_ION (int): LITHIUM_ION
        CARBON_ZINC (int): CARBON_ZINC
        ZINC_CHLORIDE (int): ZINC_CHLORIDE
        ALKALINE (int): ALKALINE
        RECHARGEABLE_ALKALINE (int): RECHARGEABLE_ALKALINE
        SODIUM_SULFUR (int): SODIUM_SULFUR
        FLOW (int): FLOW
        OTHER (int): OTHER
    """
    NOT_APPLICABLE_UNKNOWN = 0
    LEAD_ACID = 1
    NICKEL_METAL_HYDRATE = 2
    NICKEL_CADMIUM = 3
    LITHIUM_ION = 4
    CARBON_ZINC = 5
    ZINC_CHLORIDE = 6
    ALKALINE = 7
    RECHARGEABLE_ALKALINE = 8
    SODIUM_SULFUR = 9
    FLOW = 10
    OTHER = 99



class Model802State(IntEnum):
    """
    State of the battery bank.  Enumeration.

    Members:
        DISCONNECTED (int): DISCONNECTED
        INITIALIZING (int): INITIALIZING
        CONNECTED (int): CONNECTED
        STANDBY (int): STANDBY
        SOC_PROTECTION (int): SOC_PROTECTION
        SUSPENDING (int): SUSPENDING
        FAULT (int): FAULT
    """
    DISCONNECTED = 1
    INITIALIZING = 2
    CONNECTED = 3
    STANDBY = 4
    SOC_PROTECTION = 5
    SUSPENDING = 6
    FAULT = 99



class Model802Evt1(IntFlag):
    """
    Alarms and warnings.  Bit flags.

    Members:
        COMMUNICATION_ERROR (int): COMMUNICATION_ERROR
        OVER_TEMP_ALARM (int): OVER_TEMP_ALARM
        OVER_TEMP_WARNING (int): OVER_TEMP_WARNING
        UNDER_TEMP_ALARM (int): UNDER_TEMP_ALARM
        UNDER_TEMP_WARNING (int): UNDER_TEMP_WARNING
        OVER_CHARGE_CURRENT_ALARM (int): OVER_CHARGE_CURRENT_ALARM
        OVER_CHARGE_CURRENT_WARNING (int): OVER_CHARGE_CURRENT_WARNING
        OVER_DISCHARGE_CURRENT_ALARM (int): OVER_DISCHARGE_CURRENT_ALARM
        OVER_DISCHARGE_CURRENT_WARNING (int): OVER_DISCHARGE_CURRENT_WARNING
        OVER_VOLT_ALARM (int): OVER_VOLT_ALARM
        OVER_VOLT_WARNING (int): OVER_VOLT_WARNING
        UNDER_VOLT_ALARM (int): UNDER_VOLT_ALARM
        UNDER_VOLT_WARNING (int): UNDER_VOLT_WARNING
        UNDER_SOC_MIN_ALARM (int): UNDER_SOC_MIN_ALARM
        UNDER_SOC_MIN_WARNING (int): UNDER_SOC_MIN_WARNING
        OVER_SOC_MAX_ALARM (int): OVER_SOC_MAX_ALARM
        OVER_SOC_MAX_WARNING (int): OVER_SOC_MAX_WARNING
        VOLTAGE_IMBALANCE_WARNING (int): VOLTAGE_IMBALANCE_WARNING
        TEMPERATURE_IMBALANCE_ALARM (int): TEMPERATURE_IMBALANCE_ALARM
        TEMPERATURE_IMBALANCE_WARNING (int): TEMPERATURE_IMBALANCE_WARNING
        CONTACTOR_ERROR (int): CONTACTOR_ERROR
        FAN_ERROR (int): FAN_ERROR
        GROUND_FAULT (int): GROUND_FAULT
        OPEN_DOOR_ERROR (int): OPEN_DOOR_ERROR
        CURRENT_IMBALANCE_WARNING (int): CURRENT_IMBALANCE_WARNING
        OTHER_ALARM (int): OTHER_ALARM
        OTHER_WARNING (int): OTHER_WARNING
        RESERVED_1 (int): RESERVED_1
        CONFIGURATION_ALARM (int): CONFIGURATION_ALARM
        CONFIGURATION_WARNING (int): CONFIGURATION_WARNING
    """
    COMMUNICATION_ERROR = 1 << 0
    OVER_TEMP_ALARM = 1 << 1
    OVER_TEMP_WARNING = 1 << 2
    UNDER_TEMP_ALARM = 1 << 3
    UNDER_TEMP_WARNING = 1 << 4
    OVER_CHARGE_CURRENT_ALARM = 1 << 5
    OVER_CHARGE_CURRENT_WARNING = 1 << 6
    OVER_DISCHARGE_CURRENT_ALARM = 1 << 7
    OVER_DISCHARGE_CURRENT_WARNING = 1 << 8
    OVER_VOLT_ALARM = 1 << 9
    OVER_VOLT_WARNING = 1 << 10
    UNDER_VOLT_ALARM = 1 << 11
    UNDER_VOLT_WARNING = 1 << 12
    UNDER_SOC_MIN_ALARM = 1 << 13
    UNDER_SOC_MIN_WARNING = 1 << 14
    OVER_SOC_MAX_ALARM = 1 << 15
    OVER_SOC_MAX_WARNING = 1 << 16
    VOLTAGE_IMBALANCE_WARNING = 1 << 17
    TEMPERATURE_IMBALANCE_ALARM = 1 << 18
    TEMPERATURE_IMBALANCE_WARNING = 1 << 19
    CONTACTOR_ERROR = 1 << 20
    FAN_ERROR = 1 << 21
    GROUND_FAULT = 1 << 22
    OPEN_DOOR_ERROR = 1 << 23
    CURRENT_IMBALANCE_WARNING = 1 << 24
    OTHER_ALARM = 1 << 25
    OTHER_WARNING = 1 << 26
    RESERVED_1 = 1 << 27
    CONFIGURATION_ALARM = 1 << 28
    CONFIGURATION_WARNING = 1 << 29



class Model802ReqInvState(IntEnum):
    """
    Request from battery to start or stop the inverter.  Enumeration.

    Members:
        NO_REQUEST (int): NO_REQUEST
        START (int): START
        STOP (int): STOP
    """
    NO_REQUEST = 0
    START = 1
    STOP = 2



class Model802SetOp(IntEnum):
    """
    Instruct the battery bank to perform an operation such as connecting.  Enumeration.

    Members:
        CONNECT (int): CONNECT
        DISCONNECT (int): DISCONNECT
    """
    CONNECT = 1
    DISCONNECT = 2



class Model802SetInvState(IntEnum):
    """
    Set the current state of the inverter.

    Members:
        INVERTER_STOPPED (int): INVERTER_STOPPED
        INVERTER_STANDBY (int): INVERTER_STANDBY
        INVERTER_STARTED (int): INVERTER_STARTED
    """
    INVERTER_STOPPED = 1
    INVERTER_STANDBY = 2
    INVERTER_STARTED = 3



class Model802(SunSpecModel, model_name="battery", id=802):
    """
    Attributes:
        AHRtg (int): Nameplate charge capacity in amp-hours.
        WHRtg (int): Nameplate energy capacity in DC watt-hours.
        WChaRteMax (int): Maximum rate of energy transfer into the storage device in DC watts.
        WDisChaRteMax (int): Maximum rate of energy transfer out of the storage device in DC watts.
        DisChaRte (int): Self discharge rate.  Percentage of capacity (WHRtg) discharged per day.
        SoCMax (int): Manufacturer maximum state of charge, expressed as a percentage.
        SoCMin (int): Manufacturer minimum state of charge, expressed as a percentage.
        SocRsvMax (int): Setpoint for maximum reserve for storage as a percentage of the nominal maximum storage.
        SoCRsvMin (int): Setpoint for minimum reserve for storage as a percentage of the nominal maximum storage.
        SoC (int): State of charge, expressed as a percentage.
        DoD (int): Depth of discharge, expressed as a percentage.
        SoH (int): Percentage of battery life remaining.
        NCyc (int): Number of cycles executed in the battery.
        ChaSt (Model802ChaSt): Charge status of storage device. Enumeration.
        LocRemCtl (Model802LocRemCtl): Battery control mode. Enumeration.
        Hb (int): Value is incremented every second with periodic resets to zero.
        CtrlHb (int): Value is incremented every second with periodic resets to zero.
        AlmRst (int): Used to reset any latched alarms.  1 = Reset.
        Typ (Model802Typ): Type of battery. Enumeration.
        State (Model802State): State of the battery bank.  Enumeration.
        StateVnd (int): Vendor specific battery bank state.  Enumeration.
        WarrDt (int): Date the device warranty expires.
        Evt1 (Model802Evt1): Alarms and warnings.  Bit flags.
        Evt2 (int): Alarms and warnings.  Bit flags.
        EvtVnd1 (int): Vendor defined events.
        EvtVnd2 (int): Vendor defined events.
        V (int): DC Bus Voltage.
        VMax (int): Instantaneous maximum battery voltage.
        VMin (int): Instantaneous minimum battery voltage.
        CellVMax (int): Maximum voltage for all cells in the bank.
        CellVMaxStr (int): String containing the cell with maximum voltage.
        CellVMaxMod (int): Module containing the cell with maximum voltage.
        CellVMin (int): Minimum voltage for all cells in the bank.
        CellVMinStr (int): String containing the cell with minimum voltage.
        CellVMinMod (int): Module containing the cell with minimum voltage.
        CellVAvg (int): Average cell voltage for all cells in the bank.
        A (int): Total DC current flowing to/from the battery bank.
        AChaMax (int): Instantaneous maximum DC charge current.
        ADisChaMax (int): Instantaneous maximum DC discharge current.
        W (int): Total power flowing to/from the battery bank.
        ReqInvState (Model802ReqInvState): Request from battery to start or stop the inverter.  Enumeration.
        ReqW (int): AC Power requested by battery.
        SetOp (Model802SetOp): Instruct the battery bank to perform an operation such as connecting.  Enumeration.
        SetInvState (Model802SetInvState): Set the current state of the inverter.
        AHRtg_SF (int): Scale factor for charge capacity.
        WHRtg_SF (int): Scale factor for energy capacity.
        WChaDisChaMax_SF (int): Scale factor for maximum charge and discharge rate.
        DisChaRte_SF (int): Scale factor for self discharge rate.
        SoC_SF (int): Scale factor for state of charge values.
        DoD_SF (int): Scale factor for depth of discharge.
        SoH_SF (int): Scale factor for state of health.
        V_SF (int): Scale factor for DC bus voltage.
        CellV_SF (int): Scale factor for cell voltage.
        A_SF (int): Scale factor for DC current.
        AMax_SF (int): Scale factor for instantaneous DC charge/discharge current.
        W_SF (int): Scale factor for AC power request.
    """

    AHRtg: Annotated[int, ("SunSpecPoint", {'name': 'AHRtg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: AHRtg_SF
    WHRtg: Annotated[int, ("SunSpecPoint", {'name': 'WHRtg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: WHRtg_SF
    WChaRteMax: Annotated[int, ("SunSpecPoint", {'name': 'WChaRteMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: WChaDisChaMax_SF
    WDisChaRteMax: Annotated[int, ("SunSpecPoint", {'name': 'WDisChaRteMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: WChaDisChaMax_SF
    DisChaRte: Annotated[int, ("SunSpecPoint", {'name': 'DisChaRte', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DisChaRte_SF
    SoCMax: Annotated[int, ("SunSpecPoint", {'name': 'SoCMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoC_SF
    SoCMin: Annotated[int, ("SunSpecPoint", {'name': 'SoCMin', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoC_SF
    SocRsvMax: Annotated[int, ("SunSpecPoint", {'name': 'SocRsvMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: SoC_SF
    SoCRsvMin: Annotated[int, ("SunSpecPoint", {'name': 'SoCRsvMin', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: SoC_SF
    SoC: Annotated[int, ("SunSpecPoint", {'name': 'SoC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: SoC_SF
    DoD: Annotated[int, ("SunSpecPoint", {'name': 'DoD', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DoD_SF
    SoH: Annotated[int, ("SunSpecPoint", {'name': 'SoH', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoH_SF
    NCyc: Annotated[int, ("SunSpecPoint", {'name': 'NCyc', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    ChaSt: Annotated[int, ("SunSpecPoint", {'name': 'ChaSt', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    LocRemCtl: Annotated[int, ("SunSpecPoint", {'name': 'LocRemCtl', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Hb: Annotated[int, ("SunSpecPoint", {'name': 'Hb', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CtrlHb: Annotated[int, ("SunSpecPoint", {'name': 'CtrlHb', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    AlmRst: Annotated[int, ("SunSpecPoint", {'name': 'AlmRst', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Typ: Annotated[int, ("SunSpecPoint", {'name': 'Typ', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    State: Annotated[int, ("SunSpecPoint", {'name': 'State', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StateVnd: Annotated[int, ("SunSpecPoint", {'name': 'StateVnd', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    WarrDt: Annotated[int, ("SunSpecPoint", {'name': 'WarrDt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    Evt1: Annotated[int, ("SunSpecPoint", {'name': 'Evt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Evt2: Annotated[int, ("SunSpecPoint", {'name': 'Evt2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd1: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd2: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    VMax: Annotated[int, ("SunSpecPoint", {'name': 'VMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    VMin: Annotated[int, ("SunSpecPoint", {'name': 'VMin', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    CellVMax: Annotated[int, ("SunSpecPoint", {'name': 'CellVMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    CellVMaxStr: Annotated[int, ("SunSpecPoint", {'name': 'CellVMaxStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'CellVMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMin: Annotated[int, ("SunSpecPoint", {'name': 'CellVMin', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    CellVMinStr: Annotated[int, ("SunSpecPoint", {'name': 'CellVMinStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMinMod: Annotated[int, ("SunSpecPoint", {'name': 'CellVMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'CellVAvg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    AChaMax: Annotated[int, ("SunSpecPoint", {'name': 'AChaMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: AMax_SF
    ADisChaMax: Annotated[int, ("SunSpecPoint", {'name': 'ADisChaMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: AMax_SF
    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: W_SF
    ReqInvState: Annotated[int, ("SunSpecPoint", {'name': 'ReqInvState', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ReqW: Annotated[int, ("SunSpecPoint", {'name': 'ReqW', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: W_SF
    SetOp: Annotated[int, ("SunSpecPoint", {'name': 'SetOp', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    SetInvState: Annotated[int, ("SunSpecPoint", {'name': 'SetInvState', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AHRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'AHRtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    WHRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'WHRtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    WChaDisChaMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'WChaDisChaMax_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DisChaRte_SF: Annotated[int, ("SunSpecPoint", {'name': 'DisChaRte_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    SoC_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoC_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    DoD_SF: Annotated[int, ("SunSpecPoint", {'name': 'DoD_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    SoH_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    CellV_SF: Annotated[int, ("SunSpecPoint", {'name': 'CellV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    AMax_SF: Annotated[int, ("SunSpecPoint", {'name': 'AMax_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]

