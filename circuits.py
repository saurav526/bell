"""Circuit construction and exact ideal CHSH calculation."""

import math

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

A0 = 0.0
A1 = math.pi / 2
B0 = math.pi / 4
B1 = -math.pi / 4

SETTING_PAIRS = [
    (A0, B0),
    (A0, B1),
    (A1, B0),
    (A1, B1),
]


def build_circuit(theta_a, theta_b, product_state=False):
    """Measure local observables cos(theta) Z + sin(theta) X.

    Prepare |Phi+> = (|00> + |11>)/sqrt(2), unless a product-state
    control is requested. RY(-theta) followed by Z measurement realizes
    the stated observable. q0 is Alice; q1 is Bob.
    """
    qc = QuantumCircuit(2, 2)
    if not product_state:
        qc.h(0)
        qc.cx(0, 1)

    qc.ry(-float(theta_a), 0)
    qc.ry(-float(theta_b), 1)
    qc.measure(0, 0)
    qc.measure(1, 1)
    return qc


def exact_correlation(theta_a, theta_b):
    """Compute ideal correlation from an unmeasured statevector."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.ry(-float(theta_a), 0)
    qc.ry(-float(theta_b), 1)
    state = Statevector.from_instruction(qc)
    probabilities = state.probabilities_dict()
    expectation = 0.0
    for bitstring, probability in probabilities.items():
        bits = bitstring.replace(" ", "")
        expectation += (
            (1.0 if bits[-1] == bits[-2] else -1.0) * probability
        )
    return float(expectation)


def exact_chsh():
    """Return the exact ideal CHSH value for the selected angle convention."""
    e00 = exact_correlation(A0, B0)
    e01 = exact_correlation(A0, B1)
    e10 = exact_correlation(A1, B0)
    e11 = exact_correlation(A1, B1)
    return e00 + e01 + e10 - e11
