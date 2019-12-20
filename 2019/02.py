from IntCode import IntCode


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


def part1(prog):
    intcode = IntCode()
    intcode.program = prog[:]
    intcode.run_program()
    return intcode.program


def part2(prog, expected):
    return gravity_assist(prog, expected)


testprog1 = [1, 0, 0, 0, 99]
testprog2 = [2, 3, 0, 3, 99]
testprog3 = [2, 4, 4, 5, 99, 0]
testprog4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]


program = [int(a) for a in open("02input.txt").read().strip().split(",")]
program[1] = 12
program[2] = 2
print((part1(program))[0])
print(part2(program, 19690720))
