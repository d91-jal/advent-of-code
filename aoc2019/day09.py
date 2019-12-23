from aoc2019.intcode import IntCode

test_prog_1 = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]


def part_1():
    intcode = IntCode(test_prog_1, [], 2000)
    intcode.running = True

    while intcode.running:
        intcode.run_program()

    print(intcode.output_buffer)
    return


def part_2():
    return


def main():
    print("Day 9 part 1 answer: ", part_1())
    print("Day 9 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()
