def generate_layout(disk_map):
    result = {}
    id_counter = 0

    for i in range(0, len(disk_map), 2):
        file_len = int(disk_map[i])

        if i + 1 < len(disk_map):
            space_len = int(disk_map[i + 1]) 
        else:
            space_len = 0            

        result[id_counter] = [file_len, space_len]

        id_counter += 1

    return result


def compact_layout(layout):
    checksum = 0
    back_file = len(layout) - 1
    pos = 0

    # Loop until front and back pointers collide.
    for i in range(len(layout)):
        if i > back_file:
            break

        # Process the segment, loop over actual file content and increment checksum.
        for j in range(layout[i][0]):
            checksum += i * pos
            pos += 1

        # Then fill the empty space of the segment from the back of the file list.
        for j in range(layout[i][1]):
            while layout[back_file][0] == 0:
                back_file -= 1

            if layout[back_file][0] > 0 and back_file > i:
                checksum += back_file * pos
                layout[back_file][0] -= 1
                pos += 1
                                                
    return checksum
            

def part_1(my_input):
    layout = generate_layout(my_input[0])
    result = compact_layout(layout)
    return result


def part_2(my_input):
    result = 0
    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input09.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()