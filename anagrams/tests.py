#!/usr/bin/env python

import unittest
from kata import anagramize
from math import factorial


class TestAnagrams(unittest.TestCase):

    def test_sin_letras(self):
        self.generico('')

    def test_una_letra(self):
        self.generico('a')

    def test_dos_letras(self):
        self.generico('ab')

    def test_tres_letras(self):
        self.generico('abc')

    def test_mas_letras(self):
        word = "abcdefghi"
        self.generico(word)

    def generico(self, word):
        resultado = anagramize(word)
        self.assertEqual(factorial(len(word)), len(set(resultado)))
        for palabra in resultado:
            self.assertEqual(len(word), len(set(palabra)))
            for char in palabra:
                self.assertIn(char, word)

if __name__ == '__main__':
    unittest.main()
