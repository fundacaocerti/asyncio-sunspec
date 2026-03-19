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


class Model64412DAManipulation(IntEnum):
    """
    Modify the device ID of the DER

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412FalsifyDeviceIdentity(IntEnum):
    """
    Change the DER manufacturer and model

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasPAlwaysNameplate(IntEnum):
    """
    Set the DER meas to always be at nameplate power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasQAlwaysMinimum(IntEnum):
    """
    Set the DER to always be at minimum reactive power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasQAlwaysMaximum(IntEnum):
    """
    Set the DER to always be at maximum reactive power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasQAlwaysZero(IntEnum):
    """
    Set the DER to always be at zero reactive power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasZeroP(IntEnum):
    """
    Set the DER to always be at zero P, Q, and S

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasInvertQ(IntEnum):
    """
    Set the DER to reverse the Q measurement data

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowV(IntEnum):
    """
    Set the DER to always measure low voltage

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasHighV(IntEnum):
    """
    Set the DER to always measure high voltage

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowL1V(IntEnum):
    """
    Set the DER to always measure low line 1 voltage

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasHighL1V(IntEnum):
    """
    Set the DER to always measure high line 1 voltage

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowF(IntEnum):
    """
    Set the DER to always measure low frequency

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasHighF(IntEnum):
    """
    Set the DER to always measure high frequency

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowAmps(IntEnum):
    """
    Set the DER to always measure low current

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasHighAmps(IntEnum):
    """
    Set the DER to always measure high current

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasHighS(IntEnum):
    """
    Set the DER to always measure high apparent power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowS(IntEnum):
    """
    Set the DER to always measure low apparent power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasHighQ(IntEnum):
    """
    Set the DER to always measure high reactive power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowQ(IntEnum):
    """
    Set the DER to always measure low reactive power

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowPF(IntEnum):
    """
    Set the DER to always measure low power factor

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412MeasLowReversedPF(IntEnum):
    """
    Set the DER to always measure low reversed power factor

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateHighP(IntEnum):
    """
    Set the DER nameplate power to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowP(IntEnum):
    """
    Set the DER nameplate power to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateHighS(IntEnum):
    """
    Set the DER nameplate apparent power to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowS(IntEnum):
    """
    Set the DER nameplate apparent power to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateHighQ(IntEnum):
    """
    Set the DER nameplate reactive power to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowQ(IntEnum):
    """
    Set the DER nameplate reactive power to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateHighNomV(IntEnum):
    """
    Set the DER nameplate voltage to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowNomV(IntEnum):
    """
    Set the DER nameplate voltage to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowAmps(IntEnum):
    """
    Set the DER nameplate current to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowVarmaxinj(IntEnum):
    """
    Set the DER nameplate VarMaxInj to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowVarmaxabs(IntEnum):
    """
    Set the DER nameplate VarMaxAbs to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412NameplateLowPF(IntEnum):
    """
    Set the DER nameplate power factor to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsHighNomV(IntEnum):
    """
    Set the DER settings voltage to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsLowAmps(IntEnum):
    """
    Set the DER settings current to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsHighP(IntEnum):
    """
    Set the DER settings power to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsLowP(IntEnum):
    """
    Set the DER settings power to be low

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsHighVAMax(IntEnum):
    """
    Set the DER settings VAMax to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsHighVarmaxinj(IntEnum):
    """
    Set the DER settings VarMaxInj to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412SettingsHighVarmaxabs(IntEnum):
    """
    Set the DER settings VarMaxAbs to be high

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412ChangeCommonModelID(IntEnum):
    """
    Change the common model ID

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412ChangeCommonModelLength(IntEnum):
    """
    Change the common model length

    Members:
        OFF (int): Modbus Falsification Disabled
        ON (int): Modbus Falsification Enabled
    """
    OFF = 0
    ON = 1



class Model64412(SunSpecModel, model_name="DERExploitation", id=64412):
    """
    Operations that represent a hacked DER device

    Attributes:
        DAManipulation (Model64412DAManipulation): Modify the device ID of the DER
        FalsifyDeviceIdentity (Model64412FalsifyDeviceIdentity): Change the DER manufacturer and model
        MeasPAlwaysNameplate (Model64412MeasPAlwaysNameplate): Set the DER meas to always be at nameplate power
        MeasQAlwaysMinimum (Model64412MeasQAlwaysMinimum): Set the DER to always be at minimum reactive power
        MeasQAlwaysMaximum (Model64412MeasQAlwaysMaximum): Set the DER to always be at maximum reactive power
        MeasQAlwaysZero (Model64412MeasQAlwaysZero): Set the DER to always be at zero reactive power
        MeasZeroP (Model64412MeasZeroP): Set the DER to always be at zero P, Q, and S
        MeasInvertQ (Model64412MeasInvertQ): Set the DER to reverse the Q measurement data
        MeasLowV (Model64412MeasLowV): Set the DER to always measure low voltage
        MeasHighV (Model64412MeasHighV): Set the DER to always measure high voltage
        MeasLowL1V (Model64412MeasLowL1V): Set the DER to always measure low line 1 voltage
        MeasHighL1V (Model64412MeasHighL1V): Set the DER to always measure high line 1 voltage
        MeasLowF (Model64412MeasLowF): Set the DER to always measure low frequency
        MeasHighF (Model64412MeasHighF): Set the DER to always measure high frequency
        MeasLowAmps (Model64412MeasLowAmps): Set the DER to always measure low current
        MeasHighAmps (Model64412MeasHighAmps): Set the DER to always measure high current
        MeasHighS (Model64412MeasHighS): Set the DER to always measure high apparent power
        MeasLowS (Model64412MeasLowS): Set the DER to always measure low apparent power
        MeasHighQ (Model64412MeasHighQ): Set the DER to always measure high reactive power
        MeasLowQ (Model64412MeasLowQ): Set the DER to always measure low reactive power
        MeasLowPF (Model64412MeasLowPF): Set the DER to always measure low power factor
        MeasLowReversedPF (Model64412MeasLowReversedPF): Set the DER to always measure low reversed power factor
        NameplateHighP (Model64412NameplateHighP): Set the DER nameplate power to be high
        NameplateLowP (Model64412NameplateLowP): Set the DER nameplate power to be low
        NameplateHighS (Model64412NameplateHighS): Set the DER nameplate apparent power to be high
        NameplateLowS (Model64412NameplateLowS): Set the DER nameplate apparent power to be low
        NameplateHighQ (Model64412NameplateHighQ): Set the DER nameplate reactive power to be high
        NameplateLowQ (Model64412NameplateLowQ): Set the DER nameplate reactive power to be low
        NameplateHighNomV (Model64412NameplateHighNomV): Set the DER nameplate voltage to be high
        NameplateLowNomV (Model64412NameplateLowNomV): Set the DER nameplate voltage to be low
        NameplateLowAmps (Model64412NameplateLowAmps): Set the DER nameplate current to be low
        NameplateLowVarmaxinj (Model64412NameplateLowVarmaxinj): Set the DER nameplate VarMaxInj to be low
        NameplateLowVarmaxabs (Model64412NameplateLowVarmaxabs): Set the DER nameplate VarMaxAbs to be low
        NameplateLowPF (Model64412NameplateLowPF): Set the DER nameplate power factor to be low
        SettingsHighNomV (Model64412SettingsHighNomV): Set the DER settings voltage to be high
        SettingsLowAmps (Model64412SettingsLowAmps): Set the DER settings current to be low
        SettingsHighP (Model64412SettingsHighP): Set the DER settings power to be high
        SettingsLowP (Model64412SettingsLowP): Set the DER settings power to be low
        SettingsHighVAMax (Model64412SettingsHighVAMax): Set the DER settings VAMax to be high
        SettingsHighVarmaxinj (Model64412SettingsHighVarmaxinj): Set the DER settings VarMaxInj to be high
        SettingsHighVarmaxabs (Model64412SettingsHighVarmaxabs): Set the DER settings VarMaxAbs to be high
        ChangeCommonModelID (Model64412ChangeCommonModelID): Change the common model ID
        ChangeCommonModelLength (Model64412ChangeCommonModelLength): Change the common model length
    """

    DAManipulation: Annotated[int, ("SunSpecPoint", {'name': 'DAManipulation', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    FalsifyDeviceIdentity: Annotated[int, ("SunSpecPoint", {'name': 'FalsifyDeviceIdentity', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasPAlwaysNameplate: Annotated[int, ("SunSpecPoint", {'name': 'MeasPAlwaysNameplate', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasQAlwaysMinimum: Annotated[int, ("SunSpecPoint", {'name': 'MeasQAlwaysMinimum', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasQAlwaysMaximum: Annotated[int, ("SunSpecPoint", {'name': 'MeasQAlwaysMaximum', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasQAlwaysZero: Annotated[int, ("SunSpecPoint", {'name': 'MeasQAlwaysZero', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasZeroP: Annotated[int, ("SunSpecPoint", {'name': 'MeasZeroP', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasInvertQ: Annotated[int, ("SunSpecPoint", {'name': 'MeasInvertQ', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowV: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasHighV: Annotated[int, ("SunSpecPoint", {'name': 'MeasHighV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowL1V: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowL1V', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasHighL1V: Annotated[int, ("SunSpecPoint", {'name': 'MeasHighL1V', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowF: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasHighF: Annotated[int, ("SunSpecPoint", {'name': 'MeasHighF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowAmps: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowAmps', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasHighAmps: Annotated[int, ("SunSpecPoint", {'name': 'MeasHighAmps', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasHighS: Annotated[int, ("SunSpecPoint", {'name': 'MeasHighS', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowS: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowS', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasHighQ: Annotated[int, ("SunSpecPoint", {'name': 'MeasHighQ', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowQ: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowQ', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowPF: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowPF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    MeasLowReversedPF: Annotated[int, ("SunSpecPoint", {'name': 'MeasLowReversedPF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateHighP: Annotated[int, ("SunSpecPoint", {'name': 'NameplateHighP', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowP: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowP', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateHighS: Annotated[int, ("SunSpecPoint", {'name': 'NameplateHighS', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowS: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowS', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateHighQ: Annotated[int, ("SunSpecPoint", {'name': 'NameplateHighQ', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowQ: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowQ', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateHighNomV: Annotated[int, ("SunSpecPoint", {'name': 'NameplateHighNomV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowNomV: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowNomV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowAmps: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowAmps', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowVarmaxinj: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowVarmaxinj', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowVarmaxabs: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowVarmaxabs', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    NameplateLowPF: Annotated[int, ("SunSpecPoint", {'name': 'NameplateLowPF', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsHighNomV: Annotated[int, ("SunSpecPoint", {'name': 'SettingsHighNomV', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsLowAmps: Annotated[int, ("SunSpecPoint", {'name': 'SettingsLowAmps', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsHighP: Annotated[int, ("SunSpecPoint", {'name': 'SettingsHighP', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsLowP: Annotated[int, ("SunSpecPoint", {'name': 'SettingsLowP', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsHighVAMax: Annotated[int, ("SunSpecPoint", {'name': 'SettingsHighVAMax', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsHighVarmaxinj: Annotated[int, ("SunSpecPoint", {'name': 'SettingsHighVarmaxinj', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    SettingsHighVarmaxabs: Annotated[int, ("SunSpecPoint", {'name': 'SettingsHighVarmaxabs', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ChangeCommonModelID: Annotated[int, ("SunSpecPoint", {'name': 'ChangeCommonModelID', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]
    ChangeCommonModelLength: Annotated[int, ("SunSpecPoint", {'name': 'ChangeCommonModelLength', 'ptype': 'uint16', 'mandatory': False, 'static': False, 'access': 'RW'})]

