Week 1 — Project setup & Git

Objectives: Initialize GitHub repo, learn branching, PR workflow, basic CI. Set up local dev environment (Python, dbt-core, DuckDB), Power BI Desktop.

Deliverables: GitHub repo skeleton, README, .gitignore, simple CI that lints Python and runs a smoke test.

Skills: Git/GitHub, GitHub Actions, repo organization (meta), environment setup (hard).

Tasks
- Create and activate a virtual environment
- Install requirements (pytest, flake8)
- Run pytest to confirm test runner
- Run flake8 to check style
- Create branch week-1-setup and push
- Document developer setup in learning/week-01/notes.md

Acceptance criteria
- Tests pass locally (pytest -q)
- CI workflow passes on push
- Clear README with setup steps