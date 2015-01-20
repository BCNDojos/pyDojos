def anagramize(word):
    if len(word) < 2:
      return [word]
    else:
      return [word, word[::-1]]
