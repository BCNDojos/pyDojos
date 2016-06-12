def process():
    day = 0
    temp = 1000
    with open('weather.dat') as file:
        for line in file:
            columns = line.replace("*", "").split()
            try:
                if len(columns) > 0 and int(columns[2]) < temp:
                    day = columns[0]
                    temp = int(columns[2])
            except ValueError:
                pass
    print("{} {}".format(day, temp))