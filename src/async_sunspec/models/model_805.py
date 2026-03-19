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
from enum import IntFlag


class Model805CellSt(IntFlag):
    """
    Status of the cell.

    Members:
        CELL_IS_BALANCING (int): CELL_IS_BALANCING
    """
    CELL_IS_BALANCING = 1 << 0



class Model805LithiumIonModuleCellGroup(SunSpecGroup):
    """
    Attributes:
        CellV (int): Cell terminal voltage.
        CellTmp (int): Cell temperature.
        CellSt (Model805CellSt): Status of the cell.
    """

    CellV: Annotated[int, ("SunSpecPoint", {'name': 'CellV', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    CellTmp: Annotated[int, ("SunSpecPoint", {'name': 'CellTmp', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    CellSt: Annotated[int, ("SunSpecPoint", {'name': 'CellSt', 'ptype': 'uint32', 'mandatory': False, 'static': False})]


class Model805(SunSpecModel, model_name="lithium-ion-module", id=805):
    """
    Attributes:
        StrIdx (int): Index of the string containing the module.
        ModIdx (int): Index of the module within the string.
        NCell (int): Count of all cells in the module.
        SoC (int): Module state of charge, expressed as a percentage.
        DoD (int): Depth of discharge for the module.
        SoH (int): Module state of health, expressed as a percentage.
        NCyc (int): Count of cycles executed.
        V (int): Voltage of the module.
        CellVMax (int): Maximum voltage for all cells in the module.
        CellVMaxCell (int): Cell with the maximum voltage.
        CellVMin (int): Minimum voltage for all cells in the module.
        CellVMinCell (int): Cell with the minimum voltage.
        CellVAvg (int): Average voltage for all cells in the module.
        CellTmpMax (int): Maximum temperature for all cells in the module.
        CellTmpMaxCell (int): Cell with the maximum cell temperature.
        CellTmpMin (int): Minimum temperature for all cells in the module.
        CellTmpMinCell (int): Cell with the minimum cell temperature.
        CellTmpAvg (int): Average temperature for all cells in the module.
        NCellBal (int): Number of cells currently being balanced in the module.
        SN (str): Serial number for the module.
        SoC_SF (int): Scale factor for module state of charge.
        SoH_SF (int): Scale factor for module state of health.
        DoD_SF (int): Scale factor for module depth of discharge.
        V_SF (int): Scale factor for module voltage.
        CellV_SF (int): Scale factor for cell voltage.
        Tmp_SF (int): Scale factor for module temperature.
    """

    StrIdx: Annotated[int, ("SunSpecPoint", {'name': 'StrIdx', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    ModIdx: Annotated[int, ("SunSpecPoint", {'name': 'ModIdx', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    NCell: Annotated[int, ("SunSpecPoint", {'name': 'NCell', 'ptype': 'uint16', 'mandatory': True, 'static': False})]
    SoC: Annotated[int, ("SunSpecPoint", {'name': 'SoC', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoC_SF
    DoD: Annotated[int, ("SunSpecPoint", {'name': 'DoD', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: DoD_SF
    SoH: Annotated[int, ("SunSpecPoint", {'name': 'SoH', 'ptype': 'uint16', 'mandatory': False, 'static': False})]  # sf: SoH_SF
    NCyc: Annotated[int, ("SunSpecPoint", {'name': 'NCyc', 'ptype': 'uint32', 'mandatory': False, 'static': False})]
    V: Annotated[int, ("SunSpecPoint", {'name': 'V', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: V_SF
    CellVMax: Annotated[int, ("SunSpecPoint", {'name': 'CellVMax', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    CellVMaxCell: Annotated[int, ("SunSpecPoint", {'name': 'CellVMaxCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVMin: Annotated[int, ("SunSpecPoint", {'name': 'CellVMin', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    CellVMinCell: Annotated[int, ("SunSpecPoint", {'name': 'CellVMinCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellVAvg: Annotated[int, ("SunSpecPoint", {'name': 'CellVAvg', 'ptype': 'uint16', 'mandatory': True, 'static': False})]  # sf: CellV_SF
    CellTmpMax: Annotated[int, ("SunSpecPoint", {'name': 'CellTmpMax', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    CellTmpMaxCell: Annotated[int, ("SunSpecPoint", {'name': 'CellTmpMaxCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellTmpMin: Annotated[int, ("SunSpecPoint", {'name': 'CellTmpMin', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    CellTmpMinCell: Annotated[int, ("SunSpecPoint", {'name': 'CellTmpMinCell', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    CellTmpAvg: Annotated[int, ("SunSpecPoint", {'name': 'CellTmpAvg', 'ptype': 'int16', 'mandatory': True, 'static': False})]  # sf: Tmp_SF
    NCellBal: Annotated[int, ("SunSpecPoint", {'name': 'NCellBal', 'ptype': 'uint16', 'mandatory': False, 'static': False})]
    SN: Annotated[str, ("SunSpecPoint", {'name': 'SN', 'ptype': 'string', 'size': 16, 'mandatory': False, 'static': False})]
    SoC_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoC_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    SoH_SF: Annotated[int, ("SunSpecPoint", {'name': 'SoH_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    DoD_SF: Annotated[int, ("SunSpecPoint", {'name': 'DoD_SF', 'ptype': 'sunssf', 'mandatory': False, 'static': False})]
    V_SF: Annotated[int, ("SunSpecPoint", {'name': 'V_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    CellV_SF: Annotated[int, ("SunSpecPoint", {'name': 'CellV_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    Tmp_SF: Annotated[int, ("SunSpecPoint", {'name': 'Tmp_SF', 'ptype': 'sunssf', 'mandatory': True, 'static': False})]
    lithium_ion_module_cell: Annotated[Model805LithiumIonModuleCellGroup, ("SunSpecGroup", {"name": "lithium_ion_module_cell", "group_type": Model805LithiumIonModuleCellGroup})]

