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

    def __init__(self, program=[], input_buffer=[]):
        self.program = program
        self.input_buffer = input_buffer
        self.output_buffer = []
        self.running = False
        self.p = 0
        self.stdout = False

    def run_program(self):
        result = self.program[:]
        self.running = True
        # self.output_buffer = []

        while self.p < len(result):
            if (self.p + 1 > len(result)) or (result[self.p] == 99):
                self.p = 0
                self.running = False
                break

            opcode, mode1, mode2, mode3 = parse_instruction(str(result[self.p]))

            if opcode == "01":      # Addition
                result[result[self.p + 3]] = get_param(mode1, result, self.p + 1) + get_param(mode2, result, self.p + 2)
                self.p += 4
            elif opcode == "02":    # Multiplication
                result[result[self.p + 3]] = get_param(mode1, result, self.p + 1) * get_param(mode2, result, self.p + 2)
                self.p += 4
            elif opcode == "03":    # Read input
                input_val = self.input_buffer.pop(0) if len(self.input_buffer) > 0 else read_input()
                result[result[self.p + 1]] = input_val
                self.p += 2
            elif opcode == "04":    # Print output
                out_val = result[result[self.p + 1]]
                self.output_buffer.append(out_val)

                if self.stdout:
                    print(out_val)

                self.p += 2
                break
            elif opcode == "05":    # Jump if true
                if get_param(mode1, result, self.p + 1) != 0:
                    self.p = get_param(mode2, result, self.p + 2)
                else:
                    self.p += 3
            elif opcode == "06":    # Jump if false
                if get_param(mode1, result, self.p + 1) == 0:
                    self.p = get_param(mode2, result, self.p + 2)
                else:
                    self.p += 3
            elif opcode == "07":    # Less than
                result[result[self.p + 3]] = \
                    1 if get_param(mode1, result, self.p + 1) < get_param(mode2, result, self.p + 2) else 0
                self.p += 4
            elif opcode == "08":    # Equals
                result[result[self.p + 3]] = \
                    1 if get_param(mode1, result, self.p + 1) == get_param(mode2, result, self.p + 2) else 0
                self.p += 4
            else:                   # Undefined = NOP
                self.p += 1

        self.program = result[:]
        return



