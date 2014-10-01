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

        self.assertEqual(multiple_pattern_match(["TTTAAACCCGGG", "A", "C", "G", "T"]), [i for i in range(len("TTTAAACCCGGG"))])
        self.assertEqual(multiple_pattern_match(["AJSKDKJASD", ""]), range(len("AJSKDKJASD")))
        self.assertEqual(multiple_pattern_match(["ABABABABA", "AB"]), [0, 2, 4, 6])
        self.assertEqual(multiple_pattern_match(["ABABABABACC", "ABA", "CC"]), [0, 2, 4, 6, 9])
        self.assertEqual(multiple_pattern_match(["AAAAAAAAAA", "AAA"]), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(multiple_pattern_match(["", "A"]), [])
        self.assertEqual(multiple_pattern_match(["AAAABBBBBCCCCDDDDD", "F", "G", "L", "AAAAA", "BBBBBB"]), [])

    def test_longest_repeat(self):
        self.assertEqual(longest_repeat("ATATCGTTTTATCGTT"), 'TATCGTT')
        self.assertEqual(longest_repeat(actg_1k), 'CTGATTTG')
        self.assertEqual(longest_repeat(actg_5k), 'AGTCTGTCTCGTCA')
        self.assertEqual(longest_repeat(az09_40k), '3YP30R')
        self.assertEqual(longest_repeat("AAAAAAAAAAAAAAAA"), 'AAAAAAAAAAAAAAA')
        self.assertEqual(longest_repeat("AAAABCDFABCDFA"), 'ABCDFA')
        self.assertEqual(longest_repeat(""), '')

    def test_longest_common_substring(self):
        self.assertEqual(longest_common_substring("TCGGTAGATTGCGCCCACTC", "AGGGGCTCGCAGTGTAAGAA"), 'AGA')
        self.assertEqual(longest_common_substring(actg_1k, actg_5k), 'ACGCGAAGGC')
        self.assertEqual(longest_common_substring(actg_5k, actg_10k), 'CTGACATGTGAAGC')
        self.assertEqual(longest_common_substring("TCGGTAGATTGCGCCCACTC", "AGGGGCTCGCAGTGTAAGAA"), 'AGA')
        self.assertEqual(longest_common_substring("BBBBCCCCCCAAA", "BCCCCCCA"), 'BCCCCCCA')
        self.assertEqual(longest_common_substring("", "ATCCCCGGGGA"), "")
        self.assertEqual(longest_common_substring("ATCCCCGGGGA", ""), "")

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("A"), 'A')
        self.assertEqual(longest_palindromic_substring("AGA"), 'AGA')
        self.assertEqual(longest_palindromic_substring("GCGTTCAACTCGG"), 'TCAACT')
        self.assertEqual(longest_palindromic_substring("GCGTTCAACTCGG"), "TCAACT")
        self.assertEqual(longest_palindromic_substring("1234XABA4321"), "ABA")
        self.assertEqual(longest_palindromic_substring("1234ABA4321"), "1234ABA4321")
        self.assertEqual(longest_palindromic_substring("ABCDEFGHIHGFEDCBA"), "ABCDEFGHIHGFEDCBA")
        self.assertEqual(longest_palindromic_substring(actg_1k), 'GATATCTCTATAG')
        self.assertEqual(longest_palindromic_substring(actg_5k), 'ATGTCGGCTGTA')

    def test_shortest_non_shared_substring(self):
        self.assertEqual(shortest_non_shared_substring("CCAAGCTGCTAGAGG", "CATGCTGGGCTGGCT"), 'AA')
        self.assertEqual(shortest_non_shared_substring("AABAC", "ACBAA"), 'AB')
        self.assertEqual(shortest_non_shared_substring(actg_1k, actg_5k), 'ATAGT')
        self.assertEqual(shortest_non_shared_substring("CCAAGCTGCTAGAGG", "CATGCTGGGCTGGCT"), "AA")
        self.assertEqual(shortest_non_shared_substring("APPLE", "PLEA"), "AP")
        self.assertEqual(shortest_non_shared_substring("", "AP"), "")
        self.assertEqual(shortest_non_shared_substring("ABCDEFGHIJKLMNOPQRSTUVWXZ", "ZYXWABCDEFGHIJKLMNOPQRSTUV"), "VW")

    def test_longest_k_repeat_substring(self):
        self.assertEqual(longest_k_repeat_substring(3, "AAACCACACACAAA"), 'CACA')
        self.assertEqual(longest_k_repeat_substring(3, "AAACCACACACAAA"), "CACA")
        self.assertEqual(longest_k_repeat_substring(4, "ABCADJAKKKABCABCABCAAA"), "ABCA")
        self.assertEqual(longest_k_repeat_substring(4, "BADFHZACERTAPOLKANMMM"), "A")
        self.assertEqual(longest_k_repeat_substring(4, "ABC"), "")
        self.assertEqual(longest_k_repeat_substring(5, actg_1k), 'ATTTG')
        self.assertEqual(longest_k_repeat_substring(10, actg_5k), 'AAACT')
        self.assertEqual(longest_k_repeat_substring(1, "HELLO1WORLD"), 'HELLO1WORLD')

    def test_shortest_non_substring(self):
        self.assertEqual(shortest_non_substring("GCGTTCAACTCGG"), 'AG')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGG"), 'AT')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGAT"), 'CC')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGATCC"), 'TA')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGATCCTA"), 'TG')
        self.assertEqual(shortest_non_substring("GCGTTCAACTCAGGATCCTATG"), 'AAA')
        self.assertEqual(shortest_non_substring("A"), 'AA')
        self.assertEqual(shortest_non_substring("AB"), 'AA')
        self.assertEqual(shortest_non_substring("AABA"), 'BB')
        self.assertEqual(shortest_non_substring(""), "")
        self.assertEqual(shortest_non_substring("A"), "AA")
        self.assertEqual(shortest_non_substring("AA"), "AAA")
        self.assertEqual(shortest_non_substring("AG"), "AA")
        self.assertEqual(shortest_non_substring("GCGTTCAAACAGATCCTCGG"), "TA")
        self.assertEqual(shortest_non_substring("GCGTTCAACTCGG"), "AG")
        self.assertEqual(shortest_non_substring("ABCDEFGHIJKLMNOPQRSTUVWXZ"), "AA")
        self.assertEqual(shortest_non_substring("AABBCDEFGHIJKLMNOPQRSTUVWXZ"), "AC")
        self.assertEqual(shortest_non_substring(actg_1k), 'AGTG')
        self.assertEqual(shortest_non_substring(actg_5k), 'AGTGC')
        self.assertEqual(shortest_non_substring(az09_40k), '002')

#     def test_longest_repeat_time(self, trials=5):
#         import timeit
#         for n in [1000, 2000, 4000, 8000]:#, 100000, 1000000]:
#             t = timeit.Timer("""longest_repeat(s)""", setup="""
# import random
# from pa1 import longest_repeat
# s = ''.join(random.choice('{alphabet}') for i in range({size}))
#             """.format(size=n, alphabet='ACTG'))
#             total_time = t.timeit(trials)
#             print "Size: " + str(n) + ". Average time = " + str(total_time / trials)

unittest.main(verbosity=1)
