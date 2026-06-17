import unittest
import tests.test_proportion as t

class ProportionTests(unittest.TestCase):
    def test_binary_quaternary_exact_identity(self):
        t.test_binary_quaternary_exact_identity()
    def test_decimal_1000_zeros_to_quaternary_cert_cell(self):
        t.test_decimal_1000_zeros_to_quaternary_cert_cell()
    def test_decimal_small_zero_blocks(self):
        t.test_decimal_small_zero_blocks()
    def test_against_bruteforce_small_grids(self):
        t.test_against_bruteforce_small_grids()
    def test_medium_decimal_resonance(self):
        t.test_medium_decimal_resonance()
    def test_logarithmic_resonance_pairs_contains_mediumish_pair(self):
        t.test_logarithmic_resonance_pairs_contains_mediumish_pair()

if __name__ == "__main__":
    unittest.main()
