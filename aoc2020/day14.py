def get_input():
    # Read input.
    input_file = open("resources/input14.txt")
    my_input = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return my_input


def write_to_memory(memory, address, bitmask, value):
    old_value = format(value, 'b').rjust(len(bitmask), '0')
    new_value = []

    for old, bit in zip(old_value, bitmask):
        if bit == 'X':
            new_value += old
        else:
            new_value += bit

    memory[address] = int(''.join(a for a in new_value), 2)


def write_to_memory_v2(memory, address, bitmask, value):
    width = len(bitmask)
    address_b = format(address, 'b').rjust(width, '0')
    addresses = [0]
    
    for i in range(width):         
        if bitmask[i] == '1' or (bitmask[i] == '0' and address_b[i] == '1'):
            for idx in range(len(addresses)):
                addresses[idx] = int(addresses[idx] + 2**(width - i))
        elif bitmask[i] == 'X':
            new_addresses = []

            for a in addresses:
                new_addresses.append(int(a + 2**(width - i)))
            
            addresses += new_addresses

    for a in addresses:
        memory[a] = value


def part_1():
    program = get_input()
    memory = {}
    bitmask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for row in program:
        instr, arg = row.split(' = ')

        if instr == "mask":
            bitmask = arg
        elif instr[:3] == "mem":
            address = int(instr[4:-1])
            write_to_memory(memory, address, bitmask, int(arg))

    return sum(memory.values())


def part_2():
    program = get_input()
    memory = {}
    bitmask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for row in program:
        instr, arg = row.split(' = ')

        if instr == "mask":
            bitmask = arg
        elif instr[:3] == "mem":
            address = int(instr[4:-1])
            write_to_memory_v2(memory, address, bitmask, int(arg))

    return sum(memory.values())


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

