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


class Model801(SunSpecModel, model_name="storage", id=801):
    """
    This model has been deprecated.

    Attributes:
        DEPRECATED (int): This model has been deprecated.
    """

    DEPRECATED: Annotated[int, ("SunSpecPoint", {'name': 'DEPRECATED', 'ptype': 'uint16', 'mandatory': True, 'static': False})]

