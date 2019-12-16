import itertools
from Intcode import run_program

testprog1 = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
testparams1 = [4, 3, 2, 1, 0]
testprog2 = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
testparams2 = [0, 1, 2, 3, 4]
testprog3 = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32,
             31, 31, 4, 31, 99, 0, 0, 0]
testparams3 = [1, 0, 4, 3, 2]


# my_input = testprog1
# perms = [testparams1]

my_input = [int(a) for a in open("07input.txt").read().strip().split(",")]
params = [0, 1, 2, 3, 4]
perms = list(itertools.permutations(params))
# print(perms)
highscore = 0

for perm in perms:
    program = my_input[:]
    input_val = 0
    phase_addr = program[1]
    input_addr = program[3]
    output = []

    for phase in perm:
        program[phase_addr] = phase
        program[input_addr] = input_val

        for i in range(4):
            program[i] = 0

        result = run_program(program)
        output.append(str(result[input_addr]))
        input_val = result[phase_addr]
        program = my_input[:]

    highscore = input_val if input_val > highscore else highscore


print(highscore)
