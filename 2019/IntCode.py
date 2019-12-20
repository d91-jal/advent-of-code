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


class IntCode:

    def __init__(self, program=[]):
        self.program = program
        self.input_buffer = []
        self.output_buffer = []

    def run_program(self):
        """ The input_vals parameter can be used to send in pre-defined inputs.
            These will be used instead of prompting the user for input until all
            have been used up.

            Returns a tuple containing
                [0] result: the program state after execution has finished
                [1] output_buffer: any output values yielded during execution
            """

        result = self.program[:]
        self.output_buffer = []
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
                input_val = self.input_buffer.pop(0) if len(self.input_buffer) > 0 else read_input()
                result[result[p + 1]] = input_val
                p += 2
            elif opcode == "04":    # Print output
                out_val = result[result[p + 1]]
                self.output_buffer.append(out_val)
                print(out_val)
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

        self.program = result[:]
        return



