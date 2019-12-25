from aoc2019.intcode import IntCode


def gravity_assist(program, expected_result):
    intcode = IntCode()

    for noun in range(0, 99):
        for verb in range(0, 99):
            testprog = program[:]
            testprog[1], testprog[2] = noun, verb
            intcode.program = testprog
            intcode.run_program()
            result = intcode.program

            if result[0] == expected_result:
                return (noun * 100) + verb

    return -1, -1


def part_1():
    input_file = open("resources/02input.txt")
    prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    prog[1] = 12
    prog[2] = 2
    intcode = IntCode()
    intcode.program = prog[:]
    intcode.run_program()
    return intcode.program[0]


def part_2():
    input_file = open("resources/02input.txt")
    prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    prog[1] = 12
    prog[2] = 2
    return gravity_assist(prog, 19690720)


def main():
    print("Day 2 part 1 answer: ", part_1())
    print("Day 2 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()

# testprog1 = [1, 0, 0, 0, 99]
# testprog2 = [2, 3, 0, 3, 99]
# testprog3 = [2, 4, 4, 5, 99, 0]
# testprog4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]

