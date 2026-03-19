"""Reusable model fixtures for async_sunspec unit tests."""

from typing import Annotated

from async_sunspec.group import SunSpecGroup, SunSpecRepeatingBlock
from async_sunspec.model import SunSpecModel


class Model420Group(SunSpecGroup):
    """Small group used by tests that validate repeating blocks."""

    f1: Annotated[
        int,
        ("SunSpecPoint", {"name": "f1", "ptype": "uint16", "value": 0}),
    ]
    f2: Annotated[
        str,
        ("SunSpecPoint", {"name": "f2", "ptype": "string", "size": 8}),
    ]


class FooModel(SunSpecModel, model_name="test_model_420", id=0x0420):
    """Simple test model used across unit tests."""

    foo: Annotated[
        int,
        ("SunSpecPoint", {"name": "foo", "ptype": "uint16", "value": 0}),
    ]
    bar: Annotated[
        int,
        (
            "SunSpecPoint",
            {"name": "bar", "ptype": "int32", "value": 2, "static": True},
        ),
    ]
    zoo: Annotated[
        int,
        (
            "SunSpecPoint",
            {"name": "zoo", "ptype": "uint32", "value": 3, "mandatory": False},
        ),
    ]
    txt: Annotated[
        str,
        ("SunSpecPoint", {"name": "txt", "ptype": "string", "size": 8}),
    ]
    cnt: Annotated[
        int,
        ("SunSpecPoint", {"name": "cnt", "ptype": "uint16", "value": 0}),
    ]
    grp: Annotated[
        SunSpecRepeatingBlock[Model420Group],
        (
            "SunSpecRepeatingBlock",
            {
                "name": "grp",
                "ptype": "group",
                "group_type": Model420Group,
                "counter": "cnt",
            },
        ),
    ]
