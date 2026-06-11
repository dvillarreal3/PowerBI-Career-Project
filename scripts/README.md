Running scripts in this repo

Recommended (module mode)
- From project root, activate venv and run:
  python -m scripts.parse_sample

Direct script mode (ensure imports work)
- From project root:
  $env:PYTHONPATH = '.'
  python .\scripts\parse_sample.py

Developer notes
- Pytest adds the project root to sys.path; running scripts directly may not.
- Packaging the scripts folder (adding __init__.py) lets you run scripts as modules which uses package imports.
- To inspect Python path: python -c "import sys; print('\n'.join(sys.path))"
