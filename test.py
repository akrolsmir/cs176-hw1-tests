import unittest
from pa1 import *

actg_1k = open("actg_1k.txt", "r").read().strip()
actg_5k = open("actg_5k.txt", "r").read().strip()
actg_10k = open("actg_10k.txt", "r").read().strip()
actg_20k = open("actg_20k.txt", "r").read().strip()
az09_40k = open("az09_40k.txt", "r").read().strip()

class MyTest(unittest.TestCase):
    def test_multiple_pattern_match(self):
        self.assertEqual(multiple_pattern_match(["AATCGGGTTCAATCGGGGT", "ATCG", "GGGT"]), [1, 4, 11, 15])
        self.assertEqual(multiple_pattern_match([actg_10k, "GATTACA", "TATCTT"]), [2821, 6539, 7564])
        self.assertEqual(multiple_pattern_match([actg_1k, "QQQ"]), [])
        self.assertEqual(multiple_pattern_match(['BARBARA', 'HI']), [])
        self.assertEqual(multiple_pattern_match(['BARBARA', 'AR', 'BAR']), [0, 1, 3, 4])
        self.assertEqual(multiple_pattern_match(['BARBARAB', 'B']), [0, 3, 7])

    def test_longest_repeat(self):
        self.assertEqual(longest_repeat("ATATCGTTTTATCGTT"), 'TATCGTT')
        self.assertEqual(longest_repeat(actg_1k), 'CTGATTTG')
        # self.assertEqual(longest_repeat(az09_40k), '3YP30R')

    def test_longest_common_substring(self):
        self.assertEqual(longest_common_substring("TCGGTAGATTGCGCCCACTC", "AGGGGCTCGCAGTGTAAGAA"), 'AGA')
        self.assertEqual(longest_common_substring(actg_1k, actg_5k), 'ACGCGAAGGC')

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring(actg_1k), 'GATATCTCTATAG')
        self.assertEqual(longest_palindromic_substring("GCGTTCAACTCGG"), 'TCAACT')

    def test_shortest_non_shared_substring(self):
        self.assertEqual(shortest_non_shared_substring("CCAAGCTGCTAGAGG", "CATGCTGGGCTGGCT"), 'AA')
        self.assertEqual(shortest_non_shared_substring(actg_1k, actg_5k), 'ATAGT')

    def test_longest_k_repeat_substring(self):
        self.assertEqual(longest_k_repeat_substring(3, "AAACCACACACAAA"), 'CACA')
        self.assertEqual(longest_k_repeat_substring(5, actg_1k), 'ATTTG')

    def test_shortest_non_substring(self):
        self.assertEqual(shortest_non_substring("GCGTTCAACTCGG"), 'AG')
        self.assertEqual(shortest_non_substring(actg_1k), 'TCCG')
        # self.assertEqual(shortest_non_substring(az09_40k), '002')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGG"), 'AT')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGAT"), 'CC')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGATCC"), 'TA')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGATCCTA"), 'TG')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGATCCTATG"), 'AAA')
        self.assertEqual(shortest_non_substring("A"), 'AA')
        self.assertEqual(shortest_non_substring("AB"), 'AA')
        self.assertEqual(shortest_non_substring("AABA"), 'BB')

unittest.main(verbosity=1)
