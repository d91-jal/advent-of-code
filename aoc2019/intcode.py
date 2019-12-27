def parse_instruction(instruction):
    formatted_instr = instruction.rjust(5, "0")
    return formatted_instr[3:5], formatted_instr[2], formatted_instr[1], formatted_instr[0]


def read_input():
    value = ""

    while not value.isdigit():
        value = input("Input: ")

    return int(value)


class IntCode:

    def __init__(self, program=[], input_buffer=[], memory_size=1000):
        self.program = program + ([0] * (memory_size - len(program)))
        self.input_buffer = input_buffer
        self.output_buffer = []
        self.running = False
        self.p = 0
        self.stdout = False
        self.relative_base = 0
        self.memory_size = memory_size

    def get_address(self, mode, index):
        if mode == "0":     # Position mode
            return self.program[index]
        elif mode == "1":   # Immediate mode
            return index
        elif mode == "2":   # Relative mode
            return self.program[index] + self.relative_base

    def get_param(self, mode, index):
        return self.program[self.get_address(mode, index)]

    def set_param(self, mode, index, value):
        self.program[self.get_address(mode, index)] = value

    def run_program(self):
        self.running = True

        while self.p < len(self.program):
            if (self.p + 1 > len(self.program)) or (self.program[self.p] == 99):
                self.p = 0
                self.running = False
                break

            opcode, mode1, mode2, mode3 = parse_instruction(str(self.program[self.p]))

            if opcode == "01":      # Addition
                self.set_param(mode3, self.p + 3, self.get_param(mode1, self.p + 1) + self.get_param(mode2, self.p + 2))
                self.p += 4
            elif opcode == "02":    # Multiplication
                self.set_param(mode3, self.p + 3, self.get_param(mode1, self.p + 1) * self.get_param(mode2, self.p + 2))
                self.p += 4
            elif opcode == "03":    # Read input
                input_val = self.input_buffer.pop(0) if len(self.input_buffer) > 0 else read_input()
                self.set_param(mode1, self.p + 1, input_val)
                self.p += 2
            elif opcode == "04":    # Print output
                out_val = self.get_param(mode1, self.p + 1)
                self.output_buffer.append(out_val)

                if self.stdout:
                    print(out_val)

                self.p += 2
                break
            elif opcode == "05":    # Jump if true
                if self.get_param(mode1, self.p + 1) != 0:
                    self.p = self.get_param(mode2, self.p + 2)
                else:
                    self.p += 3
            elif opcode == "06":    # Jump if false
                if self.get_param(mode1, self.p + 1) == 0:
                    self.p = self.get_param(mode2, self.p + 2)
                else:
                    self.p += 3
            elif opcode == "07":    # Less than
                new_val = 1 if self.get_param(mode1, self.p + 1) < self.get_param(mode2, self.p + 2) else 0
                self.set_param(mode3, self.p + 3, new_val)
                self.p += 4
            elif opcode == "08":    # Equals
                new_val = 1 if self.get_param(mode1, self.p + 1) == self.get_param(mode2, self.p + 2) else 0
                self.set_param(mode3, self.p + 3, new_val)
                self.p += 4
            elif opcode == "09":    # Relative base
                self.relative_base += self.get_param(mode1, self.p + 1)
                self.p += 2
            else:                   # Undefined = NOP
                self.p += 1

        return



