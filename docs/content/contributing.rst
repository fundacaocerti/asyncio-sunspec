Contributing
============

Thanks for your interest in contributing! The following guidelines will help
your contribution be reviewed and merged more quickly.

Guidelines
----------

1. Report an issue first

   - If possible, open an issue describing the bug or feature and include
     steps to reproduce or a clear design proposal.

2. Branching and commits

   - We follow the Gitflow branching model: use ``develop`` as the main
     integration branch and keep ``master`` reserved for tagged releases.
     Create topic branches from ``develop`` named ``feature/...``,
     ``fix/...`` or ``hotfix/...`` as appropriate.

   - Keep commits small and focused. Use clear, imperative commit messages
     and squash or rebase locally to keep topic branches tidy before PRs.

3. Tests

   - Add unit tests for bug fixes and new features. Run the test suite locally 
     with ``python -m pytest -q``.

4. Style and linting

   - The project uses ``ruff``. Run ``ruff check src tests`` before submitting.
   - Formatting can be applied with ``ruff format src tests``.

5. Documentation

   - Update the ``docs/`` tree for user-facing changes and add developer notes
     in ``docs/content/`` for deeper explanations.

6. Pull requests

   - Open a PR against ``develop`` with a clear description and link to any
     related issues. Include test and docs updates where appropriate.

   - Exceptions: for urgent fixes that must go directly into a released
     version, open a PR against ``master`` as a ``hotfix`` and follow the
     project's release process.

7. CI and checks

   - Ensure all CI checks (tests, linters) pass before requesting review.

License
-------
By contributing you agree that your contributions will be licensed under the
project's existing license (see ``LICENSE.md``).
