from aoc2019.intcode import IntCode


def run(prog, instr):
    intcode = IntCode(prog[:], [instr])
    intcode.running = True

    while intcode.running:
        intcode.run_program()

    return intcode.output_buffer[-1]


def part_1():
    input_file = open("resources/05input.txt")
    prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    return run(prog, 1)


def part_2():
    input_file = open("resources/05input.txt")
    prog = [int(a) for a in input_file.read().strip().split(",")]
    input_file.close()
    return run(prog, 5)


def main():
    print("Day 5 part 1 answer: ", part_1())
    print("Day 5 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()


