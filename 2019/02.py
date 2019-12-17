from Intcode import run_program


testprog1 = [1, 0, 0, 0, 99]
testprog2 = [2, 3, 0, 3, 99]
testprog3 = [2, 4, 4, 5, 99, 0]
testprog4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]


def gravity_assist(program, expected_result):
    for noun in range(0, 99):
        for verb in range(0, 99):
            testprog = program[:]
            testprog[1], testprog[2] = noun, verb
            result = run_program(testprog)[0]

            if result[0] == expected_result:
                return (noun * 100) + verb

    return -1, -1


program = [int(a) for a in open("02input.txt").read().strip().split(",")]
program[1] = 12
program[2] = 2
print(run_program(program)[0])
print(gravity_assist(program, 19690720))


# print(run_program(testprog1))
# print(run_program(testprog2))
# print(run_program(testprog3))
# print(run_program(testprog4))


