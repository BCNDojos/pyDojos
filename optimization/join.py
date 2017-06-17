def join(loops):
    l = []
    for _ in range(loops):
        l.append("a")
    return "".join(l)

if __name__ == "__main__":
    s = join(int(1e6))
    print("{}".format(len(s)))
