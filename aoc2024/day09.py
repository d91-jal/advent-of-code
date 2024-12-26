def part_1(my_input):
    result = 0
    return result


def part_2(my_input):
    result = 0
    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input08.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()