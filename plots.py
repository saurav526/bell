"""Simple theory plot; no Qiskit visualization dependencies."""

import math

import matplotlib.pyplot as plt
import numpy as np

from bell.entropy import randomness_bound


def show_results(visibility, measured_s=None, show_noise_sweep=True):
    """Plot theoretical entropy curve and selected operating point."""
    if show_noise_sweep:
        visibilities = np.linspace(0.0, 1.0, 301)
    else:
        visibilities = np.array([visibility])

    ideal_s = 2.0 * math.sqrt(2.0) * visibilities
    entropy = np.array([randomness_bound(s) for s in ideal_s])
    threshold = 1.0 / math.sqrt(2.0)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))

    axes[0].plot(visibilities, ideal_s, label="Ideal model S = 2√2 v")
    axes[0].axhline(2.0, linestyle="--", label="Local bound S = 2")
    axes[0].axvline(
        threshold, linestyle=":", label="Model threshold v = 1/√2"
    )
    axes[0].axvline(
        visibility, linestyle="-.", label=f"Selected v = {visibility:.3f}"
    )
    if measured_s is not None:
        axes[0].scatter(
            [visibility], [measured_s],
            label="Measured/modelled point estimate", zorder=4
        )
    axes[0].set_xlabel("Visibility v")
    axes[0].set_ylabel("CHSH S")
    axes[0].set_title("Bell violation versus visibility")
    axes[0].set_ylim(0.0, 3.0)
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(fontsize=8)

    axes[1].plot(visibilities, entropy, label="Theoretical bound")
    axes[1].axvline(threshold, linestyle=":", label="Threshold v = 1/√2")
    axes[1].axvline(
        visibility, linestyle="-.", label=f"Selected v = {visibility:.3f}"
    )
    axes[1].set_xlabel("Visibility v")
    axes[1].set_ylabel("Bound (bits per round)")
    axes[1].set_title("Illustrative min-entropy bound")
    axes[1].set_ylim(-0.03, 1.05)
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(fontsize=8)

    fig.suptitle(
        "Bell Test and Randomness Lab — theory/model, not certification"
    )
    fig.tight_layout()
    plt.show()
