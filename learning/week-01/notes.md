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
- Add example script and a unit test for it
- Commit and push branch week-1-setup
