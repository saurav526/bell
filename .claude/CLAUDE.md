# Project guide for Claude Code

Bell Test and Randomness Lab: a Qiskit CHSH simulator with an illustrative
min-entropy bound. Educational only, never a certification of randomness.

## Layout
- `src/bell/chsh.py` - correlation, CHSH sum, visibility mixing, shot-noise error
- `src/bell/circuits.py` - Phi+ circuits, angle settings, exact statevector CHSH
- `src/bell/entropy.py` - theoretical min-entropy bound
- `src/bell/runner.py` - Aer simulation driver (`run_chsh`)
- `src/bell/plots.py` - matplotlib theory plots
- `src/bell/cli.py` - `bell-lab` entry point
- `tests/` - pytest suite

## Commands
- Install: `make install`
- Test: `make test`
- Lint/format: `make lint` / `make format`

## Conventions
- CHSH convention: S = E00 + E01 + E10 - E11; ideal S = 2*sqrt(2).
- Observable is cos(theta) Z + sin(theta) X; measure via RY(-theta) then Z.
- q0 = Alice, q1 = Bob; use the last two bits of a count key.
- Keep wording honest: results are simulation/theory, not certification.
- Add a test for every behaviour change.
