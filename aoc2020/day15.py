def generate(series, last, start, end):
    for i in range(start, end):
        if last in series:
            series[last] = series[last][-1], i
            new = series[last][-1] - series[last][-2]
        else: 
            series[last] = 0, i
            new = 0
        
        last = new

    return last



def part_1():
    series = {}
    init = [0, 14, 1, 3, 7]
    last = 9

    for i in range(len(init)):
        series[init[i]] = [i]

    return generate(series, last, 5, 2019)


def part_2():
    series = {}
    init = [0, 14, 1, 3, 7]
    last = 9

    for i in range(len(init)):
        series[init[i]] = [i]

    return generate(series, last, 5, 30000000 - 1)

def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
