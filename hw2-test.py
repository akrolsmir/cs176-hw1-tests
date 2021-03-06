import unittest, random
from pa2 import *

actg_1k = open("actg_1k.txt", "r").read().strip()
actg_1k_bwt = "GGGAACTAGACGTCTATACGTATGGAAACCTAGCCATACTAAGGGAATCTGCCCCGAACTCTAGTGGCGGGTCCTTCAGACCACTCGTGGAGCCGTCTCAACACGCGGATTGCAAAGGCTCATCAATTGATCCATTTGTGCGCAGAAGAATACGGTGTTTTGGATGGTGGCAGTCTTCAGGTCGCAGCGTTTTACAGCTCATGAAGACAGCAAGC$CTCGATACGATTTACCTTCAACGACACGGATATTGGAGGGCAACATAACGCCACCGGATGGCAGGCAGTTAGAGCGGTTAGGGGGGCTCCAATTTTTATGTGGTAGCGATGTCGGACTTGCGCGCGCCAGAGGTAACTTAATCTCCCAGTATTTTGCTAGAAGAAGTCGTAGGAGTTTGTAAGATACGGAATGATTTCGGTCACGAGACAATTCTCTCTGGATCCGAATCACGCTTGACCATACACAGCCATATGTGCACAAGTATCCCTAAAGCTAAAGGGAGTAGTTGCCGCGAAAGCAGCTCAGGAGCTCGCAATGTTATGATATGGCGTAGGGATGCGGGCAACGGAGTCTGTGTCCTCGGTCTAGAAGTGGGAGACTTGCGCGTGGAGAAGTTCTAGGCTCGTAGATCGCCTCAGAATCGTTGGACATTCTTGTCGTATACTCGTATCGAGCTTAAGCACTTTGCCTCCAGGAACGCCATTTCCTTCCCGGGGGTAGCCGTTCAGTAGAGTTTACCCGAGTTATCAAGCTGTGCAACCGCAGAGTATTTTCACTAGATTGCGACCAAATACACAATGAAATCTGAGTATTGACTCCGGCATCATAAAAGGTTCCCGTGACCTAAGAACGAGTATTGAGATCCGCCCGTTTTGTTAGTTTAAGCTGACGAACATTCTCCCATATTGTTGTAGTTGTACAGTGTATTGACACTGTCGCGTGCTCTGGTCCTTGTTGAATATCTGTGCGTAGTCTGTTTGGATGACAACATTGAGTATATTCA"
actg_5k = open("actg_5k.txt", "r").read().strip()
actg_10k = open("actg_10k.txt", "r").read().strip()
actg_20k = open("actg_20k.txt", "r").read().strip()
az09_40k = open("az09_40k.txt", "r").read().strip()

class MyTest(unittest.TestCase):
    def test_bwt(self):
        self.assertEqual(bwt("banana$"), "annb$aa")
        self.assertEqual(bwt(actg_1k + "$"), actg_1k_bwt)

    def test_ibwt(self):
        self.assertEqual(ibwt("annb$aa"), "banana$")
        self.assertEqual(ibwt("arbbr$aa"), "barbara$")
        self.assertEqual(ibwt(actg_1k_bwt), actg_1k + "$")

    def test_ibwt_of_bwt(self):
        for text in ["banana", actg_1k, actg_5k, actg_10k, actg_20k]:
            text += "$"
            self.assertEqual(text, ibwt(bwt(text)))
        for size in range(500):
            s = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(size)) + "$"
            self.assertEqual(s, ibwt(bwt(s)))

    def test_exact_match(self):
        self.assertEqual(exact_match("banana", "ana"), ([1, 3], [(1, 3), (5, 6), (2, 3)]))
        self.assertEqual(exact_match("shesellsseashellsbytheseashore", "sea"), ([8, 22], [(1, 2), (5, 6), (22, 23)]))
        self.assertEqual(exact_match(actg_1k, "ACTG"), ([381, 739, 872], [(474, 735), (851, 916), (447, 458), (116, 118)]))

    def test_bowtie(self):
        self.assertEqual(bowtie('GATTACA', 'AGA', [40, 15, 35], 2, 2), 4)
        self.assertEqual(bowtie(actg_1k, "ACTG", [0, 0, 0, 0], 1, 1), 381)
        self.assertEqual(bowtie('CAGTACCA', 'AGGA', [40, 15, 15, 35], 2, 2), 4)
        self.assertEqual(bowtie('GATTACCA', 'AGGA', [40, 15, 15, 35], 2, 2), False)

unittest.main(verbosity=1)
