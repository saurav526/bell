"""Theoretical CHSH-based min-entropy illustration."""

import math


def randomness_bound(s):
    """Return the stated theoretical lower bound in bits per round.

    H_min >= 1 - log2(1 + sqrt(2 - S^2/4)), for 2 < S <= 2 sqrt(2).
    Outside the violating interval this lab reports zero, not a certificate.
    """
    s = float(s)
    if not math.isfinite(s) or s <= 2.0:
        return 0.0

    s = min(s, 2.0 * math.sqrt(2.0))
    radicand = max(0.0, 2.0 - s * s / 4.0)
    value = 1.0 - math.log2(1.0 + math.sqrt(radicand))
    return max(0.0, min(1.0, value))
