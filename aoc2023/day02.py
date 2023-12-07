def part_1(my_input):
    return


def part_2(my_input):
    return


def main():
    # Read input into an array.
    input_file = open("resources/input02.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()