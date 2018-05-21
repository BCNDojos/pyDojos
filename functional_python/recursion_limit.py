from sys import getrecursionlimit, setrecursionlimit


def recursion_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursion_sum(n-1)


print(recursion_sum(1000))
print(getrecursionlimit())
setrecursionlimit(1002)
print(recursion_sum(1000))
