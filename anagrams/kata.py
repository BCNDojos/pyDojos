from math import factorial
from random import shuffle

def anagramize(word):
    anagrams = [word]
    while len(anagrams) < factorial(len(word)):
        letters = list(word)
        shuffle(letters)
        anagram = ''.join(letters)
        if not anagram in anagrams:
            anagrams.append(anagram)
    return anagrams

