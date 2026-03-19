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


class Model714PrtTyp(IntEnum):
    """
    Port type.

    Members:
        PV (int): Photovoltaic
        ESS (int): Energy Storage System
        EV (int): Electric Vehicle
        INJ (int): Generic Injecting
        ABS (int): Generic Absorbing
        BIDIR (int): Generic Bidirectional
        DC_DC (int): DC to DC
    """
    PV = 0
    ESS = 1
    EV = 2
    INJ = 3
    ABS = 4
    BIDIR = 5
    DC_DC = 6



class Model714DCSta(IntEnum):
    """
    DC port status.

    Members:
        OFF (int): Off
        ON (int): On
        WARNING (int): Warning
        ERROR (int): Error
    """
    OFF = 0
    ON = 1
    WARNING = 2
    ERROR = 3



class Model714DCAlrm(IntFlag):
    """
    DC port alarm.

    Members:
        GROUND_FAULT (int): Ground Fault
        INPUT_OVER_VOLTAGE (int): Input Over Voltage
        DC_DISCONNECT (int): DC Disconnect
        CABINET_OPEN (int): Cabinet Open
        MANUAL_SHUTDOWN (int): Manual Shutdown
        OVER_TEMP (int): Over Temperature
        BLOWN_FUSE (int): Blown Fuse
        UNDER_TEMP (int): Under Temperature
        MEMORY_LOSS (int): Memory Loss
        ARC_DETECTION (int): Arc Detection
        RESERVED (int): Reserved
        TEST_FAILED (int): Test Failed
        INPUT_UNDER_VOLTAGE (int): Under Voltage
        INPUT_OVER_CURRENT (int): Over Current
    """
    GROUND_FAULT = 1 << 0
    INPUT_OVER_VOLTAGE = 1 << 1
    DC_DISCONNECT = 1 << 3
    CABINET_OPEN = 1 << 5
    MANUAL_SHUTDOWN = 1 << 6
    OVER_TEMP = 1 << 7
    BLOWN_FUSE = 1 << 12
    UNDER_TEMP = 1 << 13
    MEMORY_LOSS = 1 << 14
    ARC_DETECTION = 1 << 15
    RESERVED = 1 << 19
    TEST_FAILED = 1 << 20
    INPUT_UNDER_VOLTAGE = 1 << 21
    INPUT_OVER_CURRENT = 1 << 22



class Model714PrtGroup(SunSpecGroup):
    """
    Attributes:
        PrtTyp (Model714PrtTyp): Port type.
        ID (int): Port ID.
        IDStr (str): Port ID string.
        DCA (int): DC current for the port.
        DCV (int): DC voltage for the port.
        DCW (int): DC power for the port.
        DCWhInj (int): Total cumulative DC energy injected for the port.
        DCWhAbs (int): Total cumulative DC energy absorbed for the port.
        Tmp (int): DC port temperature.
        DCSta (Model714DCSta): DC port status.
        DCAlrm (Model714DCAlrm): DC port alarm.
    """

    PrtTyp: Annotated[int, ("SunSpecPoint", {'name': 'PrtTyp', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    ID: Annotated[int, ("SunSpecPoint", {'name': 'ID', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    IDStr: Annotated[str, ("SunSpecPoint", {'name': 'IDStr', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False})]
    DCA: Annotated[int, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCA_SF
    DCV: Annotated[int, ("SunSpecPoint", {'name': 'DCV', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DCV_SF
    DCW: Annotated[int, ("SunSpecPoint", {'name': 'DCW', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCW_SF
    DCWhInj: Annotated[int, ("SunSpecPoint", {'name': 'DCWhInj', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: DCWH_SF
    DCWhAbs: Annotated[int, ("SunSpecPoint", {'name': 'DCWhAbs', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: DCWH_SF
    Tmp: Annotated[int, ("SunSpecPoint", {'name': 'Tmp', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: Tmp_SF
    DCSta: Annotated[int, ("SunSpecPoint", {'name': 'DCSta', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    DCAlrm: Annotated[int, ("SunSpecPoint", {'name': 'DCAlrm', 'ptype': 'uint32', 'mandatory': False, 'static': False})]


class Model714(SunSpecModel, model_name="DERMeasureDC", id=714):
    """
    DER DC measurement.

    Attributes:
        PrtAlrms (int): Bitfield of ports with active alarms. Bit is 1 if port has an active alarm. Bit 0 is first port.
        NPrt (int): Number of DC ports.
        DCA (int): Total DC current for all ports.
        DCW (int): Total DC power for all ports.
        DCWhInj (int): Total cumulative DC energy injected for all ports.
        DCWhAbs (int): Total cumulative DC energy absorbed for all ports.
        DCA_SF (int): DC current scale factor.
        DCV_SF (int): DC voltage scale factor.
        DCW_SF (int): DC power scale factor.
        DCWH_SF (int): DC energy scale factor.
        Tmp_SF (int): Temperature Scale Factor.
    """

    PrtAlrms: Annotated[int, ("SunSpecPoint", {'name': 'PrtAlrms', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    NPrt: Annotated[int, ("SunSpecPoint", {'name': 'NPrt', 'ptype': 'uint16', 'mandatory': False, 'static': True})]
    DCA: Annotated[int, ("SunSpecPoint", {'name': 'DCA', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCA_SF
    DCW: Annotated[int, ("SunSpecPoint", {'name': 'DCW', 'ptype': 'int16', 'mandatory': False, 'static': False})]  # sf: DCW_SF
    DCWhInj: Annotated[int, ("SunSpecPoint", {'name': 'DCWhInj', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: DCWH_SF
    DCWhAbs: Annotated[int, ("SunSpecPoint", {'name': 'DCWhAbs', 'ptype': 'uint64', 'mandatory': False, 'static': False})]  # sf: DCWH_SF
    DCA_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCA_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    DCV_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCV_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    DCW_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCW_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    DCWH_SF: Annotated[int, ("SunSpecPoint", {'name': 'DCWH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Tmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tmp_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': True})]
    Prt: Annotated[SunSpecRepeatingBlock[Model714PrtGroup], ("SunSpecRepeatingBlock", {"name": "Prt", "ptype": "group", "group_type": Model714PrtGroup, "counter": "NPrt"})]

