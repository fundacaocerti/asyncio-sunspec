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


class Model704Ext(IntEnum):
    """
    Power factor excitation setpoint when injecting active power.

    Members:
        OVER_EXCITED (int): Power factor over-excited excitation.
        UNDER_EXCITED (int): Power factor under-excited excitation.
    """
    OVER_EXCITED = 0
    UNDER_EXCITED = 1



class Model704PfwinjGroup(SunSpecGroup):
    """
    Power factor setpoint when injecting active power.

    Attributes:
        PF (int): Power factor setpoint when injecting active power.
        Ext (Model704Ext): Power factor excitation setpoint when injecting active power.
    """

    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    Ext: Annotated[int, ("SunSpecPoint", {'name': 'Ext', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]


class Model704Ext(IntEnum):
    """
    Reversion power factor excitation setpoint when injecting active power.

    Members:
        OVER_EXCITED (int): Power factor over-excited excitation.
        UNDER_EXCITED (int): Power factor under-excited excitation.
    """
    OVER_EXCITED = 0
    UNDER_EXCITED = 1



class Model704PfwinjrvrtGroup(SunSpecGroup):
    """
    Reversion power factor setpoint when injecting active power.

    Attributes:
        PF (int): Reversion power factor setpoint when injecting active power.
        Ext (Model704Ext): Reversion power factor excitation setpoint when injecting active power.
    """

    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    Ext: Annotated[int, ("SunSpecPoint", {'name': 'Ext', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]


class Model704Ext(IntEnum):
    """
    Power factor excitation setpoint when absorbing active power.

    Members:
        OVER_EXCITED (int): Power factor over-excited excitation.
        UNDER_EXCITED (int): Power factor under-excited excitation.
    """
    OVER_EXCITED = 0
    UNDER_EXCITED = 1



class Model704PfwabsGroup(SunSpecGroup):
    """
    Power factor setpoint when absorbing active power.

    Attributes:
        PF (int): Power factor setpoint when absorbing active power.
        Ext (Model704Ext): Power factor excitation setpoint when absorbing active power.
    """

    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    Ext: Annotated[int, ("SunSpecPoint", {'name': 'Ext', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]


class Model704Ext(IntEnum):
    """
    Reversion power factor excitation setpoint when absorbing active power.

    Members:
        OVER_EXCITED (int): Power factor over-excited excitation.
        UNDER_EXCITED (int): Power factor under-excited excitation.
    """
    OVER_EXCITED = 0
    UNDER_EXCITED = 1



class Model704PfwabsrvrtGroup(SunSpecGroup):
    """
    Reversion power factor setpoint when absorbing active power.

    Attributes:
        PF (int): Reversion power factor setpoint when absorbing active power.
        Ext (Model704Ext): Reversion power factor excitation setpoint when absorbing active power.
    """

    PF: Annotated[int, ("SunSpecPoint", {'name': 'PF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: PF_SF
    Ext: Annotated[int, ("SunSpecPoint", {'name': 'Ext', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]


class Model704PFWInjEna(IntEnum):
    """
    Power factor enable when injecting active power.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704PFWInjEnaRvrt(IntEnum):
    """
    Power factor reversion timer when injecting active power enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704PFWAbsEna(IntEnum):
    """
    Power factor enable when absorbing active power.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704PFWAbsEnaRvrt(IntEnum):
    """
    Power factor reversion timer when absorbing active power enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704WMaxLimPctEna(IntEnum):
    """
    Limit maximum active power percent enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704WMaxLimPctEnaRvrt(IntEnum):
    """
    Reversion limit maximum active power percent value enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704WSetEna(IntEnum):
    """
    Set active power enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704WSetMod(IntEnum):
    """
    Set active power mode.

    Members:
        W_MAX_PCT (int): Active power setting is percentage of maximum active power.
        WATTS (int): Active power setting is in watts.
    """
    W_MAX_PCT = 0
    WATTS = 1



class Model704WSetEnaRvrt(IntEnum):
    """
    Reversion active power function enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704VarSetEna(IntEnum):
    """
    Set reactive power enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704VarSetMod(IntEnum):
    """
    Set reactive power mode.

    Members:
        W_MAX_PCT (int): Reactive power setting is percent of maximum active power.
        VAR_MAX_PCT (int): Reactive power setting is percent of maximum reactive power.
        VAR_AVAIL_PCT (int): Reactive power setting is percent of available reactive  power.
        VA_MAX_PCT (int): Reactive power setting is percent of maximum apparent power.
        VARS (int): Reactive power is in vars.
    """
    W_MAX_PCT = 0
    VAR_MAX_PCT = 1
    VAR_AVAIL_PCT = 2
    VA_MAX_PCT = 3
    VARS = 4



class Model704VarSetPri(IntEnum):
    """
    Reactive power priority.

    Members:
        ACTIVE (int): Active power priority.
        REACTIVE (int): Reactive power priority.
        VENDOR (int): Power priority is vendor specific mode.
    """
    ACTIVE = 0
    REACTIVE = 1
    VENDOR = 2



class Model704VarSetEnaRvrt(IntEnum):
    """
    Reversion reactive power function enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704WRmpRef(IntEnum):
    """
    Ramp rate reference unit for increases in active power or current during normal generation.

    Members:
        A_MAX (int): Ramp based on percent of max current per second.
        W_MAX (int): Ramp based on percent of max active power per second.
    """
    A_MAX = 0
    W_MAX = 1



class Model704AntiIslEna(IntEnum):
    """
    Anti-islanding enable.

    Members:
        DISABLED (int): Anti-islanding is disabled.
        ENABLED (int): Anti-islanding is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model704(SunSpecModel, model_name="DERCtlAC", id=704):
    """
    DER AC controls model.

    Attributes:
        PFWInjEna (Model704PFWInjEna): Power factor enable when injecting active power.
        PFWInjEnaRvrt (Model704PFWInjEnaRvrt): Power factor reversion timer when injecting active power enable.
        PFWInjRvrtTms (int): Power factor reversion timer when injecting active power.
        PFWInjRvrtRem (int): Power factor reversion time remaining when injecting active power.
        PFWAbsEna (Model704PFWAbsEna): Power factor enable when absorbing active power.
        PFWAbsEnaRvrt (Model704PFWAbsEnaRvrt): Power factor reversion timer when absorbing active power enable.
        PFWAbsRvrtTms (int): Power factor reversion timer when absorbing active power.
        PFWAbsRvrtRem (int): Power factor reversion time remaining when absorbing active power.
        WMaxLimPctEna (Model704WMaxLimPctEna): Limit maximum active power percent enable.
        WMaxLimPct (int): Limit maximum active power percent value.
        WMaxLimPctRvrt (int): Reversion limit maximum active power percent value.
        WMaxLimPctEnaRvrt (Model704WMaxLimPctEnaRvrt): Reversion limit maximum active power percent value enable.
        WMaxLimPctRvrtTms (int): Limit maximum active power percent reversion time.
        WMaxLimPctRvrtRem (int): Limit maximum active power percent reversion time remaining.
        WSetEna (Model704WSetEna): Set active power enable.
        WSetMod (Model704WSetMod): Set active power mode.
        WSet (int): Active power setting value in watts.
        WSetRvrt (int): Reversion active power setting value in watts.
        WSetPct (int): Active power setting value as percent.
        WSetPctRvrt (int): Reversion active power setting value as percent.
        WSetEnaRvrt (Model704WSetEnaRvrt): Reversion active power function enable.
        WSetRvrtTms (int): Set active power reversion time.
        WSetRvrtRem (int): Set active power reversion time remaining.
        VarSetEna (Model704VarSetEna): Set reactive power enable.
        VarSetMod (Model704VarSetMod): Set reactive power mode.
        VarSetPri (Model704VarSetPri): Reactive power priority.
        VarSet (int): Reactive power setting value in vars.
        VarSetRvrt (int): Reversion reactive power setting value in vars.
        VarSetPct (int): Reactive power setting value as percent.
        VarSetPctRvrt (int): Reversion reactive power setting value as percent.
        VarSetEnaRvrt (Model704VarSetEnaRvrt): Reversion reactive power function enable.
        VarSetRvrtTms (int): Set reactive power reversion time.
        VarSetRvrtRem (int): Set reactive power reversion time remaining.
        WRmp (int): Ramp rate for increases in active power during normal generation.
        WRmpRef (Model704WRmpRef): Ramp rate reference unit for increases in active power or current during normal generation.
        VarRmp (int): Ramp rate based on max reactive power per second.
        AntiIslEna (Model704AntiIslEna): Anti-islanding enable.
        PF_SF (int): Power factor scale factor.
        WMaxLimPct_SF (int): Limit maximum power scale factor.
        WSet_SF (int): Active power scale factor.
        WSetPct_SF (int): Active power pct scale factor.
        VarSet_SF (int): Reactive power scale factor.
        VarSetPct_SF (int): Reactive power pct scale factor.
    """

    PFWInjEna: Annotated[int, ("SunSpecPoint", {'name': 'PFWInjEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PFWInjEnaRvrt: Annotated[int, ("SunSpecPoint", {'name': 'PFWInjEnaRvrt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PFWInjRvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'PFWInjRvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PFWInjRvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'PFWInjRvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    PFWAbsEna: Annotated[int, ("SunSpecPoint", {'name': 'PFWAbsEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PFWAbsEnaRvrt: Annotated[int, ("SunSpecPoint", {'name': 'PFWAbsEnaRvrt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PFWAbsRvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'PFWAbsRvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PFWAbsRvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'PFWAbsRvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    WMaxLimPctEna: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPctEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMaxLimPct: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WMaxLimPct_SF
    WMaxLimPctRvrt: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPctRvrt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WMaxLimPct_SF
    WMaxLimPctEnaRvrt: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPctEnaRvrt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMaxLimPctRvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPctRvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WMaxLimPctRvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPctRvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    WSetEna: Annotated[int, ("SunSpecPoint", {'name': 'WSetEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WSetMod: Annotated[int, ("SunSpecPoint", {'name': 'WSetMod', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WSet: Annotated[int, ("SunSpecPoint", {'name': 'WSet', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WSet_SF
    WSetRvrt: Annotated[int, ("SunSpecPoint", {'name': 'WSetRvrt', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WSet_SF
    WSetPct: Annotated[int, ("SunSpecPoint", {'name': 'WSetPct', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WSetPct_SF
    WSetPctRvrt: Annotated[int, ("SunSpecPoint", {'name': 'WSetPctRvrt', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: WSetPct_SF
    WSetEnaRvrt: Annotated[int, ("SunSpecPoint", {'name': 'WSetEnaRvrt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WSetRvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'WSetRvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WSetRvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'WSetRvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    VarSetEna: Annotated[int, ("SunSpecPoint", {'name': 'VarSetEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VarSetMod: Annotated[int, ("SunSpecPoint", {'name': 'VarSetMod', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VarSetPri: Annotated[int, ("SunSpecPoint", {'name': 'VarSetPri', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VarSet: Annotated[int, ("SunSpecPoint", {'name': 'VarSet', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VarSet_SF
    VarSetRvrt: Annotated[int, ("SunSpecPoint", {'name': 'VarSetRvrt', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VarSet_SF
    VarSetPct: Annotated[int, ("SunSpecPoint", {'name': 'VarSetPct', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VarSetPct_SF
    VarSetPctRvrt: Annotated[int, ("SunSpecPoint", {'name': 'VarSetPctRvrt', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: VarSetPct_SF
    VarSetEnaRvrt: Annotated[int, ("SunSpecPoint", {'name': 'VarSetEnaRvrt', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VarSetRvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'VarSetRvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VarSetRvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'VarSetRvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    WRmp: Annotated[int, ("SunSpecPoint", {'name': 'WRmp', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    WRmpRef: Annotated[int, ("SunSpecPoint", {'name': 'WRmpRef', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    VarRmp: Annotated[int, ("SunSpecPoint", {'name': 'VarRmp', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    AntiIslEna: Annotated[int, ("SunSpecPoint", {'name': 'AntiIslEna', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    PF_SF: Annotated[int, ("SunSpecPoint", {'name': 'PF_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    WMaxLimPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'WMaxLimPct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    WSet_SF: Annotated[int, ("SunSpecPoint", {'name': 'WSet_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    WSetPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'WSetPct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    VarSet_SF: Annotated[int, ("SunSpecPoint", {'name': 'VarSet_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    VarSetPct_SF: Annotated[int, ("SunSpecPoint", {'name': 'VarSetPct_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    PFWInj: Annotated[Model704PfwinjGroup, ("SunSpecGroup", {"name": "PFWInj", "group_type": Model704PfwinjGroup})]
    PFWInjRvrt: Annotated[Model704PfwinjrvrtGroup, ("SunSpecGroup", {"name": "PFWInjRvrt", "group_type": Model704PfwinjrvrtGroup})]
    PFWAbs: Annotated[Model704PfwabsGroup, ("SunSpecGroup", {"name": "PFWAbs", "group_type": Model704PfwabsGroup})]
    PFWAbsRvrt: Annotated[Model704PfwabsrvrtGroup, ("SunSpecGroup", {"name": "PFWAbsRvrt", "group_type": Model704PfwabsrvrtGroup})]

