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


class Model64112CC_Config_MPPT_mode(IntEnum):
    """
    Members:
        Auto (int): Auto
        U_Pick (int): U_Pick
        Wind (int): Wind
    """
    Auto = 0
    U_Pick = 1
    Wind = 2



class Model64112CC_Config_sweep_width(IntEnum):
    """
    Members:
        Half (int): Half
        Full (int): Full
    """
    Half = 0
    Full = 1



class Model64112CC_Config_sweep_max(IntEnum):
    """
    Members:
        Eighty_Percent (int): Eighty_Percent
        Eighty_Five_Percent (int): Eighty_Five_Percent
        Ninty_Percent (int): Ninty_Percent
        Ninty_Nine_Percent (int): Ninty_Nine_Percent
    """
    Eighty_Percent = 0
    Eighty_Five_Percent = 1
    Ninty_Percent = 2
    Ninty_Nine_Percent = 3



class Model64112CC_Config_grid_tie(IntEnum):
    """
    Members:
        Disabled (int): Disabled
        Enabled (int): Enabled
    """
    Disabled = 0
    Enabled = 1



class Model64112CC_Config_temp_comp(IntEnum):
    """
    Members:
        Wide (int): Wide
        Limited (int): Limited
    """
    Wide = 0
    Limited = 1



class Model64112CC_Config_auto_restart(IntEnum):
    """
    Members:
        Off (int): Off
        Every_90_Minutes (int): Every_90_Minutes
        Every_90_Minutes_if_Absorb_or_Float (int): Every_90_Minutes_if_Absorb_or_Float
    """
    Off = 0
    Every_90_Minutes = 1
    Every_90_Minutes_if_Absorb_or_Float = 2



class Model64112CC_Config_AUX_mode(IntEnum):
    """
    Members:
        Float (int): Float
        Diversion_Relay (int): Diversion_Relay
        Diversion_Solid_St (int): Diversion_Solid_St
        Low_Batt_Disconnect (int): Low_Batt_Disconnect
        Remote (int): Remote
        Vent_Fan (int): Vent_Fan
        PV_Trigger (int): PV_Trigger
        Error_Output (int): Error_Output
        Night_Light (int): Night_Light
    """
    Float = 0
    Diversion_Relay = 1
    Diversion_Solid_St = 2
    Low_Batt_Disconnect = 3
    Remote = 4
    Vent_Fan = 5
    PV_Trigger = 6
    Error_Output = 7
    Night_Light = 8



class Model64112CC_Config_AUX_control(IntEnum):
    """
    Members:
        Off (int): Off
        Auto (int): Auto
        On (int): On
    """
    Off = 0
    Auto = 1
    On = 2



class Model64112CC_Config_AUX_state(IntEnum):
    """
    Members:
        Disabled (int): Disabled
        Enabled (int): Enabled
    """
    Disabled = 0
    Enabled = 1



class Model64112CC_Config_AUX_polarity(IntEnum):
    """
    Members:
        Low (int): Low
        High (int): High
    """
    Low = 0
    High = 1



class Model64112(SunSpecModel, model_name="model_64112", id=64112):
    """
    Attributes:
        Port (int)
        V_SF (int)
        C_SF (int)
        H_SF (int)
        P_SF (int)
        AH_SF (int)
        KWH_SF (int)
        CC_Config_fault (int)
        CC_Config_absorb_V (int)
        CC_Config_absorb_Hr (int)
        CC_Config_absorb_End_A (int)
        CC_Config_rebulk_V (int)
        CC_Config_float_V (int)
        CC_Config_max_Chg_A (int)
        CC_Config_equalize_V (int)
        CC_Config_equalize_Hr (int)
        CC_Config_auto_equalize (int)
        CC_Config_MPPT_mode (Model64112CC_Config_MPPT_mode)
        CC_Config_sweep_width (Model64112CC_Config_sweep_width)
        CC_Config_sweep_max (Model64112CC_Config_sweep_max)
        CC_Config_U_Pick_Duty_cyc (int)
        CC_Config_grid_tie (Model64112CC_Config_grid_tie)
        CC_Config_temp_comp (Model64112CC_Config_temp_comp)
        CC_Config_temp_comp_llimt (int)
        CC_Config_temp_comp_hlimt (int)
        CC_Config_auto_restart (Model64112CC_Config_auto_restart)
        CC_Config_wakeup_VOC (int)
        CC_Config_snooze_mode_A (int)
        CC_Config_wakeup_interval (int)
        CC_Config_AUX_mode (Model64112CC_Config_AUX_mode)
        CC_Config_AUX_control (Model64112CC_Config_AUX_control)
        CC_Config_AUX_state (Model64112CC_Config_AUX_state)
        CC_Config_AUX_polarity (Model64112CC_Config_AUX_polarity)
        CC_Config_AUX_L_Batt_disc (int)
        CC_Config_AUX_L_Batt_rcon (int)
        CC_Config_AUX_L_Batt_dly (int)
        CC_Config_AUX_Vent_fan_V (int)
        CC_Config_AUX_PV_triggerV (int)
        CC_Config_AUX_PV_trg_h_tm (int)
        CC_Config_AUX_Nlite_ThrsV (int)
        CC_Config_AUX_Nlite_On_tm (int)
        CC_Config_AUX_Nlite_On_hist (int)
        CC_Config_AUX_Nlite_Off_hist (int)
        CC_Config_AUX_Error_batt_V (int)
        CC_Config_AUX_Divert_h_time (int)
        CC_Config_AUX_Divert_dly_time (int)
        CC_Config_AUX_Divert_Rel_V (int)
        CC_Config_AUX_Divert_Hyst_V (int)
        CC_Config_MajorFWRev (int)
        CC_Config_MidFWRev (int)
        CC_Config_MinorFWRev (int)
        CC_Config_DataLog_Day_offset (int)
        CC_Config_DataLog_Cur_Day_off (int)
        CC_Config_DataLog_Daily_AH (int)
        CC_Config_DataLog_Daily_KWH (int)
        CC_Config_DataLog_Max_Out_A (int)
        CC_Config_DataLog_Max_Out_W (int)
        CC_Config_DataLog_Absorb_T (int)
        CC_Config_DataLog_Float_T (int)
        CC_Config_DataLog_Min_Batt_V (int)
        CC_Config_DataLog_Max_Batt_V (int)
        CC_Config_DataLog_Max_Input_V (int)
        CC_Config_DataLog_Clear (int)
        CC_Config_DataLog_Clr_Comp (int)
    """

    Port: Annotated[int, ("SunSpecPoint", {'name': 'Port', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    C_SF: Annotated[int, ("SunSpecPoint", {'name': 'C_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    H_SF: Annotated[int, ("SunSpecPoint", {'name': 'H_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    P_SF: Annotated[int, ("SunSpecPoint", {'name': 'P_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    AH_SF: Annotated[int, ("SunSpecPoint", {'name': 'AH_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    KWH_SF: Annotated[int, ("SunSpecPoint", {'name': 'KWH_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    CC_Config_fault: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_fault', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_absorb_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_absorb_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_absorb_Hr: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_absorb_Hr', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: H_SF
    CC_Config_absorb_End_A: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_absorb_End_A', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_rebulk_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_rebulk_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_float_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_float_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_max_Chg_A: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_max_Chg_A', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_equalize_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_equalize_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_equalize_Hr: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_equalize_Hr', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_auto_equalize: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_auto_equalize', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_MPPT_mode: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_MPPT_mode', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_sweep_width: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_sweep_width', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_sweep_max: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_sweep_max', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_U_Pick_Duty_cyc: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_U_Pick_Duty_cyc', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_grid_tie: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_grid_tie', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_temp_comp: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_temp_comp', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_temp_comp_llimt: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_temp_comp_llimt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_temp_comp_hlimt: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_temp_comp_hlimt', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_auto_restart: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_auto_restart', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_wakeup_VOC: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_wakeup_VOC', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_snooze_mode_A: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_snooze_mode_A', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_wakeup_interval: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_wakeup_interval', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_mode: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_mode', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_control: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_control', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_state: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_state', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_polarity: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_polarity', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_L_Batt_disc: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_L_Batt_disc', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_L_Batt_rcon: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_L_Batt_rcon', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_L_Batt_dly: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_L_Batt_dly', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_Vent_fan_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Vent_fan_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_PV_triggerV: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_PV_triggerV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_PV_trg_h_tm: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_PV_trg_h_tm', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_Nlite_ThrsV: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Nlite_ThrsV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_Nlite_On_tm: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Nlite_On_tm', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: H_SF
    CC_Config_AUX_Nlite_On_hist: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Nlite_On_hist', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_Nlite_Off_hist: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Nlite_Off_hist', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_Error_batt_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Error_batt_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_Divert_h_time: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Divert_h_time', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_Divert_dly_time: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Divert_dly_time', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_AUX_Divert_Rel_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Divert_Rel_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_AUX_Divert_Hyst_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_AUX_Divert_Hyst_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_MajorFWRev: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_MajorFWRev', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_MidFWRev: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_MidFWRev', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_MinorFWRev: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_MinorFWRev', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Day_offset: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Day_offset', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Cur_Day_off: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Cur_Day_off', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Daily_AH: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Daily_AH', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Daily_KWH: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Daily_KWH', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: KWH_SF
    CC_Config_DataLog_Max_Out_A: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Max_Out_A', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_DataLog_Max_Out_W: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Max_Out_W', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_DataLog_Absorb_T: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Absorb_T', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Float_T: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Float_T', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Min_Batt_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Min_Batt_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_DataLog_Max_Batt_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Max_Batt_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_DataLog_Max_Input_V: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Max_Input_V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CC_Config_DataLog_Clear: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Clear', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    CC_Config_DataLog_Clr_Comp: Annotated[int, ("SunSpecPoint", {'name': 'CC_Config_DataLog_Clr_Comp', 'ptype': 'uint16', 'mandatory': True, 'static': False})]

