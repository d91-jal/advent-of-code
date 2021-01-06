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


def find_adjacent_2(table, x_pos, y_pos, symbol):
    vecs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    y_max = len(table) - 1
    x_max = len(table[0]) - 1
    result = 0

    for vec in vecs:
        x = x_pos + vec[0]
        y = y_pos + vec[1]

        if (0 <= x <= x_max) and (0 <= y <= y_max):
            result += 1 if table[y][x] == symbol else 0

    return result


def find_visible(table, x_pos, y_pos, symbol):
    vecs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    y_max = len(table) - 1
    x_max = len(table[0]) - 1
    result = 0 
    floor = ord('.')

    # Find the first non-floor tile in each direction and return the number matching <symbol>.    
    for vec in vecs:        
        x = x_pos + vec[0]
        y = y_pos + vec[1]
        found = False

        while (0 <= x <= x_max) and (0 <= y <= y_max) and not found:            
            if table[y][x] == symbol:
                result += 1
                found = True
            elif table[y][x] == floor:
                x = x + vec[0]
                y = y + vec[1]
            else:
                found = True

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
    free = ord('L')
    occu = ord('#')

    while not stable:
        my_input = copy.deepcopy(my_output)
        stable = True
        iterations += 1

        for y in range(len(my_input)):
            for x in range(len(my_input[0])):
                symbol = my_input[y][x]

                if symbol == free:
                    if find_adjacent_2(my_input, x, y, occu) == 0:
                        my_output[y][x] = occu
                        stable = False
                elif symbol == occu:
                    if find_adjacent_2(my_input, x, y, occu) > 3:
                        my_output[y][x] = free
                        stable = False

    return count(my_output, occu)


def part_2():
    my_output = get_input()
    stable = False
    iterations = 0
    free = ord('L')
    occu = ord('#')

    while not stable:
        my_input = copy.deepcopy(my_output)
        stable = True
        iterations += 1

        for y in range(len(my_input)):
            for x in range(len(my_input[0])):
                symbol = my_input[y][x]

                if symbol == free:
                    if find_visible(my_input, x, y, occu) == 0:
                        my_output[y][x] = occu
                        stable = False
                elif symbol == occu:
                    if find_visible(my_input, x, y, occu) > 4:
                        my_output[y][x] = free
                        stable = False
    
    return count(my_output, occu)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

