import join

def measure_join():
    s = join.join(int(1e6))
    print("{}".format(len(s)))

if __name__ == "__main__":
    measure_join()
