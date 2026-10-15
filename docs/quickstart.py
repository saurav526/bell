"""Minimal example: run a CHSH experiment with 90% visibility."""

from bell.runner import run_chsh

result = run_chsh(shots=8192, visibility=0.9, seed=42)
print(f"S = {result.s_value:.3f} +/- {result.std_error:.3f}")
print(f"Entropy bound = {result.entropy_bound:.3f} bits/round")
