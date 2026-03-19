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


class Model705PtGroup(SunSpecGroup):
    """
    Stored curve points.

    Attributes:
        V (int): Curve voltage point as percentage.
        Var (int): Curve reactive power point as set in DeptRef point.
    """

    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    Var: Annotated[int, ("SunSpecPoint", {'name': 'Var', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: DeptRef_SF


class Model705DeptRef(IntEnum):
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



class Model705Pri(IntEnum):
    """
    Power priority.

    Members:
        ACTIVE (int): Active power priority.
        REACTIVE (int): Reactive power priority.
        VENDOR (int): Power priority is vendor specific mode.
    """
    ACTIVE = 0
    REACTIVE = 1
    VENDOR = 2



class Model705VRefAutoEna(IntEnum):
    """
    Enable autonomous vref.

    Members:
        DISABLED (int): Disabled flag (Disabled = 0, Enabled = 1).
        ENABLED (int): Enabled flag (Disabled = 0, Enabled = 1).
    """
    DISABLED = 0
    ENABLED = 1



class Model705ReadOnly(IntEnum):
    """
    Curve read-write access.

    Members:
        RW (int): Curve has read-write access.
        R (int): Curve has read-only access.
    """
    RW = 0
    R = 1



class Model705CrvGroup(SunSpecGroup):
    """
    Stored curve sets.

    Attributes:
        ActPt (int): Number of active points.
        DeptRef (Model705DeptRef): Curve dependent reference.
        Pri (Model705Pri): Power priority.
        VRef (int): Vref adjustment as percentage of nominal voltage.
        VRefAuto (int): Autonomous vref value as a percentage of nominal voltage.
        VRefAutoEna (Model705VRefAutoEna): Enable autonomous vref.
        VRefAutoTms (int): Autonomous vref time constant.
        RspTms (int): Open loop response time.
        ReadOnly (Model705ReadOnly): Curve read-write access.
    """

    ActPt: Annotated[int, ("SunSpecPoint", {'name': 'ActPt', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    DeptRef: Annotated[int, ("SunSpecPoint", {'name': 'DeptRef', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    Pri: Annotated[int, ("SunSpecPoint", {'name': 'Pri', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VRef: Annotated[int, ("SunSpecPoint", {'name': 'VRef', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: V_SF
    VRefAuto: Annotated[int, ("SunSpecPoint", {'name': 'VRefAuto', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: V_SF
    VRefAutoEna: Annotated[int, ("SunSpecPoint", {'name': 'VRefAutoEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VRefAutoTms: Annotated[int, ("SunSpecPoint", {'name': 'VRefAutoTms', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RspTms: Annotated[int, ("SunSpecPoint", {'name': 'RspTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: RspTms_SF
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    Pt: Annotated[SunSpecRepeatingBlock[Model705PtGroup], ("SunSpecRepeatingBlock", {"name": "Pt", "ptype": "group", "group_type": Model705PtGroup, "counter": "NPt"})]


class Model705Ena(IntEnum):
    """
    Volt-Var control enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model705AdptCrvRslt(IntEnum):
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



class Model705(SunSpecModel, model_name="DERVoltVar", id=705):
    """
    DER Volt-Var model.

    Attributes:
        Ena (Model705Ena): Volt-Var control enable.
        AdptCrvReq (int): Index of curve points to adopt. First curve index is 1.
        AdptCrvRslt (Model705AdptCrvRslt): Result of last adopt curve operation.
        NPt (int): Number of curve points supported.
        NCrv (int): Number of stored curves supported.
        RvrtTms (int): Reversion time in seconds.  0 = No reversion time.
        RvrtRem (int): Reversion time remaining in seconds.
        RvrtCrv (int): Default curve after reversion timeout.
        V_SF (int): Scale factor for curve voltage points.
        DeptRef_SF (int): Scale factor for curve var points.
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
    Crv: Annotated[SunSpecRepeatingBlock[Model705CrvGroup], ("SunSpecRepeatingBlock", {"name": "Crv", "ptype": "group", "group_type": Model705CrvGroup, "counter": "NCrv"})]

