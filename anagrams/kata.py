def anagramize(word):
    l = len(word)
    r = range(l)

    if l <= 1:
        return [word]
    else:
        result = []
        for i in r:
            child_list = anagramize(word[:i] + word[i+1:])
            for j in child_list:
                result.append(word[i] + j)
        return result
