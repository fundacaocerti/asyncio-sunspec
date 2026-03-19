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


class Model120DERTyp(IntEnum):
    """
    Type of DER device. Default value is 4 to indicate PV device.

    Members:
        PV (int): PV
        PV_STOR (int): PV_STOR
    """
    PV = 4
    PV_STOR = 82



class Model120(SunSpecModel, model_name="nameplate", id=120):
    """
    Inverter Controls Nameplate Ratings 

    Attributes:
        DERTyp (Model120DERTyp): Type of DER device. Default value is 4 to indicate PV device.
        WRtg (int): Continuous power output capability of the inverter.
        WRtg_SF (int): Scale factor
        VARtg (int): Continuous Volt-Ampere capability of the inverter.
        VARtg_SF (int): Scale factor
        VArRtgQ1 (int): Continuous VAR capability of the inverter in quadrant 1.
        VArRtgQ2 (int): Continuous VAR capability of the inverter in quadrant 2.
        VArRtgQ3 (int): Continuous VAR capability of the inverter in quadrant 3.
        VArRtgQ4 (int): Continuous VAR capability of the inverter in quadrant 4.
        VArRtg_SF (int): Scale factor
        ARtg (int): Maximum RMS AC current level capability of the inverter.
        ARtg_SF (int): Scale factor
        PFRtgQ1 (int): Minimum power factor capability of the inverter in quadrant 1.
        PFRtgQ2 (int): Minimum power factor capability of the inverter in quadrant 2.
        PFRtgQ3 (int): Minimum power factor capability of the inverter in quadrant 3.
        PFRtgQ4 (int): Minimum power factor capability of the inverter in quadrant 4.
        PFRtg_SF (int): Scale factor
        WHRtg (int): Nominal energy rating of storage device.
        WHRtg_SF (int): Scale factor
        AhrRtg (int): The usable capacity of the battery.  Maximum charge minus minimum charge from a technology capability perspective (Amp-hour capacity rating).
        AhrRtg_SF (int): Scale factor for amp-hour rating.
        MaxChaRte (int): Maximum rate of energy transfer into the storage device.
        MaxChaRte_SF (int): Scale factor
        MaxDisChaRte (int): Maximum rate of energy transfer out of the storage device.
        MaxDisChaRte_SF (int): Scale factor
        Pad (int): Pad register.
    """

    DERTyp: Annotated[int, ("SunSpecPoint", {'name': 'DERTyp', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    WRtg: Annotated[int, ("SunSpecPoint", {'name': 'WRtg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: WRtg_SF
    WRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'WRtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VARtg: Annotated[int, ("SunSpecPoint", {'name': 'VARtg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: VARtg_SF
    VARtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'VARtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VArRtgQ1: Annotated[int, ("SunSpecPoint", {'name': 'VArRtgQ1', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: VArRtg_SF
    VArRtgQ2: Annotated[int, ("SunSpecPoint", {'name': 'VArRtgQ2', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: VArRtg_SF
    VArRtgQ3: Annotated[int, ("SunSpecPoint", {'name': 'VArRtgQ3', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: VArRtg_SF
    VArRtgQ4: Annotated[int, ("SunSpecPoint", {'name': 'VArRtgQ4', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: VArRtg_SF
    VArRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'VArRtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    ARtg: Annotated[int, ("SunSpecPoint", {'name': 'ARtg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: ARtg_SF
    ARtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'ARtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    PFRtgQ1: Annotated[int, ("SunSpecPoint", {'name': 'PFRtgQ1', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: PFRtg_SF
    PFRtgQ2: Annotated[int, ("SunSpecPoint", {'name': 'PFRtgQ2', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: PFRtg_SF
    PFRtgQ3: Annotated[int, ("SunSpecPoint", {'name': 'PFRtgQ3', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: PFRtg_SF
    PFRtgQ4: Annotated[int, ("SunSpecPoint", {'name': 'PFRtgQ4', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: PFRtg_SF
    PFRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'PFRtg_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    WHRtg: Annotated[int, ("SunSpecPoint", {'name': 'WHRtg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: WHRtg_SF
    WHRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'WHRtg_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    AhrRtg: Annotated[int, ("SunSpecPoint", {'name': 'AhrRtg', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: AhrRtg_SF
    AhrRtg_SF: Annotated[int, ("SunSpecPoint", {'name': 'AhrRtg_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    MaxChaRte: Annotated[int, ("SunSpecPoint", {'name': 'MaxChaRte', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: MaxChaRte_SF
    MaxChaRte_SF: Annotated[int, ("SunSpecPoint", {'name': 'MaxChaRte_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    MaxDisChaRte: Annotated[int, ("SunSpecPoint", {'name': 'MaxDisChaRte', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: MaxDisChaRte_SF
    MaxDisChaRte_SF: Annotated[int, ("SunSpecPoint", {'name': 'MaxDisChaRte_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

