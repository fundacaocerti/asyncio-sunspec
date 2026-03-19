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


class Model804LithiumIonStringModuleGroup(SunSpecGroup):
    """
    Attributes:
        ModNCell (int): Count of all cells in the module.
        ModSoC (int): Module state of charge, expressed as a percentage.
        ModSoH (int): Module state of health, expressed as a percentage.
        ModCellVMax (int): Maximum voltage for all cells in the module.
        ModCellVMaxCell (int): Cell with maximum voltage.
        ModCellVMin (int): Minimum voltage for all cells in the module.
        ModCellVMinCell (int): Cell with minimum voltage.
        ModCellVAvg (int): Average voltage for all cells in the module.
        ModCellTmpMax (int): Maximum temperature for all cells in the module.
        ModCellTmpMaxCell (int): Cell with maximum temperature.
        ModCellTmpMin (int): Minimum temperature for all cells in the module.
        ModCellTmpMinCell (int): Cell with minimum temperature.
        ModCellTmpAvg (int): Average temperature for all cells in the module.
        Pad5 (int): Pad register.
        Pad6 (int): Pad register.
        Pad7 (int): Pad register.
    """

    ModNCell: Annotated[int, ("SunSpecPoint", {'name': 'ModNCell', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModSoC: Annotated[int, ("SunSpecPoint", {'name': 'ModSoC', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoC_SF
    ModSoH: Annotated[int, ("SunSpecPoint", {'name': 'ModSoH', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoH_SF
    ModCellVMax: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    ModCellVMaxCell: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMaxCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModCellVMin: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMin', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    ModCellVMinCell: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVMinCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModCellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'ModCellVAvg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    ModCellTmpMax: Annotated[int, ("SunSpecPoint", {'name': 'ModCellTmpMax', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    ModCellTmpMaxCell: Annotated[int, ("SunSpecPoint", {'name': 'ModCellTmpMaxCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModCellTmpMin: Annotated[int, ("SunSpecPoint", {'name': 'ModCellTmpMin', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    ModCellTmpMinCell: Annotated[int, ("SunSpecPoint", {'name': 'ModCellTmpMinCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModCellTmpAvg: Annotated[int, ("SunSpecPoint", {'name': 'ModCellTmpAvg', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    Pad5: Annotated[int, ("SunSpecPoint", {'name': 'Pad5', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad6: Annotated[int, ("SunSpecPoint", {'name': 'Pad6', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad7: Annotated[int, ("SunSpecPoint", {'name': 'Pad7', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model804St(IntFlag):
    """
    Current status of the string.

    Members:
        STRING_ENABLED (int): STRING_ENABLED
        CONTACTOR_STATUS (int): CONTACTOR_STATUS
    """
    STRING_ENABLED = 1 << 0
    CONTACTOR_STATUS = 1 << 1



class Model804ConFail(IntEnum):
    """
    Members:
        NO_FAILURE (int): NO_FAILURE
        BUTTON_PUSHED (int): BUTTON_PUSHED
        STR_GROUND_FAULT (int): STR_GROUND_FAULT
        OUTSIDE_VOLTAGE_RANGE (int): OUTSIDE_VOLTAGE_RANGE
        STRING_NOT_ENABLED (int): STRING_NOT_ENABLED
        FUSE_OPEN (int): FUSE_OPEN
        CONTACTOR_FAILURE (int): CONTACTOR_FAILURE
        PRECHARGE_FAILURE (int): PRECHARGE_FAILURE
        STRING_FAULT (int): STRING_FAULT
    """
    NO_FAILURE = 0
    BUTTON_PUSHED = 1
    STR_GROUND_FAULT = 2
    OUTSIDE_VOLTAGE_RANGE = 3
    STRING_NOT_ENABLED = 4
    FUSE_OPEN = 5
    CONTACTOR_FAILURE = 6
    PRECHARGE_FAILURE = 7
    STRING_FAULT = 8



class Model804ConSt(IntFlag):
    """
    Status of the contactor(s) for the string.

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



class Model804Evt1(IntFlag):
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
        TEMPERATURE_IMBALANCE_ALARM (int): TEMPERATURE_IMBALANCE_ALARM
        TEMPERATURE_IMBALANCE_WARNING (int): TEMPERATURE_IMBALANCE_WARNING
        CONTACTOR_ERROR (int): CONTACTOR_ERROR
        FAN_ERROR (int): FAN_ERROR
        GROUND_FAULT (int): GROUND_FAULT
        OPEN_DOOR_ERROR (int): OPEN_DOOR_ERROR
        RESERVED_1 (int): RESERVED_1
        OTHER_ALARM (int): OTHER_ALARM
        OTHER_WARNING (int): OTHER_WARNING
        RESERVED_2 (int): RESERVED_2
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
    RESERVED_1 = 1 << 24
    OTHER_ALARM = 1 << 25
    OTHER_WARNING = 1 << 26
    RESERVED_2 = 1 << 27
    CONFIGURATION_ALARM = 1 << 28
    CONFIGURATION_WARNING = 1 << 29



class Model804SetCon(IntEnum):
    """
    Connects and disconnects the string.

    Members:
        CONNECT_STRING (int): CONNECT_STRING
        DISCONNECT_STRING (int): DISCONNECT_STRING
    """
    CONNECT_STRING = 1
    DISCONNECT_STRING = 2



class Model804(SunSpecModel, model_name="lithium_ion_string", id=804):
    """
    Attributes:
        Idx (int): Index of the string within the bank.
        NMod (int): Count of modules in the string.
        St (Model804St): Current status of the string.
        ConFail (Model804ConFail)
        NCellBal (int): Number of cells currently being balanced in the string.
        SoC (int): Battery string state of charge, expressed as a percentage.
        DoD (int): Depth of discharge for the string, expressed as a percentage.
        NCyc (int): Number of discharge cycles executed upon the string.
        SoH (int): Battery string state of health, expressed as a percentage.
        A (int): String current measurement.
        V (int): String voltage measurement.
        CellVMax (int): Maximum voltage for all cells in the string.
        CellVMaxMod (int): Module containing the cell with maximum cell voltage.
        CellVMin (int): Minimum voltage for all cells in the string.
        CellVMinMod (int): Module containing the cell with minimum cell voltage.
        CellVAvg (int): Average voltage for all cells in the string.
        ModTmpMax (int): Maximum temperature for all modules in the string.
        ModTmpMaxMod (int): Module with the maximum temperature.
        ModTmpMin (int): Minimum temperature for all modules in the string.
        ModTmpMinMod (int): Module with the minimum temperature.
        ModTmpAvg (int): Average temperature for all modules in the string.
        Pad1 (int): Pad register.
        ConSt (Model804ConSt): Status of the contactor(s) for the string.
        Evt1 (Model804Evt1): Alarms, warnings and status values.  Bit flags.
        Evt2 (int): Alarms, warnings and status values.  Bit flags.
        EvtVnd1 (int): Vendor defined events.
        EvtVnd2 (int): Vendor defined events.
        SetEna (int): Enables and disables the string.  Should reset to 0 upon completion.
        SetCon (Model804SetCon): Connects and disconnects the string.
        SoC_SF (int): Scale factor for string state of charge.
        SoH_SF (int): Scale factor for string state of health.
        DoD_SF (int): Scale factor for string depth of discharge.
        A_SF (int): Scale factor for string current.
        V_SF (int): Scale factor for string voltage.
        CellV_SF (int): Scale factor for cell voltage.
        ModTmp_SF (int): Scale factor for module temperature.
        Pad2 (int): Pad register.
        Pad3 (int): Pad register.
        Pad4 (int): Pad register.
    """

    Idx: Annotated[int, ("SunSpecPoint", {'name': 'Idx', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NMod: Annotated[int, ("SunSpecPoint", {'name': 'NMod', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    St: Annotated[int, ("SunSpecPoint", {'name': 'St', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    ConFail: Annotated[int, ("SunSpecPoint", {'name': 'ConFail', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    NCellBal: Annotated[int, ("SunSpecPoint", {'name': 'NCellBal', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    SoC: Annotated[int, ("SunSpecPoint", {'name': 'SoC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: SoC_SF
    DoD: Annotated[int, ("SunSpecPoint", {'name': 'DoD', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DoD_SF
    NCyc: Annotated[int, ("SunSpecPoint", {'name': 'NCyc', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    SoH: Annotated[int, ("SunSpecPoint", {'name': 'SoH', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoH_SF
    A: Annotated[int, ("SunSpecPoint", {'name': 'A', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    CellVMax: Annotated[int, ("SunSpecPoint", {'name': 'CellVMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    CellVMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'CellVMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMin: Annotated[int, ("SunSpecPoint", {'name': 'CellVMin', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    CellVMinMod: Annotated[int, ("SunSpecPoint", {'name': 'CellVMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'CellVAvg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    ModTmpMax: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMax', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    ModTmpMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMaxMod', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModTmpMin: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMin', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    ModTmpMinMod: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMinMod', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModTmpAvg: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpAvg', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    Pad1: Annotated[int, ("SunSpecPoint", {'name': 'Pad1', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ConSt: Annotated[int, ("SunSpecPoint", {'name': 'ConSt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    Evt1: Annotated[int, ("SunSpecPoint", {'name': 'Evt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    Evt2: Annotated[int, ("SunSpecPoint", {'name': 'Evt2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd1: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    EvtVnd2: Annotated[int, ("SunSpecPoint", {'name': 'EvtVnd2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    SetEna: Annotated[int, ("SunSpecPoint", {'name': 'SetEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SetCon: Annotated[int, ("SunSpecPoint", {'name': 'SetCon', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SoC_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoC_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    SoH_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DoD_SF: Annotated[int, ("SunSpecPoint", {'name': 'DoD_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    CellV_SF: Annotated[int, ("SunSpecPoint", {'name': 'CellV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    ModTmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'ModTmp_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Pad2: Annotated[int, ("SunSpecPoint", {'name': 'Pad2', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad3: Annotated[int, ("SunSpecPoint", {'name': 'Pad3', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad4: Annotated[int, ("SunSpecPoint", {'name': 'Pad4', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    lithium_ion_string_module: Annotated[SunSpecRepeatingBlock[Model804LithiumIonStringModuleGroup], ("SunSpecRepeatingBlock", {"name": "lithium_ion_string_module", "ptype": "group", "group_type": Model804LithiumIonStringModuleGroup, "counter": "NMod"})]

