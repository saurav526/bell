# Contributing

Thanks for your interest in improving Bell Test and Randomness Lab!

## Setup
```bash
git clone https://github.com/<you>/bell-test-randomness-lab.git
cd bell-test-randomness-lab
python -m venv .venv && source .venv/bin/activate
make install
pre-commit install
```

## Workflow
1. Create a branch: `git checkout -b feat/my-change`
2. Make changes and add tests in `tests/`.
3. Run `make lint` and `make test`.
4. Open a pull request using the template.

## Style
- Python 3.10+, formatted and linted with Ruff.
- Docstrings on public functions; keep the physics conventions stated in
  `docs/theory.md` consistent.
- Conventional commit messages (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
