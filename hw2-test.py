import unittest
from pa2 import *

actg_1k = open("actg_1k.txt", "r").read().strip()
actg_5k = open("actg_5k.txt", "r").read().strip()
actg_10k = open("actg_10k.txt", "r").read().strip()
actg_20k = open("actg_20k.txt", "r").read().strip()
az09_40k = open("az09_40k.txt", "r").read().strip()

class MyTest(unittest.TestCase):
    def test_bwt(self):
        self.assertEqual(bwt("banana$"), "annb$aa")

    def test_ibwt(self):
        self.assertEqual(ibwt("annb$aa"), "banana$")

    def test_exact_match(self):
        self.assertEqual(exact_match("banana", "ana"), ([1, 3], [(1, 3), (5, 6), (2, 3)]))
        self.assertEqual(exact_match("shesellsseashellsbytheseashore", "sea"), ([8, 22], [(1, 2), (5, 6), (22, 23)]))

    def test_bowtie(self):
        self.assertEqual(bowtie('GATTACA', 'AGA', [40, 15, 35], 2, 2), 4)

unittest.main(verbosity=1)
