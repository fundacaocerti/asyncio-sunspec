"""Package-level smoke tests."""

import async_sunspec


def test_package_is_importable() -> None:
    """Importing the package should succeed."""
    assert async_sunspec is not None
