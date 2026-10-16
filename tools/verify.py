#!/usr/bin/env python3
"""Reproduce finite entropy values and the explanatory scientific figure."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
import scipy

from causal_threshold.core import (
    C_INFINITY, PRODUCT_CONSTANT, binomial_prior, entropy, product_entropy_bounds,
    exact_readout_coefficients, robust_coefficients, window_entropy,
)


def make_figure(destination: Path) -> None:
    os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "build" / "matplotlib"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    destination.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "svg.fonttype": "path"})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.3), layout="constrained")
    blue, teal, orange = "#245994", "#127c73", "#c27123"
    q = np.arange(0, 17)
    a, g = 6, 4
    ax = axes[0]
    ax.step(q, np.clip((q-a)/g, 0, 1), where="mid", color=blue, linewidth=2.3)
    ax.scatter(q, np.clip((q-a)/g, 0, 1), color=blue, s=19, zorder=3)
    ax.axvspan(-0.5, a + 0.5, color=teal, alpha=0.07)
    ax.axvspan(a + g - 0.5, 16.5, color=orange, alpha=0.07)
    ax.text(2.9, 0.83, "certain low", color=teal, ha="center")
    ax.text(13.2, 0.2, "certain high", color=orange, ha="center")
    ax.set(xlim=(-0.5, 16.5), ylim=(-0.07, 1.1), xlabel="Definite total charge q",
           ylabel="Probability of high", title="A   A calibrated binary threshold")
    ax.set_yticks([0, 0.5, 1])
    ax.set_xticks([0, 6, 10, 16], ["0", "a = 6", "a + g = 10", "N = 16"])
    ax.text(0.98, 0.53, "s = q + Z\nZ uniform on {0, 1, 2, 3}",
            transform=ax.transAxes, ha="right", fontsize=9)

    ax = axes[1]
    m = 64
    gaps = np.arange(1, 129)
    p = binomial_prior(m)
    values = np.array([window_entropy(p, int(gap)) for gap in gaps])
    bounds = np.array([product_entropy_bounds(m, int(gap)) for gap in gaps])
    ax.fill_between(gaps, bounds[:, 0], bounds[:, 1], color=blue, alpha=0.10,
                    label="Analytic bounds on the optimum")
    ax.plot(gaps, bounds[:, 0], color=blue, linestyle="--", linewidth=1.2)
    ax.plot(gaps, bounds[:, 1], color=blue, linestyle="--", linewidth=1.2)
    ax.plot(gaps, values, color=teal, linewidth=2.3, label="Explicit window apparatus")
    ax.axvline(math.sqrt(m), color=orange, linestyle=":", linewidth=1.4)
    ax.text(math.sqrt(m)*1.10, 4.7, r"$g=\sqrt{m}$", color=orange, fontsize=10)
    ax.set(xscale="log", xlim=(1, 128), ylim=(0, 5.7), xlabel="Threshold gap g",
           ylabel="Entropy of retained spins (bits)",
           title="B   A pure product input, m = 64")
    ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 128], [str(x) for x in [1, 2, 4, 8, 16, 32, 64, 128]])
    ax.legend(loc="upper right", frameon=False, fontsize=8)
    for ax in axes:
        ax.grid(axis="y", color="#d4dae0", linewidth=0.6, alpha=0.7)
        ax.set_axisbelow(True)
    # Fixed metadata makes the vector output reproducible without a timestamp.
    with plt.rc_context({"svg.hashsalt": "causal-threshold-backaction"}):
        fig.savefig(destination / "threshold_entropy.svg", metadata={"Date": None})
    svg = destination / "threshold_entropy.svg"
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
    fig.savefig(destination / "threshold_entropy.png", dpi=180,
                metadata={"Software": "causal-threshold-backaction/tools/verify.py"})
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "verification")
    parser.add_argument("--figures", type=Path, help="Also regenerate SVG/PNG explanatory figures")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    rows = []
    for m, g in [(1, 1), (8, 1), (8, 3), (8, 32), (64, 2), (64, 8),
                 (64, 32), (256, 4), (256, 16), (256, 128)]:
        p = binomial_prior(m)
        lower, upper = product_entropy_bounds(m, g)
        value = window_entropy(p, g)
        if not lower - 2e-12 <= value <= upper + 2e-12:
            raise AssertionError(f"entropy bound failed for m={m}, g={g}")
        rows.append({"m": m, "g": g, "charge_entropy": entropy(p),
                     "product_lower_bound": lower, "window_entropy": value,
                     "variance_upper_bound": upper})
    with (args.output / "entropy_values.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    report = {"python": platform.python_version(), "numpy": np.__version__,
              "scipy": scipy.__version__, "entropy_unit": "bits",
              "C_infinity": C_INFINITY, "product_constant": PRODUCT_CONSTANT,
              "eta_001_epsilon_001": robust_coefficients(0.01, 0.01),
              "exact_readout_eta_0_epsilon_001": exact_readout_coefficients(0.01),
              "examples_checked": len(rows),
              "interpretation": "Evaluation of the explicit apparatus; no optimization over instruments."}
    (args.output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    if args.figures is not None:
        make_figure(args.figures)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
