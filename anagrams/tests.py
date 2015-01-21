#!/usr/bin/env python

import string
import unittest
from math import factorial
from random import randint, sample
from kata import *

class TestAnagrams(unittest.TestCase):
     def test_basic_anagrams(self):
         '''tests basic anagrams'''
         self.assertEqual([''], anagramize(''))
         self.assertEqual(['a'], anagramize('a'))
         self.assertEqual(['ab', 'ba'], anagramize('ab'))

     def test_variable_length_anagram(self):
         alphabet = string.ascii_lowercase
         length = randint(4, 10)
         word = ''.join(sample(alphabet, length))
         anagrams_length = factorial(length)
         anagrams = anagramize(word)
         self.assertEqual(anagrams_length, len(set(anagrams)))
         for anagram in anagrams:
             self.assertEqual(length, len(anagram))
             for char in set(word):
                 self.assertTrue(char in anagram)

if __name__ == '__main__':
    unittest.main()
