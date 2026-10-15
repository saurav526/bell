import math

import matplotlib

matplotlib.use("Agg")

import pytest  # noqa: E402

from bell.cli import main  # noqa: E402
from bell.plots import show_results  # noqa: E402
from bell.runner import run_chsh  # noqa: E402


def test_entangled_violates_bound():
    r = run_chsh(shots=4000, visibility=1.0, seed=1)
    assert r.s_value == pytest.approx(2 * math.sqrt(2), abs=0.15)
    assert r.s_value > 2.0
    assert r.entropy_bound > 0.0


def test_low_visibility_no_violation():
    r = run_chsh(shots=4000, visibility=0.6, seed=1)
    assert r.s_value < 2.0
    assert r.entropy_bound == 0.0


def test_product_state_respects_local_bound():
    r = run_chsh(shots=4000, product_state=True, seed=1)
    assert r.s_value <= 2.1


def test_cli_and_plot(capsys, monkeypatch):
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    assert main(["--shots", "500", "--seed", "3", "--plot"]) == 0
    assert "CHSH S" in capsys.readouterr().out
    show_results(0.9, measured_s=2.5)
