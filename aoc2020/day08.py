def get_input():
    # Read input.
    input_file = open("resources/input08.txt")
    my_input = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return my_input


def run_prog(prog):
    ret_code = 0
    diary = [False for _ in range(len(prog))]
    acc = 0
    line = 0

    while True:
        if line == len(prog):
            ret_code = 0
            break

        if 0 > line > len(prog): # Seg fault
            ret_code = -1
            break

        if diary[line]: # Already been here...
            ret_code = -2
            break
        else:
            diary[line] = True
        
        cmd = prog[line].split()
        instr = cmd[0]
        arg = int(cmd[1])

        if instr == 'jmp':
            line += arg
            continue
        elif instr == 'acc':
            acc += arg

        line += 1
        
    return (ret_code, acc)


def part_1():
    prog = get_input()
    (_, acc) = run_prog(prog)
    return acc


def part_2():
    orig_prog = get_input()
    prog = orig_prog.copy()
    (ret_code, acc) = run_prog(prog)
    idx = 0

    # Todo: improve
    while ret_code != 0:        
        idx += 1
        prog = orig_prog[:]
        cmd = prog[idx].split()

        while cmd[0] == 'acc':
            idx += 1
            cmd = prog[idx].split()

        if cmd[0] == 'nop':
            prog[idx] = prog[idx].replace('nop', 'jmp')
        else: 
            prog[idx] = prog[idx].replace('jmp', 'nop')

        (ret_code, acc) = run_prog(prog)
    
    return acc


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__": 
    main()
