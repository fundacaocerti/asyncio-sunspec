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


class Model712PtGroup(SunSpecGroup):
    """
    Stored curve points.

    Attributes:
        W (int): Curve active power point as percentage.
        Var (int): Curve reactive power point as set in DeptRef point.
    """

    W: Annotated[int, ("SunSpecPoint", {'name': 'W', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: W_SF
    Var: Annotated[int, ("SunSpecPoint", {'name': 'Var', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF


class Model712DeptRef(IntEnum):
    """
    Curve dependent reference.

    Members:
        W_MAX_PCT (int): Percent Max Watts
        VAR_MAX_PCT (int): Percent Max Vars
        VAR_AVAL_PCT (int): Percent Available Vars
        VA_MAX_PCT (int): Percent Max Apparent Power
    """
    W_MAX_PCT = 0
    VAR_MAX_PCT = 1
    VAR_AVAL_PCT = 2
    VA_MAX_PCT = 3



class Model712Pri(IntEnum):
    """
    Power priority.

    Members:
        ACTIVE (int): Active power priority.
        REACTIVE (int): Reactive power priority.
    """
    ACTIVE = 0
    REACTIVE = 1



class Model712ReadOnly(IntEnum):
    """
    Curve read-write access.

    Members:
        RW (int): Curve has read-write access.
        R (int): Curve has read-only access.
    """
    RW = 0
    R = 1



class Model712CrvGroup(SunSpecGroup):
    """
    Stored curve sets.

    Attributes:
        ActPt (int): Number of active points.
        DeptRef (Model712DeptRef): Curve dependent reference.
        Pri (Model712Pri): Power priority.
        ReadOnly (Model712ReadOnly): Curve read-write access.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    DeptRef: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Pri: Annotated[int, ("SunSpecPoint", {'name': 'Pri', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    Pt: Annotated[SunSpecRepeatingBlock[Model712PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model712PtGroup, "counter": "NPt"})]


class Model712Ena(IntEnum):
    """
    DER Watt-Var control enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model712AdptCrvRslt(IntEnum):
    """
    Result of last set active curve operation.

    Members:
        IN_PROGRESS (int): Curve update in progress.
        COMPLETED (int): Curve update completed successfully.
        FAILED (int): Curve update failed.
    """
    IN_PROGRESS = 0
    COMPLETED = 1
    FAILED = 2



class Model712(SunSpecModel, model_name="DERWattVar", id=712):
    """
    DER Watt-Var model.

    Attributes:
        Ena (Model712Ena): DER Watt-Var control enable.
        AdptCrvReq (int): Set active curve. 0 = No active curve.
        AdptCrvRslt (Model712AdptCrvRslt): Result of last set active curve operation.
        NPt (int): Number of curve points supported.
        NCrv (int): Number of stored curves supported.
        RvrtTms (int): Reversion time in seconds.  0 = No reversion time.
        RvrtRem (int): Reversion time remaining in seconds.
        RvrtCrv (int): Default curve after reversion timeout.
        W_SF (int): Scale factor for curve active power points.
        DeptRef_SF (int): Scale factor for curve var points.
    """

    Ena: Annotated[int, ("SunSpecPoint", {'name': 'Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCrvReq: Annotated[int, ("SunSpecPoint", {'name': 'AdptCrvReq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCrvRslt: Annotated[int, ("SunSpecPoint", {'name': 'AdptCrvRslt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NPt: Annotated[int, ("SunSpecPoint", {'name': 'NPt', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    NCrv: Annotated[int, ("SunSpecPoint", {'name': 'NCrv', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'RvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    RvrtCrv: Annotated[int, ("SunSpecPoint", {'name': 'RvrtCrv', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    W_SF: Annotated[int, ("SunSpecPoint", {'name': 'W_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    DeptRef_SF: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Crv: Annotated[SunSpecRepeatingBlock[Model712CrvGroup], ("SunSpecRepeatingBlock", {"name": "Crv", "ptype": "group", "group_type": Model712CrvGroup, "counter": "NCrv"})]

