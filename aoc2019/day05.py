from aoc2019.intcode import IntCode


def run(prog, instr):
    intcode = IntCode()
    intcode.program = prog[:]
    intcode.input_buffer = [instr]
    intcode.run_program()
    return intcode.output_buffer[0]


def part1(prog):
    return run(prog, 1)


def part2(prog):
    return run(prog, 5)


program = [int(a) for a in open("resources/05input.txt").read().strip().split(",")]
print(part1(program))
print(part2(program))

