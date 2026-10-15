import math

import pytest

from bell.entropy import randomness_bound


def test_no_violation_gives_zero():
    assert randomness_bound(2.0) == 0.0
    assert randomness_bound(0.0) == 0.0
    assert randomness_bound(float("nan")) == 0.0


def test_tsirelson_gives_one_bit():
    assert randomness_bound(2 * math.sqrt(2)) == pytest.approx(1.0)
    assert randomness_bound(10.0) == pytest.approx(1.0)


def test_monotonic():
    values = [randomness_bound(s) for s in (2.1, 2.4, 2.7, 2.8)]
    assert values == sorted(values)
