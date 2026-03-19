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


class Model601Ctl(IntEnum):
    """
    Control register. Normal operation is automatic.  Operator can override the position by setting the ElCtl, AzCtl and enabling Manual operation. Entering calibration mode will revert to automatic operation after calibration is complete.

    Members:
        Automatic (int): Automatic
        Manual (int): Manual
        Calibrate (int): Calibrate
    """
    Automatic = 0
    Manual = 1
    Calibrate = 2



class Model601Alm(IntFlag):
    """
    Tracker alarm conditions

    Members:
        SetPoint (int): SetPoint
        ObsEl (int): ObsEl
        ObsAz (int): ObsAz
    """
    SetPoint = 1 << 0
    ObsEl = 1 << 1
    ObsAz = 1 << 2



class Model601TrackerGroup(SunSpecGroup):
    """
    Attributes:
        Id (str): Descriptive name for this tracker unit
        ElTrgt (int): Auto target elevation in degrees from horizontal.  Unimplemented for single axis azimuth tracker type
        AzTrgt (int): Auto target azimuth  in degrees from true north towards east.  Unimplemented for single axis horizontal tracker type
        ElPos (int): Actual elevation position  in degrees from horizontal.  Unimplemented for single axis azimuth tracker type
        AzPos (int): Actual azimuth position  in degrees from true north towards east.  Unimplemented for single axis horizontal tracker type
        ElCtl (int): Manual override target position of elevation in degrees from horizontal.  Unimplemented for single axis azimuth tracker type
        AzCtl (int): Manual override target position of azimuth in degrees from true north towards east.  Unimplemented for single axis azimuth tracker type
        Ctl (Model601Ctl): Control register. Normal operation is automatic.  Operator can override the position by setting the ElCtl, AzCtl and enabling Manual operation. Entering calibration mode will revert to automatic operation after calibration is complete.
        Alm (Model601Alm): Tracker alarm conditions
    """

    Id: Annotated[str, ("SunSpecPoint", {'name': 'Id', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False})]
    ElTrgt: Annotated[int, ("SunSpecPoint", {'name': 'ElTrgt', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: Dgr_SF
    AzTrgt: Annotated[int, ("SunSpecPoint", {'name': 'AzTrgt', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: Dgr_SF
    ElPos: Annotated[int, ("SunSpecPoint", {'name': 'ElPos', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: Dgr_SF
    AzPos: Annotated[int, ("SunSpecPoint", {'name': 'AzPos', 'ptype': 'int32', 'mandatory': False, 'static': False})]  # sf: Dgr_SF
    ElCtl: Annotated[int, ("SunSpecPoint", {'name': 'ElCtl', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Dgr_SF
    AzCtl: Annotated[int, ("SunSpecPoint", {'name': 'AzCtl', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Dgr_SF
    Ctl: Annotated[int, ("SunSpecPoint", {'name': 'Ctl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    Alm: Annotated[int, ("SunSpecPoint", {'name': 'Alm', 'ptype': 'uint16', 'mandatory': False, 'static': False})]


class Model601Typ(IntEnum):
    """
    Type of tracker

    Members:
        Unknown (int): Unknown
        Fixed (int): Fixed
        Horizontal (int): Horizontal
        Tilted (int): Tilted
        Azimuth (int): Azimuth
        Dual (int): Dual
        Other (int): Other
    """
    Unknown = 0
    Fixed = 1
    Horizontal = 2
    Tilted = 3
    Azimuth = 4
    Dual = 5
    Other = 99



class Model601GlblCtl(IntEnum):
    """
    Global Control register operates on all trackers. Normal operation is automatic.  Operator can override the position by setting the ElCtl, AzCtl and enabling Manual operation. Entering calibration mode will revert to automatic operation after calibration is complete.

    Members:
        Automatic (int): Automatic
        Manual (int): Manual
        Calibrate (int): Calibrate
    """
    Automatic = 0
    Manual = 1
    Calibrate = 2



class Model601GlblAlm(IntFlag):
    """
    Global tracker alarm conditions

    Members:
        SetPoint (int): SetPoint
        ObsEl (int): ObsEl
        ObsAz (int): ObsAz
    """
    SetPoint = 1 << 0
    ObsEl = 1 << 1
    ObsAz = 1 << 2



class Model601(SunSpecModel, model_name="tracker_controller", id=601):
    """
    Monitors and controls multiple trackers

    Attributes:
        Nam (str): Descriptive name for this control unit
        Typ (Model601Typ): Type of tracker
        DtLoc (str): Local date in YYYYMMDD format
        TmLoc (str): 24 hour local time stamp to second
        Day (int): Number of the day in the year (1-366)
        GlblElCtl (int): Global manual override target position of elevation in degrees from horizontal.  Unimplemented for single axis azimuth tracker type
        GlblAzCtl (int): Global manual override target position of azimuth in degrees from true north towards east.  Unimplemented for single axis azimuth tracker type
        GlblCtl (Model601GlblCtl): Global Control register operates on all trackers. Normal operation is automatic.  Operator can override the position by setting the ElCtl, AzCtl and enabling Manual operation. Entering calibration mode will revert to automatic operation after calibration is complete.
        GlblAlm (Model601GlblAlm): Global tracker alarm conditions
        Dgr_SF (int): Scale Factor for targets and position measurements in degrees
        N (int): Number of trackers being controlled.  Size of repeating block.
    """

    Nam: Annotated[str, ("SunSpecPoint", {'name': 'Nam', 'ptype': 'string', 'size': 8, 'mandatory': False, 'static': False})]
    Typ: Annotated[int, ("SunSpecPoint", {'name': 'Typ', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    DtLoc: Annotated[str, ("SunSpecPoint", {'name': 'DtLoc', 'ptype': 'string', 'size': 5, 'mandatory': False, 'static': False})]
    TmLoc: Annotated[str, ("SunSpecPoint", {'name': 'TmLoc', 'ptype': 'string', 'size': 3, 'mandatory': False, 'static': False})]
    Day: Annotated[int, ("SunSpecPoint", {'name': 'Day', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    GlblElCtl: Annotated[int, ("SunSpecPoint", {'name': 'GlblElCtl', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Dgr_SF
    GlblAzCtl: Annotated[int, ("SunSpecPoint", {'name': 'GlblAzCtl', 'ptype': 'int32', 'mandatory': False, 'static': False, 'access': 'RW'})]  # sf: Dgr_SF
    GlblCtl: Annotated[int, ("SunSpecPoint", {'name': 'GlblCtl', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    GlblAlm: Annotated[int, ("SunSpecPoint", {'name': 'GlblAlm', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    Dgr_SF: Annotated[int, ("SunSpecPoint", {'name': 'Dgr_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    N: Annotated[int, ("SunSpecPoint", {'name': 'N', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    tracker: Annotated[Model601TrackerGroup, ("SunSpecGroup", {"name": "tracker", "group_type": Model601TrackerGroup})]

