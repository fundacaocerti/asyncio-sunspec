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


class Model803StrSt(IntFlag):
    """
    Current status of the string.

    Members:
        STRING_ENABLED (int): STRING_ENABLED
        CONTACTOR_STATUS (int): CONTACTOR_STATUS
    """
    STRING_ENABLED = 1 << 0
    CONTACTOR_STATUS = 1 << 1



class Model803StrConFail(IntEnum):
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



class Model803StrDisRsn(IntEnum):
    """
    Reason why the string is currently disabled.

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



class Model803StrConSt(IntFlag):
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



class Model803StrEvt1(IntFlag):
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



class Model803StrSetEna(IntEnum):
    """
    Enables and disables the string.

    Members:
        ENABLE_STRING (int): ENABLE_STRING
        DISABLE_STRING (int): DISABLE_STRING
    """
    ENABLE_STRING = 1
    DISABLE_STRING = 2



class Model803StrSetCon(IntEnum):
    """
    Connects and disconnects the string.

    Members:
        CONNECT_STRING (int): CONNECT_STRING
        DISCONNECT_STRING (int): DISCONNECT_STRING
    """
    CONNECT_STRING = 1
    DISCONNECT_STRING = 2



class Model803StringGroup(SunSpecGroup):
    """
    Attributes:
        StrNMod (int): Count of modules in the string.
        StrSt (Model803StrSt): Current status of the string.
        StrConFail (Model803StrConFail)
        StrSoC (int): Battery string state of charge, expressed as a percentage.
        StrSoH (int): Battery string state of health, expressed as a percentage.
        StrA (int): String current measurement.
        StrCellVMax (int): Maximum voltage for all cells in the string.
        StrCellVMaxMod (int): Module containing the maximum cell voltage.
        StrCellVMin (int): Minimum voltage for all cells in the string.
        StrCellVMinMod (int): Module containing the minimum cell voltage.
        StrCellVAvg (int): Average voltage for all cells in the string.
        StrModTmpMax (int): Maximum temperature for all modules in the bank.
        StrModTmpMaxMod (int): Module with the maximum temperature.
        StrModTmpMin (int): Minimum temperature for all modules in the bank.
        StrModTmpMinMod (int): Module with the minimum temperature.
        StrModTmpAvg (int): Average temperature for all modules in the bank.
        StrDisRsn (Model803StrDisRsn): Reason why the string is currently disabled.
        StrConSt (Model803StrConSt): Status of the contactor(s) for the string.
        StrEvt1 (Model803StrEvt1): Alarms, warnings and status values.  Bit flags.
        StrEvt2 (int): Alarms, warnings and status values.  Bit flags.
        StrEvtVnd1 (int): Vendor defined events.
        StrEvtVnd2 (int): Vendor defined events.
        StrSetEna (Model803StrSetEna): Enables and disables the string.
        StrSetCon (Model803StrSetCon): Connects and disconnects the string.
        Pad1 (int): Pad register.
        Pad2 (int): Pad register.
    """

    StrNMod: Annotated[int, ("SunSpecPoint", {'name': 'StrNMod', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    StrSt: Annotated[int, ("SunSpecPoint", {'name': 'StrSt', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    StrConFail: Annotated[int, ("SunSpecPoint", {'name': 'StrConFail', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrSoC: Annotated[int, ("SunSpecPoint", {'name': 'StrSoC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: SoC_SF
    StrSoH: Annotated[int, ("SunSpecPoint", {'name': 'StrSoH', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoH_SF
    StrA: Annotated[int, ("SunSpecPoint", {'name': 'StrA', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: A_SF
    StrCellVMax: Annotated[int, ("SunSpecPoint", {'name': 'StrCellVMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    StrCellVMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'StrCellVMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrCellVMin: Annotated[int, ("SunSpecPoint", {'name': 'StrCellVMin', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    StrCellVMinMod: Annotated[int, ("SunSpecPoint", {'name': 'StrCellVMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrCellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'StrCellVAvg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    StrModTmpMax: Annotated[int, ("SunSpecPoint", {'name': 'StrModTmpMax', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    StrModTmpMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'StrModTmpMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrModTmpMin: Annotated[int, ("SunSpecPoint", {'name': 'StrModTmpMin', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    StrModTmpMinMod: Annotated[int, ("SunSpecPoint", {'name': 'StrModTmpMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrModTmpAvg: Annotated[int, ("SunSpecPoint", {'name': 'StrModTmpAvg', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    StrDisRsn: Annotated[int, ("SunSpecPoint", {'name': 'StrDisRsn', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrConSt: Annotated[int, ("SunSpecPoint", {'name': 'StrConSt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    StrEvt1: Annotated[int, ("SunSpecPoint", {'name': 'StrEvt1', 'ptype': 'uint32', 'mandatory': True, 'static': False})]
    StrEvt2: Annotated[int, ("SunSpecPoint", {'name': 'StrEvt2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    StrEvtVnd1: Annotated[int, ("SunSpecPoint", {'name': 'StrEvtVnd1', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    StrEvtVnd2: Annotated[int, ("SunSpecPoint", {'name': 'StrEvtVnd2', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    StrSetEna: Annotated[int, ("SunSpecPoint", {'name': 'StrSetEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    StrSetCon: Annotated[int, ("SunSpecPoint", {'name': 'StrSetCon', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pad1: Annotated[int, ("SunSpecPoint", {'name': 'Pad1', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    Pad2: Annotated[int, ("SunSpecPoint", {'name': 'Pad2', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model803(SunSpecModel, model_name="lithium_ion_bank", id=803):
    """
    Attributes:
        NStr (int): Number of strings in the bank.
        NStrCon (int): Number of strings with contactor closed.
        ModTmpMax (int): Maximum temperature for all modules in the bank.
        ModTmpMaxStr (int): String containing the module with maximum temperature.
        ModTmpMaxMod (int): Module with maximum temperature.
        ModTmpMin (int): Minimum temperature for all modules in the bank.
        ModTmpMinStr (int): String containing the module with minimum temperature.
        ModTmpMinMod (int): Module with minimum temperature.
        ModTmpAvg (int): Average temperature for all modules in the bank.
        StrVMax (int): Maximum string voltage for all strings in the bank.
        StrVMaxStr (int): String with maximum voltage.
        StrVMin (int): Minimum string voltage for all strings in the bank.
        StrVMinStr (int): String with minimum voltage.
        StrVAvg (int): Average string voltage for all strings in the bank.
        StrAMax (int): Maximum current of any string in the bank.
        StrAMaxStr (int): String with the maximum current.
        StrAMin (int): Minimum current of any string in the bank.
        StrAMinStr (int): String with the minimum current.
        StrAAvg (int): Average string current for all strings in the bank.
        NCellBal (int): Total number of cells that are currently being balanced.
        CellV_SF (int): Scale factor for cell voltage.
        ModTmp_SF (int): Scale factor for module temperatures.
        A_SF (int): Scale factor for string currents.
        SoH_SF (int): Scale factor for string state of health.
        SoC_SF (int): Scale factor for string state of charge.
        V_SF (int): Scale factor for string voltage.
    """

    NStr: Annotated[int, ("SunSpecPoint", {'name': 'NStr', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NStrCon: Annotated[int, ("SunSpecPoint", {'name': 'NStrCon', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModTmpMax: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMax', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    ModTmpMaxStr: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMaxStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModTmpMaxMod: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMaxMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModTmpMin: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMin', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: ModTmp_SF
    ModTmpMinStr: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMinStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModTmpMinMod: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpMinMod', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ModTmpAvg: Annotated[int, ("SunSpecPoint", {'name': 'ModTmpAvg', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: ModTmp_SF
    StrVMax: Annotated[int, ("SunSpecPoint", {'name': 'StrVMax', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    StrVMaxStr: Annotated[int, ("SunSpecPoint", {'name': 'StrVMaxStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrVMin: Annotated[int, ("SunSpecPoint", {'name': 'StrVMin', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    StrVMinStr: Annotated[int, ("SunSpecPoint", {'name': 'StrVMinStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrVAvg: Annotated[int, ("SunSpecPoint", {'name': 'StrVAvg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    StrAMax: Annotated[int, ("SunSpecPoint", {'name': 'StrAMax', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    StrAMaxStr: Annotated[int, ("SunSpecPoint", {'name': 'StrAMaxStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrAMin: Annotated[int, ("SunSpecPoint", {'name': 'StrAMin', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    StrAMinStr: Annotated[int, ("SunSpecPoint", {'name': 'StrAMinStr', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    StrAAvg: Annotated[int, ("SunSpecPoint", {'name': 'StrAAvg', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: A_SF
    NCellBal: Annotated[int, ("SunSpecPoint", {'name': 'NCellBal', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellV_SF: Annotated[int, ("SunSpecPoint", {'name': 'CellV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    ModTmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'ModTmp_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    A_SF: Annotated[int, ("SunSpecPoint", {'name': 'A_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    SoH_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    SoC_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoC_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    string: Annotated[SunSpecRepeatingBlock[Model803StringGroup], ("SunSpecRepeatingBlock", {"name": "string", "ptype": "group", "group_type": Model803StringGroup, "counter": "NStr"})]

