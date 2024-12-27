def generate_layout(disk_map):
    # Build a hash table of the disk layout - { file_id : [size, empty_space] } 
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
    for front_file in range(len(layout)):
        if front_file > back_file:
            break

        # Process the segment, loop over actual file content and increment checksum.
        # (could be calculated arithmetically but easier to debug this way)
        for _ in range(layout[front_file][0]):
            checksum += front_file * pos
            pos += 1

        # Then fill the empty space of the segment from the back of the file list.
        for _ in range(layout[front_file][1]):
            while layout[back_file][0] == 0:
                back_file -= 1

            if layout[back_file][0] > 0 and back_file > front_file:
                checksum += back_file * pos
                layout[back_file][0] -= 1
                pos += 1
                                                
    return checksum
            

def compact_layout_by_file(layout):
    checksum = 0
    back_file = len(layout) - 1
    pos = 0

    # Loop until front and back pointers collide.
    return checksum


def part_1(my_input):
    layout = generate_layout(my_input[0])
    result = compact_layout(layout)
    return result


def part_2(my_input):
    result = 0
    layout = generate_layout(my_input[0])
    result = compact_layout_by_file(layout)
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