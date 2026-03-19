SPHINXBUILD = sphinx-build
SOURCEDIR = .
BUILDDIR = _build

.PHONY: apidoc html

apidoc:
	sphinx-apidoc -f -e -o _generated ../src/async_sunspec

html:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"
