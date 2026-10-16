"""Analytic formulas and small finite matrices; every entropy is in bits.

The routines evaluate the explicit window apparatus. They do not numerically
minimize over causal instruments. Universal optimality bounds are analytic.
"""

from __future__ import annotations

import math
import operator
from collections.abc import Sequence

import numpy as np
from scipy.special import digamma, gammaln, xlogy

C_INFINITY = 2 * (1 - float(np.euler_gamma)) / math.log(2)
PRODUCT_CONSTANT = 0.5 * math.log2(math.pi * math.e / 2) + C_INFINITY


def positive_integer(value: int, name: str = "value") -> int:
    """Require an integer at least one (do not silently truncate floats)."""
    if isinstance(value, (bool, np.bool_)):
        raise ValueError(f"{name} must be a positive integer")
    try:
        result = operator.index(value)
    except TypeError as exc:
        raise ValueError(f"{name} must be a positive integer") from exc
    if result < 1:
        raise ValueError(f"{name} must be a positive integer")
    return result


def probabilities(p: Sequence[float]) -> np.ndarray:
    result = np.asarray(p, dtype=float)
    if result.ndim != 1 or result.size == 0:
        raise ValueError("a nonempty one-dimensional prior is required")
    if not np.all(np.isfinite(result)) or np.any(result < 0):
        raise ValueError("probabilities must be finite and nonnegative")
    total = float(result.sum())
    if not math.isclose(total, 1, rel_tol=1e-10, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return result / total


def entropy(p: Sequence[float]) -> float:
    """Shannon entropy, or von Neumann entropy given nonnegative eigenvalues."""
    p = probabilities(p)
    return float(-np.sum(xlogy(p, p)) / math.log(2))


def binary_entropy(x: float) -> float:
    if not math.isfinite(x) or not 0 <= x <= 1:
        raise ValueError("binary probability must lie in [0, 1]")
    return entropy([x, 1 - x])


def binomial_prior(m: int) -> np.ndarray:
    if isinstance(m, (bool, np.bool_)):
        raise ValueError("m must be a nonnegative integer")
    try:
        m = operator.index(m)
    except TypeError as exc:
        raise ValueError("m must be a nonnegative integer") from exc
    if m < 0:
        raise ValueError("m must be a nonnegative integer")
    q = np.arange(m + 1)
    logp = gammaln(m + 1) - gammaln(q + 1) - gammaln(m - q + 1) - m * math.log(2)
    p = np.exp(logp - np.max(logp))
    return p / p.sum()


def fejer_constant(g: int) -> float:
    g = positive_integer(g, "g")
    if g == 1:
        return 0.0
    harmonic = float(digamma(g + 1) + np.euler_gamma)
    return 2 * (1 + math.log(g) - harmonic) / math.log(2)


def box_pointer_matrix(number_of_charges: int, g: int) -> np.ndarray:
    """Column q is |e_q> on positions 0,...,number_of_charges+g-2."""
    number_of_charges = positive_integer(number_of_charges, "number_of_charges")
    g = positive_integer(g, "g")
    positions = np.arange(number_of_charges + g - 1)[:, None]
    charges = np.arange(number_of_charges)[None, :]
    return ((positions >= charges) & (positions < charges + g)) / math.sqrt(g)


def window_gram(p: Sequence[float], g: int) -> np.ndarray:
    """Weighted Gram matrix, isospectral to the nonzero output spectrum."""
    p = probabilities(p)
    g = positive_integer(g, "g")
    q = np.arange(len(p))
    overlaps = np.maximum(1 - np.abs(q[:, None] - q[None, :]) / g, 0)
    return np.sqrt(p[:, None] * p[None, :]) * overlaps


def window_entropy(p: Sequence[float], g: int) -> float:
    eigenvalues = np.linalg.eigvalsh(window_gram(p, g))
    if float(eigenvalues.min()) < -1e-10:
        raise ArithmeticError("window Gram matrix lost positivity")
    eigenvalues = np.maximum(eigenvalues, 0)
    return entropy(eigenvalues / eigenvalues.sum())


def coarse_probabilities(p: Sequence[float], g: int) -> np.ndarray:
    p = probabilities(p)
    g = positive_integer(g, "g")
    return np.bincount(np.arange(len(p)) // g, weights=p)


def coarse_entropy_bounds(p: Sequence[float], g: int) -> tuple[float, float]:
    """Bounds on the optimum; the upper is achieved or improved by the window."""
    g = positive_integer(g, "g")
    coarse = coarse_probabilities(p, g)
    h = entropy(coarse)
    parity = np.bincount(np.arange(len(coarse)) % 2, weights=coarse, minlength=2)
    lower = max(0.0, h - entropy(parity))
    if g == 1:
        lower = h
    return lower, h + math.log2(2 - 1 / g) + fejer_constant(g)


def variance_upper(p: Sequence[float], g: int) -> float:
    p = probabilities(p)
    g = positive_integer(g, "g")
    q = np.arange(len(p))
    mean = float(p @ q)
    variance = float(p @ ((q - mean) ** 2))
    return 0.5 * math.log2(2 * math.pi * math.e * (variance / g**2 + 1 / 12)) + fejer_constant(g)


def product_entropy_bounds(m: int, g: int) -> tuple[float, float]:
    p = binomial_prior(m)
    g = positive_integer(g, "g")
    return max(0.0, entropy(p) - math.log2(g)), variance_upper(p, g)


def robust_coefficients(eta: float, epsilon: float) -> dict[str, float]:
    """General noisy-readout coefficients, with random guessing outside the useful range."""
    if not (math.isfinite(eta) and 0 <= eta <= 0.5
            and math.isfinite(epsilon) and 0 <= epsilon < 1):
        raise ValueError("eta must lie in [0, 1/2] and epsilon in [0, 1)")
    angle = math.asin(math.sqrt(eta)) + math.asin(math.sqrt(epsilon))
    zeta = math.sin(angle) ** 2 if angle < math.pi / 4 else 0.5
    a = (1 - epsilon) * (1 - binary_entropy(zeta))
    return {"zeta": zeta, "A": a, "gamma": a - epsilon}


def exact_readout_coefficients(epsilon: float) -> dict[str, float]:
    """Stronger coefficients requiring eta=0 and exact nonsignalling."""
    if not math.isfinite(epsilon) or not 0 <= epsilon < 1:
        raise ValueError("epsilon must lie in [0, 1)")
    b = binary_entropy(epsilon) - (1 - epsilon) * math.log2(1 - epsilon)
    return {"coefficient": 1 - 2 * epsilon, "b_epsilon": b}
