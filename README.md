# Bell Test and Randomness Lab

[![CI](https://github.com/<your-username>/bell-test-randomness-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/bell-test-randomness-lab/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Qiskit](https://img.shields.io/badge/built%20with-Qiskit-6929C4)

A small, well-tested Qiskit lab that simulates a **CHSH Bell test**, models
noise through *visibility*, propagates shot-noise errors, and shows an
**illustrative min-entropy bound** derived from the CHSH value.

> ⚠️ **Educational tool.** Outputs are simulation and theory. They are **not** a
> certification of randomness and must not be used for cryptography.

## Features

- Bell-state (|Φ⁺⟩) circuits with configurable measurement angles
- Exact ideal CHSH value from statevectors (S = 2√2)
- Shot-based estimates on the Aer simulator, with standard-error propagation
- Visibility (white-noise) model: S = 2√2 · v, violation threshold v = 1/√2
- Product-state control experiment (must respect S ≤ 2)
- Theory plots of Bell violation and the min-entropy bound
- `bell-lab` command-line interface

## Installation

```bash
git clone https://github.com/<your-username>/bell-test-randomness-lab.git
cd bell-test-randomness-lab
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Quick start

```bash
bell-lab --shots 8192 --visibility 0.9 --seed 7 --plot
```

Or from Python:

```python
from bell.runner import run_chsh

result = run_chsh(shots=8192, visibility=0.9, seed=42)
print(result.s_value, result.std_error, result.entropy_bound)
```

## Project structure

```
.
├── .claude/              # Claude Code project guide, settings and commands
├── .github/              # CI workflow, issue/PR templates, Dependabot
├── docs/                 # Theory and architecture notes
├── examples/             # Runnable usage examples
├── src/bell/
│   ├── chsh.py           # Correlations, CHSH sum, visibility, shot noise
│   ├── circuits.py       # Circuits and exact CHSH calculation
│   ├── entropy.py        # Min-entropy bound
│   ├── plots.py          # Matplotlib theory plots
│   ├── runner.py         # Simulation driver
│   └── cli.py            # Command-line entry point
├── tests/                # pytest suite
├── pyproject.toml
├── requirements.txt
└── Makefile
```

## Development

```bash
make test     # run tests with coverage
make lint     # ruff
make format   # auto-format
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/theory.md](docs/theory.md).

## Theory in brief

| Quantity | Value |
|----------|-------|
| Classical (local) bound | S ≤ 2 |
| Ideal quantum value | S = 2√2 ≈ 2.828 |
| Violation threshold (visibility) | v > 1/√2 ≈ 0.707 |
| Entropy bound | H_min ≥ 1 − log₂(1 + √(2 − S²/4)) |

## License

MIT, see [LICENSE](LICENSE).
