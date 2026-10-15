"""CHSH estimators, shot-noise errors, and visibility mixing."""

import math


def correlation(counts):
    """Estimate E = P(equal outcomes) - P(different outcomes)."""
    total = sum(counts.values())
    if total <= 0:
        raise ValueError("Counts must have a positive total.")

    equal = 0
    different = 0
    for key, count in counts.items():
        bits = key.replace(" ", "")
        if len(bits) < 2:
            raise ValueError(f"Expected a two-bit outcome, got {key!r}.")
        if bits[-1] == bits[-2]:
            equal += count
        else:
            different += count

    return (equal - different) / total


def chsh_from_correlations(es):
    """CHSH convention: E00 + E01 + E10 - E11."""
    if len(es) != 4:
        raise ValueError("Exactly four correlations are required.")
    return float(es[0] + es[1] + es[2] - es[3])


def model_correlations(raw_es, visibility):
    """Mix each distribution with uniform white noise.

    Uniform two-bit noise has zero correlation, so E_model = v * E_raw.
    This is classical post-processing, not a simulated physical channel.
    """
    if not 0.0 <= visibility <= 1.0:
        raise ValueError("Visibility must be in [0, 1].")
    return [float(visibility * e) for e in raw_es]


def standard_error(es, shots):
    """Independent-binomial propagation for four sample correlations."""
    if shots <= 0:
        raise ValueError("Shots must be positive.")
    variance = sum(max(0.0, 1.0 - float(e) ** 2) for e in es) / shots
    return math.sqrt(variance)
