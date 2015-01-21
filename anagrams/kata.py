def anagramize(word):
    if len(word) < 2:
      return [word]
    elif len(word) < 3:
      return [word, word[::-1]]
    else:
      return [word,
              word[0] + word[2] + word[1],
              word[1] + word[0] + word[2],
              word[1] + word[2] + word[0],
              word[2] + word[0] + word[1],
              word[::-1]]
