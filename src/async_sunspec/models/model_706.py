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


class Model706PtGroup(SunSpecGroup):
    """
    Stored curve points.

    Attributes:
        V (int): Curve voltage point as percentage.
        W (int): Active power in percent of rated active power.
    """

    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF


class Model706DeptRef(IntEnum):
    """
    Curve dependent reference.

    Members:
        W_MAX_PCT (int): W_MAX_PCT
        W_AVAL_PCT (int): W_AVAL_PCT
    """
    W_MAX_PCT = 0
    W_AVAL_PCT = 1



class Model706ReadOnly(IntEnum):
    """
    Curve read-write access.

    Members:
        RW (int): Curve has read-write access.
        R (int): Curve has read-only access.
    """
    RW = 0
    R = 1



class Model706CrvGroup(SunSpecGroup):
    """
    Stored curve sets.

    Attributes:
        ActPt (int): Number of active points.
        DeptRef (Model706DeptRef): Curve dependent reference.
        RspTms (int): Open loop response time.
        ReadOnly (Model706ReadOnly): Curve read-write access.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    DeptRef: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    RspTms: Annotated[int, ("SunSpecPoint", {'name': 'RspTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RspTms_SF
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    Pt: Annotated[SunSpecRepeatingBlock[Model706PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model706PtGroup, "counter": "NPt"})]


class Model706Ena(IntEnum):
    """
    Volt-Watt control enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model706AdptCrvRslt(IntEnum):
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



class Model706(SunSpecModel, model_name="DERVoltWatt", id=706):
    """
    DER Volt-Watt model.

    Attributes:
        Ena (Model706Ena): Volt-Watt control enable.
        AdptCrvReq (int): Index of curve points to adopt. First curve index is 1.
        AdptCrvRslt (Model706AdptCrvRslt): Result of last adopt curve operation.
        NPt (int): Number of curve points supported.
        NCrv (int): Number of stored curves supported.
        RvrtTms (int): Reversion time in seconds.  0 = No reversion time.
        RvrtRem (int): Reversion time remaining in seconds.
        RvrtCrv (int): Default curve after reversion timeout.
        V_SF (int): Scale factor for curve voltage points.
        DeptRef_SF (int): Scale factor for curve watt points.
        RspTms_SF (int): Open loop response time scale factor.
    """

    Ena: Annotated[int, ("SunSpecPoint", {'name': 'Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCrvReq: Annotated[int, ("SunSpecPoint", {'name': 'AdptCrvReq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCrvRslt: Annotated[int, ("SunSpecPoint", {'name': 'AdptCrvRslt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    NCrv: Annotated[int, ("SunSpecPoint", {'name': 'NCrv', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'RvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    RvrtCrv: Annotated[int, ("SunSpecPoint", {'name': 'RvrtCrv', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    DeptRef_SF: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    RspTms_SF: Annotated[int, ("SunSpecPoint", {'name': 'RspTms_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Crv: Annotated[SunSpecRepeatingBlock[Model706CrvGroup], ("SunSpecRepeatingBlock", {"name": "Crv", "ptype": "group", "group_type": Model706CrvGroup, "counter": "NCrv"})]

