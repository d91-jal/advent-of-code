import copy


def get_input():
    # Read input.
    input_file = open("resources/input11.txt")
    rows = [a for a in input_file.read().strip().split('\n')]
    my_input = []

    for row in rows:
        my_input.append([ord(a) for a in row])

    input_file.close()
    return my_input


def find_adjacent(table, x_pos, y_pos, symbol):
    result = 0
    y_min = max(0, y_pos - 1)
    y_max = min(y_pos + 1, len(table) - 1)
    x_min = max(0, x_pos - 1)
    x_max = min(x_pos + 1, len(table[0]) - 1)

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if x == x_pos and y == y_pos:
                continue

            result += 1 if table[y][x] == symbol else 0

    return result


def count(table, target):
    result = 0

    for row in table:
        for column in row:
            result += 1 if column == target else 0

    return result


def part_1():
    my_output = get_input()
    stable = False
    iterations = 0

    while not stable:
        my_input = copy.deepcopy(my_output)
        stable = True
        iterations += 1

        for y in range(len(my_input)):
            for x in range(len(my_input[0])):
                symbol = my_input[y][x]

                if symbol == ord('L'):
                    if find_adjacent(my_input, x, y, ord('#')) == 0:
                        my_output[y][x] = ord('#')
                        stable = False
                elif symbol == ord('#'):
                    if find_adjacent(my_input, x, y, ord('#')) > 3:
                        my_output[y][x] = ord('L')
                        stable = False

    return count(my_output, ord('#'))


def part_2():
    return 2


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

