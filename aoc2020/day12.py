import math


def get_input():
    # Read input.
    input_file = open("resources/input12.txt")
    my_input = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return my_input


def part_1():
    my_input = get_input()
    pos = [0, 0]
    heading = 0   # E=0, S=pi/2, W=pi, N=3pi/2
    
    for instr in my_input:
        cmd = instr[0]
        arg = int(instr[1:])

        if cmd == 'N':
            pos[1] += arg
        elif cmd == 'S':
            pos[1] -= arg
        elif cmd == 'E':
            pos[0] += arg
        elif cmd == 'W':
            pos[0] -= arg
        elif cmd == 'L':
            heading -= math.pi * (arg / 180.0)
        elif cmd == 'R':
            heading += math.pi * (arg / 180.0)
        elif cmd == 'F':
            pos[0] += arg * math.cos(heading - (math.pi / 2.0))     # Subtract pi/2 as E=0 in this coordinate system.
            pos[1] += arg * math.sin(heading - (math.pi / 2.0))     # Subtract pi/2 as E=0 in this coordinate system.

    return int(abs(pos[0]) + abs(pos[1]))


def part_2():
    return 2
    

def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

