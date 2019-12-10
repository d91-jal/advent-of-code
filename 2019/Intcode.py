def run_program(program):
    result = program[:]
    p = 0

    while p < len(result):
        if (p + 1 > len(result)) or (result[p] == 99):
            break

        opcode, mode1, mode2, mode3 = parse_instruction(str(result[p]))

        if opcode == "01":      # Addition
            result[result[p + 3]] = get_param(mode1, result, p + 1) + get_param(mode2, result, p + 2)
            p += 4
        elif opcode == "02":    # Multiplication
            result[result[p + 3]] = get_param(mode1, result, p + 1) * get_param(mode2, result, p + 2)
            p += 4
        elif opcode == "03":    # Read input
            result[result[p + 1]] = read_input()
            p += 2
        elif opcode == "04":    # Print output
            print(result[result[p + 1]])
            p += 2
        elif opcode == "05":    # Jump if true
            if get_param(mode1, result, p + 1) != 0:
                p = get_param(mode2, result, p + 2)
            else:
                p += 3
        elif opcode == "06":    # Jump if false
            if get_param(mode1, result, p + 1) == 0:
                p = get_param(mode2, result, p + 2)
            else:
                p += 3
        elif opcode == "07":    # Less than
            result[result[p + 3]] = 1 if get_param(mode1, result, p + 1) < get_param(mode2, result, p + 2) else 0
            p += 4
        elif opcode == "08":    # Equals
            result[result[p + 3]] = 1 if get_param(mode1, result, p + 1) == get_param(mode2, result, p + 2) else 0
            p += 4
        else:
            p += 1

    return result


def parse_instruction(instruction):
    formatted_instr = instruction.rjust(5, "0")
    return formatted_instr[3:5], formatted_instr[2], formatted_instr[1], formatted_instr[0]


def get_param(mode, program, index):
    if mode == "1":
        return program[index]
    elif mode == "0":
        return program[program[index]]


def read_input():
    value = ""

    while not value.isdigit():
        value = input("Input: ")

    return int(value)

