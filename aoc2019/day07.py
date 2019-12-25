import itertools
from aoc2019.intcode import IntCode

testprog1 = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
testparams1 = [4, 3, 2, 1, 0]

testprog2 = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
testparams2 = [0, 1, 2, 3, 4]

testprog3 = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32,
             31, 31, 4, 31, 99, 0, 0, 0]
testparams3 = [1, 0, 4, 3, 2]

testprog4 = [3, 26,                 # 00: Input to &26
             1001, 26, -4, 26,      # 02: Subtract 4 from &26 to &26
             3, 27,                 # 06: Input to &27
             1002, 27, 2, 27,       # 08: Multiply &27 by 2 to &27
             1, 27, 26, 27,         # 12: Add &26 and &27 to &27
             4, 27,                 # 16: Output &27
             1001, 28, -1, 28,      # 18: Subtract 1 from &28 to &28
             1005, 28, 6,           # 22: Jump to 6 if &28 != 0
             99,                    # 25:End
             0, 0, 5]  # 26, 27, 28
testparams4 = [9, 8, 7, 6, 5]

testprog5 = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
             -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
             53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
testparams5 = [9, 7, 8, 5, 6]


def part_1():
    input_file = open("resources/07input.txt")
    my_prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    params1 = [0, 1, 2, 3, 4]
    param_sets = list(itertools.permutations(params1))

    highscore = 0

    for param_set in param_sets:
        input_vals = [0, 0]

        for phase in param_set:
            intcode = IntCode()
            input_vals[0] = phase
            intcode.input_buffer = input_vals[:]
            intcode.program = my_prog[:]
            intcode.run_program()

            if len(intcode.output_buffer) > 0:
                input_vals[1] = intcode.output_buffer[0]
                highscore = intcode.output_buffer[0] if intcode.output_buffer[0] > highscore else highscore

    return highscore


def part_2():
    input_file = open("resources/07input.txt")
    my_prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    params1 = [5, 6, 7, 8, 9]
    param_sets = list(itertools.permutations(params1))

    highscore = 0
    ampidx = 0

    for param_set in param_sets:
        # Instantiate the chained amplifiers.
        intcodes = [IntCode(my_prog[:], [param_set[i]]) for i in range(len(param_set))]

        for amp in intcodes:
            amp.running = True

        # Set up the first one with input.
        intcode = intcodes[ampidx]
        input_val = 0

        # Loop continuously through the amplifiers, with any output passed on as input to the next one.
        while True:
            intcode.input_buffer.append(input_val)
            intcode.run_program()
            # Prepare settings for next amplifier.
            ampidx = (ampidx + 1) % len(intcodes)

            # Check latest output if any.
            if len(intcode.output_buffer) > 0:
                input_val = intcode.output_buffer[-1]
                highscore = intcode.output_buffer[-1] if intcode.output_buffer[-1] > highscore else highscore

            # Quit when last amplifier has terminated.
            if not intcodes[-1].running:
                break

            intcode = intcodes[ampidx]

    return highscore


def main():
    print("Day 7 part 1 answer: ", part_1())
    print("Day 7 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()


