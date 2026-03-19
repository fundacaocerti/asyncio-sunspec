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


class Model127HysEna(IntFlag):
    """
    Enable hysteresis

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model127ModEna(IntFlag):
    """
    Is Parameterized Frequency-Watt control active.

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model127(SunSpecModel, model_name="freq_watt_param", id=127):
    """
    Parameterized Frequency-Watt 

    Attributes:
        WGra (int): The slope of the reduction in the maximum allowed watts output as a function of frequency.
        HzStr (int): The frequency deviation from nominal frequency (ECPNomHz) at which a snapshot of the instantaneous power output is taken to act as the CAPPED power level (PM) and above which reduction in power output occurs.
        HzStop (int): The frequency deviation from nominal frequency (ECPNomHz) at which curtailed power output may return to normal and the cap on the power level value is removed.
        HysEna (Model127HysEna): Enable hysteresis
        ModEna (Model127ModEna): Is Parameterized Frequency-Watt control active.
        HzStopWGra (int): The maximum time-based rate of change at which power output returns to normal after having been capped by an over frequency event.
        WGra_SF (int): Scale factor for output gradient.
        HzStrStop_SF (int): Scale factor for frequency deviations.
        RmpIncDec_SF (int): Scale factor for increment and decrement ramps.
        Pad (int)
    """

    WGra: Annotated[int, ("SunSpecPoint", {'name': 'WGra', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: WGra_SF
    HzStr: Annotated[int, ("SunSpecPoint", {'name': 'HzStr', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: HzStrStop_SF
    HzStop: Annotated[int, ("SunSpecPoint", {'name': 'HzStop', 'ptype': 'int16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: HzStrStop_SF
    HysEna: Annotated[int, ("SunSpecPoint", {'name': 'HysEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    HzStopWGra: Annotated[int, ("SunSpecPoint", {'name': 'HzStopWGra', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RmpIncDec_SF
    WGra_SF: Annotated[int, ("SunSpecPoint", {'name': 'WGra_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    HzStrStop_SF: Annotated[int, ("SunSpecPoint", {'name': 'HzStrStop_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    RmpIncDec_SF: Annotated[int, ("SunSpecPoint", {'name': 'RmpIncDec_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

