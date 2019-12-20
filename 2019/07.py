import itertools
from IntCode import IntCode


def part1(my_prog, param_sets):
    intcode = IntCode()
    highscore = 0

    for param_set in param_sets:
        input_vals = [0, 0]

        for phase in param_set:
            input_vals[0] = phase
            intcode.input_buffer = input_vals[:]
            intcode.program = my_prog[:]
            intcode.run_program()
            input_vals[1] = intcode.output_buffer[0]

        highscore = intcode.output_buffer[0] if intcode.output_buffer[0] > highscore else highscore

    return highscore


def part2(my_prog, param_sets):
    intcodes = [IntCode(my_prog[:]) for _ in range(5)]
    highscore = 0
    ampidx = 0

    for param_set in param_sets:
        input_vals = [0, 0]

        for phase in param_set:
            input_vals[0] = phase
            intcode = intcodes[ampidx]
            intcode.input_buffer = input_vals[:]
            intcode.run_program()
            input_vals[1] = intcode.output_buffer
            ampidx = (ampidx + 1) % len(intcodes)

        highscore = intcode.output_buffer[0] if intcode.output_buffer[0] > highscore else highscore

    return highscore


testprog1 = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
testparams1 = [4, 3, 2, 1, 0]
testprog2 = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
testparams2 = [0, 1, 2, 3, 4]
testprog3 = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32,
             31, 31, 4, 31, 99, 0, 0, 0]
testparams3 = [1, 0, 4, 3, 2]

# my_input = testprog3
# perms1 = [testparams3]
my_input = [int(a) for a in open("07input.txt").read().strip().split(",")]
params1 = [0, 1, 2, 3, 4]
perms1 = list(itertools.permutations(params1))
# print(perms)
print("Part 1 answer: ", part1(my_input, perms1))

testprog4 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99,
             0, 0, 5]
testparams4 = [9, 8, 7, 6, 5]
testprog5 = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
             -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
             53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
testparams5 = [9, 7, 8, 5, 6]


my_input = testprog4
perms2 = [testparams4]
# params2 = [5, 6, 7, 8, 9]
# perms2 = list(itertools.permutations(params2))

print("Part 2 answer: ", part2(my_input, perms2))
