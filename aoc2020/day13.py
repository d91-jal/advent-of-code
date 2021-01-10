def get_input():
    # Read input.
    input_file = open("resources/input13.txt")
    my_input = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    timestamp = int(my_input[0])
    ids = my_input[1].split(',')
    return (timestamp, ids)


def part_1():
    my_input = get_input()
    basetime = my_input[0]
    buses = [int(a) for a in my_input[1] if a != 'x']
    # Last departure = basetime mod departure minute.
    # Next departure = departure minute - last departure.
    next_dept = [a - (basetime % a) for a in buses]
    min_index = next_dept.index(min(next_dept))
    return(buses[min_index] * next_dept[min_index])


def part_2():
    return 2


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

