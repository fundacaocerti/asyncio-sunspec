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


class Model807ModSt(IntFlag):
    """
    Current status of the module.

    Members:
        MODULE_ENABLED (int): MODULE_ENABLED
        CONTACTOR_STATUS (int): CONTACTOR_STATUS
    """
    MODULE_ENABLED = 1 << 0
    CONTACTOR_STATUS = 1 << 1



class Model807ModConSt(IntFlag):
    """
    Members:
        CONTACTOR_0 (int): CONTACTOR_0
        CONTACTOR_1 (int): CONTACTOR_1
        CONTACTOR_2 (int): CONTACTOR_2
        CONTACTOR_3 (int): CONTACTOR_3
        CONTACTOR_4 (int): CONTACTOR_4
        CONTACTOR_5 (int): CONTACTOR_5
        CONTACTOR_6 (int): CONTACTOR_6
        CONTACTOR_7 (int): CONTACTOR_7
        CONTACTOR_8 (int): CONTACTOR_8
        CONTACTOR_9 (int): CONTACTOR_9
        CONTACTOR_10 (int): CONTACTOR_10
        CONTACTOR_11 (int): CONTACTOR_11
        CONTACTOR_12 (int): CONTACTOR_12
        CONTACTOR_13 (int): CONTACTOR_13
        CONTACTOR_14 (int): CONTACTOR_14
        CONTACTOR_15 (int): CONTACTOR_15
        CONTACTOR_16 (int): CONTACTOR_16
        CONTACTOR_17 (int): CONTACTOR_17
        CONTACTOR_18 (int): CONTACTOR_18
        CONTACTOR_19 (int): CONTACTOR_19
        CONTACTOR_20 (int): CONTACTOR_20
        CONTACTOR_21 (int): CONTACTOR_21
        CONTACTOR_22 (int): CONTACTOR_22
        CONTACTOR_23 (int): CONTACTOR_23
        CONTACTOR_24 (int): CONTACTOR_24
        CONTACTOR_25 (int): CONTACTOR_25
        CONTACTOR_26 (int): CONTACTOR_26
        CONTACTOR_27 (int): CONTACTOR_27
        CONTACTOR_28 (int): CONTACTOR_28
        CONTACTOR_29 (int): CONTACTOR_29
        CONTACTOR_30 (int): CONTACTOR_30
    """
    CONTACTOR_0 = 1 << 0
    CONTACTOR_1 = 1 << 1
    CONTACTOR_2 = 1 << 2
    CONTACTOR_3 = 1 << 3
    CONTACTOR_4 = 1 << 4
    CONTACTOR_5 = 1 << 5
    CONTACTOR_6 = 1 << 6
    CONTACTOR_7 = 1 << 7
    CONTACTOR_8 = 1 << 8
    CONTACTOR_9 = 1 << 9
    CONTACTOR_10 = 1 << 10
    CONTACTOR_11 = 1 << 11
    CONTACTOR_12 = 1 << 12
    CONTACTOR_13 = 1 << 13
    CONTACTOR_14 = 1 << 14
    CONTACTOR_15 = 1 << 15
    CONTACTOR_16 = 1 << 16
    CONTACTOR_17 = 1 << 17
    CONTACTOR_18 = 1 << 18
    CONTACTOR_19 = 1 << 19
    CONTACTOR_20 = 1 << 20
    CONTACTOR_21 = 1 << 21
    CONTACTOR_22 = 1 << 22
    CONTACTOR_23 = 1 << 23
    CONTACTOR_24 = 1 << 24
    CONTACTOR_25 = 1 << 25
    CONTACTOR_26 = 1 << 26
    CONTACTOR_27 = 1 << 27
    CONTACTOR_28 = 1 << 28
    CONTACTOR_29 = 1 << 29
    CONTACTOR_30 = 1 << 30



class Model807ModEvt1(IntFlag):
    """
    Alarms, warnings and status values.  Bit flags.

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
        RESERVED_1 (int): RESERVED_1
        RESERVED_2 (int): RESERVED_2
        CONTACTOR_ERROR (int): CONTACTOR_ERROR
        FAN_ERROR (int): FAN_ERROR
        GROUND_FAULT (int): GROUND_FAULT
        OPEN_DOOR_ERROR (int): OPEN_DOOR_ERROR
        RESERVED_3 (int): RESERVED_3
        RESERVED_4 (int): RESERVED_4
        RESERVED_5 (int): RESERVED_5
        FIRE_ALARM (int): FIRE_ALARM
        MODULE_CONFIGURATION_ALARM (int): MODULE_CONFIGURATION_ALARM
        MODULE_CONFIGURATION_WARNING (int): MODULE_CONFIGURATION_WARNING
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
    RESERVED_1 = 1 << 18
    RESERVED_2 = 1 << 19
    CONTACTOR_ERROR = 1 << 20
    FAN_ERROR = 1 << 21
    GROUND_FAULT = 1 << 22
    OPEN_DOOR_ERROR = 1 << 23
    RESERVED_3 = 1 << 24
    RESERVED_4 = 1 << 25
    RESERVED_5 = 1 << 26
    FIRE_ALARM = 1 << 27
    MODULE_CONFIGURATION_ALARM = 1 << 28
    MODULE_CONFIGURATION_WARNING = 1 << 29



class Model807ModEvt2(IntFlag):
    """
    Alarms, warnings and status values.  Bit flags.

    Members:
        LEAK_ALARM (int): LEAK_ALARM
        PUMP_ALARM (int): PUMP_ALARM
        HIGH_PRESSURE_ALARM (int): HIGH_PRESSURE_ALARM
        HIGH_PRESSURE_WARNING (int): HIGH_PRESSURE_WARNING
        LOW_FLOW_ALARM (int): LOW_FLOW_ALARM
        LOW_FLOW_WARNING (int): LOW_FLOW_WARNING
    """
    LEAK_ALARM = 1 << 0
    PUMP_ALARM = 1 << 1
    HIGH_PRESSURE_ALARM = 1 << 2
    HIGH_PRESSURE_WARNING = 1 << 3
    LOW_FLOW_ALARM = 1 << 4
    LOW_FLOW_WARNING = 1 << 5



class Model807ModConFail(IntEnum):
    """
    Members:
        NO_FAILURE (int): NO_FAILURE
        BUTTON_PUSHED (int): BUTTON_PUSHED
        MODULE_GROUND_FAULT (int): MODULE_GROUND_FAULT
        OUTSIDE_VOLTAGE_RANGE (int): OUTSIDE_VOLTAGE_RANGE
        MODULE_NOT_ENABLED (int): MODULE_NOT_ENABLED
        FUSE_OPEN (int): FUSE_OPEN
        CONTACTOR_FAILURE (int): CONTACTOR_FAILURE
        PRECHARGE_FAILURE (int): PRECHARGE_FAILURE
        MODULE_FAULT (int): MODULE_FAULT
    """
    NO_FAILURE = 0
    BUTTON_PUSHED = 1
    MODULE_GROUND_FAULT = 2
    OUTSIDE_VOLTAGE_RANGE = 3
    MODULE_NOT_ENABLED = 4
    FUSE_OPEN = 5
    CONTACTOR_FAILURE = 6
    PRECHARGE_FAILURE = 7
    MODULE_FAULT = 8



class Model807ModSetEna(IntEnum):
    """
    Enables and disables the module.

    Members:
        ENABLE_MODULE (int): ENABLE_MODULE
        DISABLE_MODULE (int): DISABLE_MODULE
    """
    ENABLE_MODULE = 1
    DISABLE_MODULE = 2



class Model807ModSetCon(IntEnum):
    """
    Connects and disconnects the module.

    Members:
        CONNECT_MODULE (int): CONNECT_MODULE
        DISCONNECT_MODULE (int): DISCONNECT_MODULE
    """
    CONNECT_MODULE = 1
    DISCONNECT_MODULE = 2



class Model807ModDisRsn(IntEnum):
    """
    Reason why the module is currently disabled.

    Members:
        NONE (int): NONE
        FAULT (int): FAULT
        MAINTENANCE (int): MAINTENANCE
        EXTERNAL (int): EXTERNAL
        OTHER (int): OTHER
    """
    NONE = 0
    FAULT = 1
    MAINTENANCE = 2
    EXTERNAL = 3
    OTHER = 4



class Model807ModuleGroup(SunSpecGroup):
    """
    Attributes:
        ModIdx (int): Index of the module within the string.
        ModNStk (int): Number of stacks in this module.
        ModSt (Model807ModSt): Current status of the module.
        ModSoC (int): State of charge for this module.
        ModOCV (int): Open circuit voltage for this module.
        ModV (int): External voltage fo this module.
        ModCellVMax (int): Maximum voltage for all cells in this module.
        ModCellVMaxCell (int): Cell with the maximum cell voltage.
        ModCellVMin (int): Minimum voltage for all cells in this module.
        ModCellVMinCell (int): Cell with the minimum cell voltage.
        ModCellVAvg (int): Average voltage for all cells in this module.
        ModAnoTmp (int)
        ModCatTmp (int)
        ModConSt (Model807ModConSt)
        ModEvt1 (Model807ModEvt1): Alarms, warnings and status values.  Bit flags.
        ModEvt2 (Model807ModEvt2): Alarms, warnings and status values.  Bit flags.
        ModConFail (Model807ModConFail)
        ModSetEna (Model807ModSetEna): Enables and disables the module.
        ModSetCon (Model807ModSetCon): Connects and disconnects the module.
        ModDisRsn (Model807ModDisRsn): Reason why the module is currently disabled.
    """

    ModIdx: Annotated[int, ("SunSpecPoint", {'name': 'ModIdx', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModNStk: Annotated[int, ("SunSpecPoint", {'name': 'ModNStk', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModSt: Annotated[int, ("SunSpecPoint", {'name': 'ModSt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    ModSoC: Annotated[int, ("SunSpecPoint", {'name': 'ModSoC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: SoC_SF
    ModOCV: Annotated[int, ("SunSpecPoint", {'name': 'ModOCV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: OCV_SF
    ModV: Annotated[int, ("SunSpecPoint", {'name': 'ModV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: ModV_SF
    ModCellVMax: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    ModCellVMaxCell: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMaxCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModCellVMin: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMin', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    ModCellVMinCell: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMinCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModCellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVAvg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    ModAnoTmp: Annotated[int, ("SunSpecPoint", {'name': 'ModAnoTmp', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    ModCatTmp: Annotated[int, ("SunSpecPoint", {'name': 'ModCatTmp', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    ModConSt: Annotated[int, ("SunSpecPoint", {'name': 'ModConSt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    ModEvt1: Annotated[int, ("SunSpecPoint", {'name': 'ModEvt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    ModEvt2: Annotated[int, ("SunSpecPoint", {'name': 'ModEvt2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    ModConFail: Annotated[int, ("SunSpecPoint", {'name': 'ModConFail', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModSetEna: Annotated[int, ("SunSpecPoint", {'name': 'ModSetEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ModSetCon: Annotated[int, ("SunSpecPoint", {'name': 'ModSetCon', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ModDisRsn: Annotated[int, ("SunSpecPoint", {'name': 'ModDisRsn', 'ptype': 'uint16', 'mandatory': False, 'static': False})]


class Model807Evt1(IntFlag):
    """
    Alarms, warnings and status values.  Bit flags.

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
        RESERVED_1 (int): RESERVED_1
        RESERVED_2 (int): RESERVED_2
        CONTACTOR_ERROR (int): CONTACTOR_ERROR
        FAN_ERROR (int): FAN_ERROR
        GROUND_FAULT (int): GROUND_FAULT
        OPEN_DOOR_ERROR (int): OPEN_DOOR_ERROR
        RESERVED_3 (int): RESERVED_3
        OTHER_ALARM (int): OTHER_ALARM
        OTHER_WARNING (int): OTHER_WARNING
        FIRE_ALARM (int): FIRE_ALARM
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
    RESERVED_1 = 1 << 18
    RESERVED_2 = 1 << 19
    CONTACTOR_ERROR = 1 << 20
    FAN_ERROR = 1 << 21
    GROUND_FAULT = 1 << 22
    OPEN_DOOR_ERROR = 1 << 23
    RESERVED_3 = 1 << 24
    OTHER_ALARM = 1 << 25
    OTHER_WARNING = 1 << 26
    FIRE_ALARM = 1 << 27
    CONFIGURATION_ALARM = 1 << 28
    CONFIGURATION_WARNING = 1 << 29



class Model807Evt2(IntFlag):
    """
    Alarms, warnings and status values.  Bit flags.

    Members:
        LEAK_ALARM (int): LEAK_ALARM
        PUMP_ALARM (int): PUMP_ALARM
        HIGH_PRESSURE_ALARM (int): HIGH_PRESSURE_ALARM
        HIGH_PRESSURE_WARNING (int): HIGH_PRESSURE_WARNING
        LOW_FLOW_ALARM (int): LOW_FLOW_ALARM
        LOW_FLOW_WARNING (int): LOW_FLOW_WARNING
    """
    LEAK_ALARM = 1 << 0
    PUMP_ALARM = 1 << 1
    HIGH_PRESSURE_ALARM = 1 << 2
    HIGH_PRESSURE_WARNING = 1 << 3
    LOW_FLOW_ALARM = 1 << 4
    LOW_FLOW_WARNING = 1 << 5



class Model807(SunSpecModel, model_name="flow_battery_string", id=807):
    """
    Attributes:
        Idx (int): Index of the string within the bank.
        NMod (int): Number of modules in this string.
        NModCon (int): Number of electrically connected modules in this string.
        ModVMax (int): Maximum voltage for all modules in the string.
        ModVMaxMod (int): Module with the maximum voltage.
        ModVMin (int): Minimum voltage for all modules in the string.
        ModVMinMod (int): Module with the minimum voltage.
        ModVAvg (int): Average voltage for all modules in the string.
        CellVMax (int): Maximum voltage for all cells in the string.
        CellVMaxMod (int): Module containing the cell with the maximum voltage.
        CellVMaxStk (int): Stack containing the cell with the maximum voltage.
        CellVMin (int): Minimum voltage for all cells in the string.
        CellVMinMod (int): Module containing the cell with the minimum voltage.
        CellVMinStk (int): Stack containing the cell with the minimum voltage.
        CellVAvg (int): Average voltage for all cells in the string.
        TmpMax (int): Maximum electrolyte temperature for all modules in the string.
        TmpMaxMod (int): Module with the maximum temperature.
        TmpMin (int): Minimum electrolyte temperature for all modules in the string.
        TmpMinMod (int): Module with the minimum temperature.
        TmpAvg (int): Average electrolyte temperature for all modules in the string.
        Evt1 (Model807Evt1): Alarms, warnings and status values.  Bit flags.
        Evt2 (Model807Evt2): Alarms, warnings and status values.  Bit flags.
        EvtVnd1 (int): Vendor defined events.
        EvtVnd2 (int): Vendor defined events.
        ModV_SF (int)
        CellV_SF (int): Scale factor for voltage.
        Tmp_SF (int): Scale factor for temperature.
        SoC_SF (int): Scale factor for state of charge.
        OCV_SF (int): Scale factor for open circuit voltage.
        Pad1 (int): Pad register.
    """

    Idx: Annotated[int, ("SunSpecPoint", {'name': 'Idx', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NMod: Annotated[int, ("SunSpecPoint", {'name': 'NMod', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NModCon: Annotated[int, ("SunSpecPoint", {'name': 'NModCon', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModVMax: Annotated[int, ("SunSpecPoint", {'name': 'ModVMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: ModV_SF
    ModVMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'ModVMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModVMin: Annotated[int, ("SunSpecPoint", {'name': 'ModVMin', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: ModV_SF
    ModVMinMod: Annotated[int, ("SunSpecPoint", {'name': 'ModVMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModVAvg: Annotated[int, ("SunSpecPoint", {'name': 'ModVAvg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: ModV_SF
    CellVMax: Annotated[int, ("SunSpecPoint", {'name': 'CellVMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    CellVMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'CellVMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMaxStk: Annotated[int, ("SunSpecPoint", {'name': 'CellVMaxStk', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMin: Annotated[int, ("SunSpecPoint", {'name': 'CellVMin', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    CellVMinMod: Annotated[int, ("SunSpecPoint", {'name': 'CellVMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMinStk: Annotated[int, ("SunSpecPoint", {'name': 'CellVMinStk', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'CellVAvg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: CellV_SF
    TmpMax: Annotated[int, ("SunSpecPoint", {'name': 'TmpMax', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    TmpMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'TmpMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    TmpMin: Annotated[int, ("SunSpecPoint", {'name': 'TmpMin', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    TmpMinMod: Annotated[int, ("SunSpecPoint", {'name': 'TmpMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    TmpAvg: Annotated[int, ("SunSpecPoint", {'name': 'TmpAvg', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    Evt1: Annotated[int, ("SunSpecPoint", {'name': 'Evt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Evt2: Annotated[int, ("SunSpecPoint", {'name': 'Evt2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd1: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    EvtVnd2: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd2', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    ModV_SF: Annotated[int, ("SunSpecPoint", {'name': 'ModV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    CellV_SF: Annotated[int, ("SunSpecPoint", {'name': 'CellV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Tmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tmp_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    SoC_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoC_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    OCV_SF: Annotated[int, ("SunSpecPoint", {'name': 'OCV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Pad1: Annotated[int, ("SunSpecPoint", {'name': 'Pad1', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    module: Annotated[Model807ModuleGroup, ("SunSpecGroup", {"name": "module", "group_type": Model807ModuleGroup})]

