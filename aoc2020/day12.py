import math


def get_input():
    # Read input.
    input_file = open("resources/input12.txt")
    my_input = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return my_input


# pos = [north_coord, east_coord, heading]
# change = command from input file
def move(pos, change):
    cmd = change[0]
    arg = int(change[1:])

    if cmd == 'N':
        pos[1] += arg
    elif cmd == 'S':
        pos[1] -= arg
    elif cmd == 'E':
        pos[0] += arg
    elif cmd == 'W':
        pos[0] -= arg
    elif cmd == 'L':
        pos[2] -= math.pi * (arg / 180.0)
    elif cmd == 'R':
        pos[2] += math.pi * (arg / 180.0)
    elif cmd == 'F':
        pos[0] += arg * math.cos(pos[2] - (math.pi / 2.0))     # Subtract pi/2 as E=0 in this coordinate system.
        pos[1] += arg * math.sin(pos[2] - (math.pi / 2.0))     # Subtract pi/2 as E=0 in this coordinate system.

    return pos


def part_1():
    my_input = get_input()
    pos = [0, 0, 0]  # pos = [north_coord, east_coord, heading]

    for instr in my_input:
        pos = move(pos, instr)

    return int(abs(pos[0]) + abs(pos[1]))


def part_2():
    my_input = get_input()
    pos = [0, 0, 0]
    waypoint = [1, 10, 0]
    

def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

