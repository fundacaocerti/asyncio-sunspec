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


class Model709PtGroup(SunSpecGroup):
    """
    Must trip curve points.

    Attributes:
        Hz (int): Curve frequency point.
        Tms (int): Curve time point in seconds.
    """

    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF


class Model709MusttripGroup(SunSpecGroup):
    """
    Stored must trip curve.

    Attributes:
        ActPt (int): Number of active points in must trip curve.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pt: Annotated[SunSpecRepeatingBlock[Model709PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model709PtGroup, "counter": "NPt"})]


class Model709PtGroup(SunSpecGroup):
    """
    May trip curve points.

    Attributes:
        Hz (int): Curve frequency point.
        Tms (int): Curve time point in seconds.
    """

    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF


class Model709MaytripGroup(SunSpecGroup):
    """
    Stored may trip curve.

    Attributes:
        ActPt (int): Number of active points in may trip curve.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pt: Annotated[SunSpecRepeatingBlock[Model709PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model709PtGroup, "counter": "NPt"})]


class Model709PtGroup(SunSpecGroup):
    """
    Momentary cessation curve points.

    Attributes:
        Hz (int): Curve frequency point.
        Tms (int): Curve time point in seconds.
    """

    Hz: Annotated[int, ("SunSpecPoint", {'name': 'Hz', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Hz_SF
    Tms: Annotated[int, ("SunSpecPoint", {'name': 'Tms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Tms_SF


class Model709MomcessGroup(SunSpecGroup):
    """
    Stored momentary cessation curve.

    Attributes:
        ActPt (int): Number of active points in the momentary cessation curve.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Pt: Annotated[SunSpecRepeatingBlock[Model709PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model709PtGroup, "counter": "NPt"})]


class Model709ReadOnly(IntEnum):
    """
    Curve read-write access.

    Members:
        RW (int): Curve has read-write access.
        R (int): Curve has read-only access.
    """
    RW = 0
    R = 1



class Model709CrvGroup(SunSpecGroup):
    """
    Stored curve sets.

    Attributes:
        ReadOnly (Model709ReadOnly): Curve read-write access.
    """

    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    MustTrip: Annotated[Model709MusttripGroup, ("SunSpecGroup", {"name": "MustTrip", "group_type": Model709MusttripGroup})]
    MayTrip: Annotated[Model709MaytripGroup, ("SunSpecGroup", {"name": "MayTrip", "group_type": Model709MaytripGroup})]
    MomCess: Annotated[Model709MomcessGroup, ("SunSpecGroup", {"name": "MomCess", "group_type": Model709MomcessGroup})]


class Model709Ena(IntEnum):
    """
    DER low frequency trip control enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model709AdptCrvRslt(IntEnum):
    """
    Result of last adopt curve operation.

    Members:
        IN_PROGRESS (int): Curve update in progress.
        COMPLETED (int): Curve update completed successfully.
        FAILED (int): Curve update failed.
    """
    IN_PROGRESS = 0
    COMPLETED = 1
    FAILED = 2



class Model709(SunSpecModel, model_name="DERTripLF", id=709):
    """
    DER low frequency trip model.

    Attributes:
        Ena (Model709Ena): DER low frequency trip control enable.
        AdptCrvReq (int): Index of curve points to adopt. First curve index is 1.
        AdptCrvRslt (Model709AdptCrvRslt): Result of last adopt curve operation.
        NPt (int): Number of curve points supported.
        NCrvSet (int): Number of stored curves supported.
        Hz_SF (int): Scale factor for curve frequency points.
        Tms_SF (int): Scale factor for curve time points.
    """

    Ena: Annotated[int, ("SunSpecPoint", {'name': 'Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCrvReq: Annotated[int, ("SunSpecPoint", {'name': 'AdptCrvReq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCrvRslt: Annotated[int, ("SunSpecPoint", {'name': 'AdptCrvRslt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    NCrvSet: Annotated[int, ("SunSpecPoint", {'name': 'NCrvSet', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    Hz_SF: Annotated[int, ("SunSpecPoint", {'name': 'Hz_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Tms_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tms_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Crv: Annotated[SunSpecRepeatingBlock[Model709CrvGroup], ("SunSpecRepeatingBlock", {"name": "Crv", "ptype": "group", "group_type": Model709CrvGroup, "counter": "NCrvSet"})]

