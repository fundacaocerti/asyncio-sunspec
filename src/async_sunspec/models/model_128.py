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


class Model128ArGraMod(IntEnum):
    """
    Indicates if gradients trend toward zero at the edges of the deadband or trend toward zero at the center of the deadband.

    Members:
        EDGE (int): EDGE
        CENTER (int): CENTER
    """
    EDGE = 0
    CENTER = 1



class Model128ModEna(IntFlag):
    """
    Activate dynamic reactive current model

    Members:
        ENABLED (int): ENABLED
    """
    ENABLED = 1 << 0



class Model128(SunSpecModel, model_name="reactive_current", id=128):
    """
    Dynamic Reactive Current 

    Attributes:
        ArGraMod (Model128ArGraMod): Indicates if gradients trend toward zero at the edges of the deadband or trend toward zero at the center of the deadband.
        ArGraSag (int): The gradient used to increase capacitive dynamic current. A value of 0 indicates no additional reactive current support.
        ArGraSwell (int): The gradient used to increase inductive dynamic current.  A value of 0 indicates no additional reactive current support.
        ModEna (Model128ModEna): Activate dynamic reactive current model
        FilTms (int): The time window used to calculate the moving average voltage.
        DbVMin (int): The lower delta voltage limit for which negative voltage deviations less than this value no dynamic vars are produced.
        DbVMax (int): The upper delta voltage limit for which positive voltage deviations less than this value no dynamic current produced.
        BlkZnV (int): Block zone voltage which defines a lower voltage boundary below which no dynamic current is produced.
        HysBlkZnV (int): Hysteresis voltage used with BlkZnV.
        BlkZnTmms (int): Block zone time the time before which reactive current support remains active regardless of how low the voltage drops.
        HoldTmms (int): Hold time during which reactive current support continues after the average voltage has entered the dead zone.
        ArGra_SF (int): Scale factor for the gradients.
        VRefPct_SF (int): Scale factor for the voltage zone and limit settings.
        Pad (int)
    """

    ArGraMod: Annotated[int, ("SunSpecPoint", {'name': 'ArGraMod', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    ArGraSag: Annotated[int, ("SunSpecPoint", {'name': 'ArGraSag', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: ArGra_SF
    ArGraSwell: Annotated[int, ("SunSpecPoint", {'name': 'ArGraSwell', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: ArGra_SF
    ModEna: Annotated[int, ("SunSpecPoint", {'name': 'ModEna', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    FilTms: Annotated[int, ("SunSpecPoint", {'name': 'FilTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    DbVMin: Annotated[int, ("SunSpecPoint", {'name': 'DbVMin', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VRefPct_SF
    DbVMax: Annotated[int, ("SunSpecPoint", {'name': 'DbVMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VRefPct_SF
    BlkZnV: Annotated[int, ("SunSpecPoint", {'name': 'BlkZnV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VRefPct_SF
    HysBlkZnV: Annotated[int, ("SunSpecPoint", {'name': 'HysBlkZnV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VRefPct_SF
    BlkZnTmms: Annotated[int, ("SunSpecPoint", {'name': 'BlkZnTmms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    HoldTmms: Annotated[int, ("SunSpecPoint", {'name': 'HoldTmms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ArGra_SF: Annotated[int, ("SunSpecPoint", {'name': 'ArGra_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    VRefPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'VRefPct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    Pad: Annotated[int, ("SunSpecPoint", {'name': 'Pad', 'ptype': 'uint16', 'mandatory': False, 'static': False})]

