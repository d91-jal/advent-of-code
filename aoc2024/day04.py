
def count_adjacent(my_input, line, col, phrase):
    result = 0
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-right
        (1, -1), # Down-left
        (-1, 1), # Up-right
        (-1, -1) # Up-left
    ]

    def check_direction(line_offset, col_offset):
        for i, c in enumerate(phrase, 1):
            new_line = line + i * line_offset
            new_col = col + i * col_offset

            if not (0 <= new_line < len(my_input) and 0 <= new_col < len(my_input[0])):
                return False
            
            if my_input[new_line][new_col] != c:
                return False
            
        return True

    for line_offset, col_offset in directions:
        if check_direction(line_offset, col_offset):
            result += 1

    return result


def count_cross(my_input, line, col, phrase):
    first = my_input[line - 1][col - 1] + my_input[line + 1][col + 1]
    second = my_input[line + 1][col - 1] + my_input[line - 1][col + 1]

    if (first == phrase or first == phrase[::-1]) and (second == phrase or second == phrase[::-1]):
        return 1
    
    return 0
        

def part_1(my_input):
    result = 0
    target = "XMAS"

    for line in range(len(my_input)):
        for col in range(len(my_input[line])):
            if my_input[line][col] == target[0]:
                result += count_adjacent(my_input, line, col, target[1:])

    return result


def part_2(my_input):
    result = 0

    for line in range(1, len(my_input) - 1):
        for col in range(1, len(my_input[line]) - 1):
            if my_input[line][col] == "A": 
                result += count_cross(my_input, line, col, "MS")

    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input04.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()