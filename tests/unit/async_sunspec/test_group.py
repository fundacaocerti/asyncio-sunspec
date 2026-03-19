from array import array

import pytest

from tests.unit.async_sunspec._fixtures import FooModel


def _build_element(model: FooModel, value: int, text: str):
    """Create a repeating-block element with deterministic content."""
    element = model.grp.create_element()
    element.f1 = value
    element.f2 = text
    return element


def test_repeating_block_rejects_elements_with_wrong_type() -> None:
    """Reject repeating-block elements that do not match the block type."""
    model = FooModel()

    with pytest.raises(TypeError):
        model.grp.add_element(object())


def test_repeating_block_clear_resets_element_count() -> None:
    """Clear all repeating-block elements and reset the counter point."""
    model = FooModel()
    model.grp.add_element(_build_element(model, 1, "A"))
    model.grp.add_element(_build_element(model, 2, "B"))

    model.grp.clear_elements()

    assert 0 == len(model.grp)
    assert 0 == model.cnt


def test_repeating_block_delete_updates_counter() -> None:
    """Track counter point updates when deleting block elements."""
    model = FooModel()
    model.grp.add_element(_build_element(model, 1, "A"))
    model.grp.add_element(_build_element(model, 2, "B"))

    del model.grp[0]

    assert 1 == len(model.grp)
    assert 1 == model.cnt


def test_repeating_block_rejects_mutation_when_locked() -> None:
    """Disallow add/remove/clear operations after block lock."""
    model = FooModel()
    model.grp.add_element(_build_element(model, 1, "A"))
    model.grp.lock()

    with pytest.raises(RuntimeError):
        model.grp.add_element(_build_element(model, 2, "B"))
    with pytest.raises(RuntimeError):
        model.grp.clear_elements()
    with pytest.raises(RuntimeError):
        model.grp.remove_element(0)


def test_repeating_block_getitem_rejects_out_of_range_index() -> None:
    """Raise IndexError for invalid repeating-block indexes."""
    model = FooModel()

    with pytest.raises(IndexError):
        _ = model.grp[0]


def test_group_read_from_register_rebuilds_repeating_elements() -> None:
    """Read repeating-block element data from a bound register buffer."""
    source = FooModel()
    source.grp.add_element(_build_element(source, 1, "A"))
    source.grp.add_element(_build_element(source, 2, "B"))
    source_length = source.process_elements()
    register = array("H", [0] * source_length)
    source.bind_register(register)
    source.foo = 77
    source.grp[0].f1 = 10
    source.grp[1].f1 = 20

    restored = FooModel()
    restored.read_from_register(register)

    assert 77 == restored.foo
    assert 2 == restored.cnt
    assert 2 == len(restored.grp)
    assert 10 == restored.grp[0].f1
    assert 20 == restored.grp[1].f1
