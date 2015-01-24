from math import factorial
from random import shuffle

def anagramize(word):
    anagrams = []    
    if len(word)<=1:
        anagrams = [word]
    else:
        for i,char in enumerate(word):
            for perm in anagramize(word[:i]+word[i+1:]):
                anagrams += [char + perm]
    return anagrams

