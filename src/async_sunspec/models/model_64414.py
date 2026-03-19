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


class Model64414(SunSpecModel, model_name="DERSimControls", id=64414):
    """
    Configuration parameters for the DER device simulator.

    Attributes:
        Time (str): Time offset for simulation formatted 'HH:MM:SS'
        Temperature (float): Ambient temperature (degrees Celsius)
        GridModelSource (str): The data source for the grid model. 'csv' or 'const'
        IrradianceModelSource (str): The data source for the irradiance model. 'csv' or 'const'
        Irradiance (float): The irradiance on the DER device (W/m^2) for the 'const' irradiance model
        GridVoltageA (float): Phase A RMS Voltage (pu) for the 'const' grid model
        GridVoltageB (float): Phase B RMS Voltage (pu) for the 'const' grid model
        GridVoltageC (float): Phase C RMS Voltage (pu) for the 'const' grid model
        GridFrequency (float): Grid frequency (Hz) for the 'const' grid model
    """

    Time: Annotated[str, ("SunSpecPoint", {'name': 'Time', 'ptype': 'string', 'size': 10, 'mandatory': False, 'static': False})]
    Temperature: Annotated[float, ("SunSpecPoint", {'name': 'Temperature', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    GridModelSource: Annotated[str, ("SunSpecPoint", {'name': 'GridModelSource', 'ptype': 'string', 'size': 32, 'mandatory': False, 'static': False, 'access': 'RW'})]
    IrradianceModelSource: Annotated[str, ("SunSpecPoint", {'name': 'IrradianceModelSource', 'ptype': 'string', 'size': 32, 'mandatory': False, 'static': False, 'access': 'RW'})]
    Irradiance: Annotated[float, ("SunSpecPoint", {'name': 'Irradiance', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    GridVoltageA: Annotated[float, ("SunSpecPoint", {'name': 'GridVoltageA', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    GridVoltageB: Annotated[float, ("SunSpecPoint", {'name': 'GridVoltageB', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    GridVoltageC: Annotated[float, ("SunSpecPoint", {'name': 'GridVoltageC', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    GridFrequency: Annotated[float, ("SunSpecPoint", {'name': 'GridFrequency', 'ptype': 'float32', 'mandatory': False, 'static': False, 'access': 'RW'})]

