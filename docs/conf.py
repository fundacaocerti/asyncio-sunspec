"""Sphinx configuration for the async-sunspec project.

This file configures Sphinx to import the package from the repository's
``src/`` directory and enables commonly-used extensions for autodoc and
Google-style docstring support (``napoleon``).
"""
from __future__ import annotations

import os
import sys

# Ensure the package in `src/` is importable by Sphinx autodoc.
sys.path.insert(0, os.path.abspath("../src"))

project = "async-sunspec"
author = "CERTI Foundation"
release = "0.1.0"
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "show-inheritance": True,
    "inherited-members": True,
}

autodoc_typehints = "description"
napoleon_google_docstring = True
autosummary_generate = True
autosummary_imported_members = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = f"{project} v{release} documentation"
html_logo = "_static/async-sunspec.png"

# Explicit master doc (Sphinx 4+ defaults to 'index' but be explicit).
master_doc = "index"
