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


class Model64020RepeatingGroup(SunSpecGroup):
    """
    Attributes:
        SerialNumber (str): strings of 16 characters
        Firmware (str): string of 11 characters
        Hardware (int)
    """

    SerialNumber: Annotated[str, ("SunSpecPoint", {'name': 'SerialNumber', 'ptype': 'string', 'size': 9, 'mandatory': True, 'static': False})]
    Firmware: Annotated[str, ("SunSpecPoint", {'name': 'Firmware', 'ptype': 'string', 'size': 6, 'mandatory': True, 'static': False})]
    Hardware: Annotated[int, ("SunSpecPoint", {'name': 'Hardware', 'ptype': 'uint16', 'mandatory': True, 'static': False})]


class Model64020(SunSpecModel, model_name="model_64020", id=64020):
    """
    Attributes:
        Aux0Tmp (int)
        Aux1Tmp (int)
        Aux2Tmp (int)
        Aux3Tmp (int)
        Aux4Tmp (int)
        ProbeTmp (int)
        MainTmp (int)
        SensorV_SF (int)
        SensorA_SF (int)
        SensorHz_SF (int)
        Sensor1Voltage (int): scale of 0-10V
        Sensor2Voltage (int): scale of 0-10V
        Sensor3Voltage (int): scale of 0-10V
        Sensor4Voltage (int): scale of 0-10V
        Sensor5Voltage (int): scale of 0-10V
        Sensor6Voltage (int): scale of 0-10V
        Sensor7Voltage (int): scale of 0-10V
        Sensor1Current (int): scale of 4-20mA
        Sensor2Current (int): in 4-20mA or 4-20mA
        Sensor3Current (int): in 4-20mA or 4-20mA
        Sensor4Current (int): in 4-20mA or 4-20mA
        Sensor5Current (int): in 4-20mA or 4-20mA
        Sensor6Current (int): in 4-20mA or 4-20mA
        Sensor7Current (int): in 4-20mA or 4-20mA
        Sensor8 (int): frequency in Hz
        Relay1 (int)
        Relay2 (int)
        Relay3 (int)
        ResetAccumulators (int): always 0 in reading, used the code 0xC0DA during the writing for resetting them
        Reset (int): always 0 in reading, used the code 0xC0DA during the writing for resetting the system
    """

    Aux0Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Aux0Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Aux1Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Aux1Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Aux2Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Aux2Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Aux3Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Aux3Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    Aux4Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Aux4Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]
    ProbeTmp: Annotated[int, ("SunSpecPoint", {'name': 'ProbeTmp', 'ptype': 'int16', 'mandatory': True, 'static': False})]
    MainTmp: Annotated[int, ("SunSpecPoint", {'name': 'MainTmp', 'ptype': 'int16', 'mandatory': True, 'static': False})]
    SensorV_SF: Annotated[int, ("SunSpecPoint", {'name': 'SensorV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    SensorA_SF: Annotated[int, ("SunSpecPoint", {'name': 'SensorA_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    SensorHz_SF: Annotated[int, ("SunSpecPoint", {'name': 'SensorHz_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Sensor1Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor1Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor2Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor2Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor3Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor3Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor4Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor4Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor5Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor5Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor6Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor6Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor7Voltage: Annotated[int, ("SunSpecPoint", {'name': 'Sensor7Voltage', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorV_SF
    Sensor1Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor1Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor2Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor2Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor3Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor3Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor4Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor4Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor5Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor5Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor6Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor6Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor7Current: Annotated[int, ("SunSpecPoint", {'name': 'Sensor7Current', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: SensorA_SF
    Sensor8: Annotated[int, ("SunSpecPoint", {'name': 'Sensor8', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SensorHz_SF
    Relay1: Annotated[int, ("SunSpecPoint", {'name': 'Relay1', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Relay2: Annotated[int, ("SunSpecPoint", {'name': 'Relay2', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Relay3: Annotated[int, ("SunSpecPoint", {'name': 'Relay3', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ResetAccumulators: Annotated[int, ("SunSpecPoint", {'name': 'ResetAccumulators', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Reset: Annotated[int, ("SunSpecPoint", {'name': 'Reset', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    repeating: Annotated[Model64020RepeatingGroup, ("SunSpecGroup", {"name": "repeating", "group_type": Model64020RepeatingGroup})]

