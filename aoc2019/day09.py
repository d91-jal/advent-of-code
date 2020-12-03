from aoc2019.intcode import IntCode

test_prog_1 = [
    109, 1,                 # Increase relative base by 1
    204, -1,                # Output &(relative base - 1)
    1001, 100, 1, 100,      # Add 1 to &100 into &100
    1008, 100, 16, 101,     # &101 = 1 if &100 equals 16 else 0
    1006, 101, 0,           # If &101 equals 0 then jump to 0
    99]

test_prog_2 = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
test_prog_3 = [104, 1125899906842624, 99]


def part_1():
    input_file = open("resources/09input.txt")
    my_prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    intcode = IntCode(my_prog, [1], 2000)
    intcode.running = True

    while intcode.running:
        intcode.run_program()

    # print(intcode.output_buffer)
    return intcode.output_buffer[0]


def part_2():
    input_file = open("resources/09input.txt")
    my_prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    intcode = IntCode(my_prog, [2], 2000)
    intcode.running = True

    while intcode.running:
        intcode.run_program()

    # print(intcode.output_buffer)
    return intcode.output_buffer[0]


def main():
    print("Day 9 part 1 answer: ", part_1())
    print("Day 9 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()
