import math

import pytest

from bell.chsh import (
    chsh_from_correlations,
    correlation,
    model_correlations,
    standard_error,
)


def test_correlation_perfect_and_anti():
    assert correlation({"00": 50, "11": 50}) == 1.0
    assert correlation({"01": 30, "10": 70}) == -1.0


def test_correlation_mixed_and_spaces():
    assert correlation({"0 0": 75, "01": 25}) == pytest.approx(0.5)


def test_correlation_errors():
    with pytest.raises(ValueError):
        correlation({})
    with pytest.raises(ValueError):
        correlation({"0": 10})


def test_chsh_sum():
    assert chsh_from_correlations([1, 1, 1, -1]) == 4.0
    with pytest.raises(ValueError):
        chsh_from_correlations([1, 1])


def test_visibility_scaling():
    assert model_correlations([1.0, -0.5], 0.5) == [0.5, -0.25]
    with pytest.raises(ValueError):
        model_correlations([1.0], 1.5)


def test_standard_error():
    assert standard_error([1, 1, 1, 1], 100) == 0.0
    assert standard_error([0, 0, 0, 0], 100) == pytest.approx(math.sqrt(4 / 100))
    with pytest.raises(ValueError):
        standard_error([0] * 4, 0)
