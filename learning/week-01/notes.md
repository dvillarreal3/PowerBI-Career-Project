Week 1 notes — Environment setup & verification

What step 4 did
- pytest: ran the test suite. The smoke test (tests/test_smoke.py) asserts True; passing confirms Python, venv, and pytest are working.
- flake8: static code analyzer (linter) that flags style issues and simple errors. The CI step runs flake8 if installed; local run helps keep code clean.

Commands you executed
- python -m venv .venv
- .\.venv\Scripts\Activate.ps1
- pip install -r requirements.txt
- pytest -q
- flake8

Why this matters
- Virtual env isolates dependencies.
- Pytest validates tests; start small (smoke) then add real tests.
- Linting prevents common bugs and enforces consistency.

Resources
- Python venv: https://docs.python.org/3/library/venv.html
- Pytest docs: https://docs.pytest.org/
- Flake8: https://flake8.pycqa.org/
- Tutorial: Real Python - Testing and Virtual Envs

Next tasks for Week 1
- Create README developer setup steps
- Add example script and unit tests (created: src/etl_utils.py, tests/test_etl_utils.py)
- Commit and push branch week-1-setup

Sample module: src/etl_utils.py
- Function: clean_amount(s) -> float|None
- Purpose: Parse monetary strings to floats; robust to currency symbols and comma separators.
- How to run tests: Activate venv, then run `pytest -q` in project root.
- Why: Unit tests validate edge cases and ensure future refactors don't break behavior.

Notes on TDD and testing practice
- Start with a failing test to specify expected behavior, then implement minimal code to pass tests.
- Keep tests small and deterministic (no network calls).
- Use pytest's parametrize to expand cases later.

Resources for testing
- Pytest: https://docs.pytest.org/
- Testing in Python (Real Python): https://realpython.com/pytest-python-testing/

Questions & answers
Q: Are tests connecting to another data source or hardwired?
A: These unit tests are hardwired — they call functions with example inputs (strings, numbers). They don't hit external systems. This is intentional: unit tests verify function correctness in isolation. Integration or end-to-end tests can exercise live or staging data and external services.

Q: Why test on hardcoded values rather than live data?
A: Hardcoded tests are deterministic, fast, and repeatable — ideal for CI. Live-data tests are useful for validating end-to-end behavior but are slower, flaky, and require environment setup. Production pipelines typically have both: unit tests for logic, integration tests for systems.

Q: How do tests and src relate? Why imports work without cache files?
A: Tests import modules from the project root (e.g., import src.etl_utils). Python adds project root to sys.path when running pytest, so 'src' is importable. __pycache__ contains compiled .pyc files — optional and recreated automatically; tests use source .py files.

Added artifacts (run/test):
- Docstring doctests are enabled via tests/test_doctests.py and run with pytest.
- Sample data: data/sample_transactions.csv — demonstrates parsing across locales.
- Demo script: scripts/parse_sample.py — run to show parsing output.

Next steps
- Run `python -m pytest -q` to execute unit + doctest checks.
- Run `python scripts\parse_sample.py` to see parsing of sample CSV.

