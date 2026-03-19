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


class Model711ReadOnly(IntEnum):
    """
    Control read-write access.

    Members:
        RW (int): Control has read-write access.
        R (int): Control has read-only access.
    """
    RW = 0
    R = 1



class Model711CtlGroup(SunSpecGroup):
    """
    Stored control sets.

    Attributes:
        DbOf (int): The deadband value for over-frequency conditions in Hz.
        DbUf (int): The deadband value for under-frequency conditions in Hz.
        KOf (int): Frequency droop per-unit frequency change for over-frequency conditions corresponding to 1 per-unit power output change.
        KUf (int): Frequency droop per-unit frequency change for under-frequency conditions corresponding to 1 per-unit power output change.
        RspTms (int): The open-loop response time in seconds.
        PMin (int): The minimum active power output due to DER prime mover constraints, in percent of the DER active power rating. The valid range is -100 to 100. This setting applies only to the frequency droop control.
        ReadOnly (Model711ReadOnly): Control read-write access.
    """

    DbOf: Annotated[int, ("SunSpecPoint", {'name': 'DbOf', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Db_SF
    DbUf: Annotated[int, ("SunSpecPoint", {'name': 'DbUf', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: Db_SF
    KOf: Annotated[int, ("SunSpecPoint", {'name': 'KOf', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: K_SF
    KUf: Annotated[int, ("SunSpecPoint", {'name': 'KUf', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: K_SF
    RspTms: Annotated[int, ("SunSpecPoint", {'name': 'RspTms', 'ptype': 'uint32', 'mandatory': True, 'static': False, 'access': 'RW'})]  # sf: RspTms_SF
    PMin: Annotated[int, ("SunSpecPoint", {'name': 'PMin', 'ptype': 'int16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ReadOnly: Annotated[int, ("SunSpecPoint", {'name': 'ReadOnly', 'ptype': 'uint16', 'mandatory': True, 'static': True})]


class Model711Ena(IntEnum):
    """
    DER Frequency-Watt (Frequency-Droop) control enable.

    Members:
        DISABLED (int): Function is disabled.
        ENABLED (int): Function is enabled.
    """
    DISABLED = 0
    ENABLED = 1



class Model711AdptCtlRslt(IntEnum):
    """
    Result of last set active control operation.

    Members:
        IN_PROGRESS (int): Control update in progress.
        COMPLETED (int): Control update completed successfully.
        FAILED (int): Control update failed.
    """
    IN_PROGRESS = 0
    COMPLETED = 1
    FAILED = 2



class Model711(SunSpecModel, model_name="DERFreqDroop", id=711):
    """
    DER Frequency Droop model.

    Attributes:
        Ena (Model711Ena): DER Frequency-Watt (Frequency-Droop) control enable.
        AdptCtlReq (int): Set active control. 0 = No active control.
        AdptCtlRslt (Model711AdptCtlRslt): Result of last set active control operation.
        NCtl (int): Number of stored controls supported.
        RvrtTms (int): Reversion time in seconds.  0 = No reversion time.
        RvrtRem (int): Reversion time remaining in seconds.
        RvrtCtl (int): Default control after reversion timeout.
        Db_SF (int): Deadband scale factor.
        K_SF (int): Frequency change scale factor.
        RspTms_SF (int): Open loop response time scale factor.
    """

    Ena: Annotated[int, ("SunSpecPoint", {'name': 'Ena', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCtlReq: Annotated[int, ("SunSpecPoint", {'name': 'AdptCtlReq', 'ptype': 'uint16', 'mandatory': True, 'static': False, 'access': 'RW'})]
    AdptCtlRslt: Annotated[int, ("SunSpecPoint", {'name': 'AdptCtlRslt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NCtl: Annotated[int, ("SunSpecPoint", {'name': 'NCtl', 'ptype': 'uint16', 'mandatory': True, 'static': True})]
    RvrtTms: Annotated[int, ("SunSpecPoint", {'name': 'RvrtTms', 'ptype': 'uint32', 'mandatory': False, 'static': False, 'access': 'RW'})]
    RvrtRem: Annotated[int, ("SunSpecPoint", {'name': 'RvrtRem', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    RvrtCtl: Annotated[int, ("SunSpecPoint", {'name': 'RvrtCtl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Db_SF: Annotated[int, ("SunSpecPoint", {'name': 'Db_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    K_SF: Annotated[int, ("SunSpecPoint", {'name': 'K_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    RspTms_SF: Annotated[int, ("SunSpecPoint", {'name': 'RspTms_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': True})]
    Ctl: Annotated[SunSpecRepeatingBlock[Model711CtlGroup], ("SunSpecRepeatingBlock", {"name": "Ctl", "ptype": "group", "group_type": Model711CtlGroup, "counter": "NCtl"})]

