testprog1 = [1, 0, 0, 0, 99]
testprog2 = [2, 3, 0, 3, 99]
testprog3 = [2, 4, 4, 5, 99, 0]
testprog4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]


def run_program(program):
    result = program[:]

    for p in range(0, len(result) - 1, 4):
        if (p + 1 > len(result)) or (result[p] == 99):
            break
        elif result[p] == 1:
            result[result[p + 3]] = result[result[p + 1]] + result[result[p + 2]]
        elif result[p] == 2:
            result[result[p + 3]] = result[result[p + 1]] * result[result[p + 2]]

    return result


def gravity_assist(program, expected_result):
    for noun in range(0, 99):
        for verb in range(0, 99):
            testprog = program[:]
            testprog[1], testprog[2] = noun, verb
            result = run_program(testprog)

            if result[0] == expected_result:
                return (noun * 100) + verb

    return -1, -1


def __main__():
    program = [int(a) for a in open("02input.txt").read().strip().split(",")]
    program[1] = 12
    program[2] = 2
    print(run_program(program))
    print(gravity_assist(program, 19690720))

__main__()
# print(run_program(testprog1))
# print(run_program(testprog2))
# print(run_program(testprog3))
# print(run_program(testprog4))


