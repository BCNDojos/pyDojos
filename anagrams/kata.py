from math import factorial
from random import shuffle

def anagramize(word):
    anagrams = [word]
    if len(word) > 1:
        anagrams = [i for i in get_anagram(word)]
    return anagrams

def get_anagram(word):
    if len(word) ==1:
        yield word
    else:
        for perm in anagramize(word[1:]):
            for i in range(len(word)):
                yield perm[:i] + word[0:1] + perm[i:]
