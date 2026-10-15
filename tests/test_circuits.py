import math

import pytest

from bell.circuits import SETTING_PAIRS, build_circuit, exact_chsh, exact_correlation


def test_exact_chsh_is_tsirelson():
    assert exact_chsh() == pytest.approx(2 * math.sqrt(2))


@pytest.mark.parametrize(("a", "b"), SETTING_PAIRS)
def test_correlation_is_cos_difference(a, b):
    assert exact_correlation(a, b) == pytest.approx(math.cos(a - b))


def test_circuit_shape():
    qc = build_circuit(0.0, 0.0)
    assert qc.num_qubits == 2
    assert qc.num_clbits == 2
    names = [i.operation.name for i in build_circuit(0, 0, product_state=True).data]
    assert "cx" not in names
