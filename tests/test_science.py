"""Independent finite checks of analytic identities, not a proof by sampling."""

import itertools
import math
import unittest

import numpy as np

from causal_threshold.core import (
    C_INFINITY, PRODUCT_CONSTANT, binary_entropy, binomial_prior,
    box_pointer_matrix, coarse_entropy_bounds, entropy, exact_readout_coefficients, fejer_constant,
    product_entropy_bounds, robust_coefficients, variance_upper,
    window_entropy, window_gram,
)


class WindowEntropyTests(unittest.TestCase):
    def test_pointer_state_and_gram_have_same_nonzero_spectrum(self):
        rng = np.random.default_rng(1847)
        for d, g in [(1, 1), (4, 1), (5, 3), (6, 12)]:
            p = rng.dirichlet(np.ones(d))
            pointers = box_pointer_matrix(d, g)
            tau = (pointers * p) @ pointers.T
            actual = np.linalg.eigvalsh(tau)
            wanted = np.linalg.eigvalsh(window_gram(p, g))
            np.testing.assert_allclose(actual[-d:], wanted, atol=2e-14)
            self.assertLess(np.linalg.norm(actual[:-d]), 2e-14)

    def test_sharp_threshold_and_spaced_code_are_exact(self):
        p = np.array([0.08, 0.27, 0.0, 0.65])
        self.assertAlmostEqual(window_entropy(p, 1), entropy(p), places=13)
        for g in [1, 2, 7]:
            p = np.zeros(3 * g + 1)
            p[::g] = 0.25
            self.assertAlmostEqual(window_entropy(p, g), 2.0, places=13)

    def test_bin_boundary_discontinuity_has_small_physical_cost(self):
        for g in [2, 8, 31]:
            p = np.zeros(g + 1)
            p[g - 1:g + 1] = 0.5
            self.assertAlmostEqual(window_entropy(p, g), binary_entropy(1 / (2 * g)), places=12)

    def test_general_prior_bounds_and_convolution_inequality(self):
        rng = np.random.default_rng(9001)
        for d, g in [(2, 1), (7, 2), (11, 4), (15, 9), (3, 17)]:
            for concentration in [0.1, 1.0, 4.0]:
                p = rng.dirichlet(np.full(d, concentration))
                value = window_entropy(p, g)
                lower, upper = coarse_entropy_bounds(p, g)
                convolved = np.convolve(p, np.ones(g) / g)
                self.assertGreaterEqual(value + 2e-12, lower)
                self.assertLessEqual(value, upper + 2e-12)
                self.assertLessEqual(value, entropy(convolved) - math.log2(g) + fejer_constant(g) + 2e-12)
                self.assertLessEqual(value, variance_upper(p, g) + 2e-12)

    def test_binomial_examples_against_analytic_bounds(self):
        for m, g in [(0, 1), (1, 1), (8, 1), (8, 3), (8, 32),
                     (64, 2), (64, 8), (64, 32), (256, 4), (256, 16), (256, 128)]:
            value = window_entropy(binomial_prior(m), g)
            lower, upper = product_entropy_bounds(m, g)
            self.assertGreaterEqual(value + 2e-12, lower)
            self.assertLessEqual(value, upper + 2e-12)

    def test_common_core_bound(self):
        rng = np.random.default_rng(336)
        for span, g in [(0, 7), (1, 8), (4, 16), (8, 8)]:
            p = rng.dirichlet(np.ones(span + 1))
            upper = binary_entropy(span / g) + (1 + C_INFINITY) * span / g
            self.assertLessEqual(window_entropy(p, g), upper + 2e-12)

    def test_fejer_integral_matches_harmonic_number_constant(self):
        # Midpoint quadrature independently evaluates the analytic integral.
        theta = 2 * np.pi * (np.arange(131072) + 0.5) / 131072
        for g in [1, 2, 3, 8, 19]:
            kernel = (np.sin(g * theta / 2) / np.sin(theta / 2)) ** 2 / g
            integral = float(np.mean(kernel * np.log2(kernel)))
            self.assertAlmostEqual(integral, math.log2(g) - fejer_constant(g), delta=2e-9)
        self.assertAlmostEqual(C_INFINITY, 1.21989772722419, places=11)
        self.assertAlmostEqual(PRODUCT_CONSTANT, 2.26699331240483, places=11)

    def test_error_coefficients_and_exact_readout_refinement(self):
        result = robust_coefficients(0.01, 0.01)
        self.assertAlmostEqual(result["zeta"], 0.0396, places=14)
        self.assertAlmostEqual(result["gamma"], 0.741949363, places=8)
        exact = exact_readout_coefficients(0.01)
        self.assertAlmostEqual(exact["coefficient"], 0.98, places=14)
        self.assertAlmostEqual(exact["b_epsilon"], 0.095147709894075, places=12)
        self.assertEqual(robust_coefficients(0, 0)["gamma"], 1)
        self.assertEqual(robust_coefficients(0.49, 0.49)["zeta"], 0.5)


class DistributedInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n, cls.g, cls.dimension = 3, 2, 8
        d = cls.dimension
        cls.charges = np.array([i.bit_count() for i in range(2**cls.n)])
        cls.w = np.zeros(d)
        cls.w[:cls.g] = 1 / math.sqrt(cls.g)
        # numpy.ifft has the positive sign required by the apparatus.
        cls.alpha = np.fft.ifft(cls.w) * math.sqrt(d)
        cls.records = list(itertools.product(range(d), repeat=cls.n))
        k = np.arange(d)
        cls.amplitudes = np.array([
            d ** (-cls.n / 2) * np.sum(
                cls.alpha[:, None] * np.exp(2j * np.pi * k[:, None]
                * (cls.charges[None, :] - sum(record)) / d), axis=0
            ) for record in cls.records
        ])

    def test_every_record_kraus_and_binary_calibration(self):
        d = self.dimension
        for record, amplitude in zip(self.records, self.amplitudes):
            s = sum(record) % d
            expected = d ** (-(self.n - 1) / 2) * self.w[(s - self.charges) % d]
            np.testing.assert_allclose(amplitude, expected, atol=7e-15)
        a = 1
        for q in range(self.n + 1):
            p_high = sum(self.w[(s - q) % d] ** 2 for s in range(a + self.g, d))
            self.assertAlmostEqual(p_high, np.clip((q - a) / self.g, 0, 1), places=13)

    def test_channel_on_every_matrix_unit_and_all_proper_transcripts(self):
        actual_kernel = self.amplitudes.T @ self.amplitudes.conj()
        expected_kernel = np.maximum(1 - np.abs(self.charges[:, None] - self.charges[None, :]) / self.g, 0)
        np.testing.assert_allclose(actual_kernel, expected_kernel, atol=2e-13)
        # Equality of this Schur kernel checks the channel, including references.
        for length in [1, 2]:
            for subset in itertools.combinations(range(self.n), length):
                for fixed in itertools.product(range(self.dimension), repeat=length):
                    indices = [i for i, r in enumerate(self.records)
                               if all(r[j] == value for j, value in zip(subset, fixed))]
                    conditional = self.amplitudes[indices]
                    kernel = conditional.T @ conditional.conj()
                    np.testing.assert_allclose(kernel, expected_kernel / self.dimension**length, atol=2e-13)

    def test_random_product_unitary_channel_and_no_signalling(self):
        k = np.arange(self.dimension)
        phases = np.exp(2j * np.pi * k[:, None] * self.charges[None, :] / self.dimension)
        phase_kernel = (phases.T * abs(self.alpha) ** 2) @ phases.conj()
        window_kernel = self.amplitudes.T @ self.amplitudes.conj()
        np.testing.assert_allclose(phase_kernel, window_kernel, atol=2e-13)
        # Trace the final two spins on every input matrix unit. Only equal B
        # indices survive; their A-channel coefficients must be B-independent.
        for x, y, b in itertools.product(range(2), range(2), range(4)):
            self.assertAlmostEqual(window_kernel[4*x+b, 4*y+b].real,
                                   window_kernel[4*x, 4*y].real, places=12)


if __name__ == "__main__":
    unittest.main()
