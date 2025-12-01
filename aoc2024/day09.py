def generate_layout(disk_map):
    # Build a hash table of the disk layout - { file_id : [size, empty_space, pos] } 
    result = {}
    id_counter = 0
    pos = 0

    for i in range(0, len(disk_map), 2):
        file_len = int(disk_map[i])

        if i + 1 < len(disk_map):
            space_len = int(disk_map[i + 1]) 
        else:
            space_len = 0            

        result[id_counter] = [file_len, space_len, pos]

        id_counter += 1
        pos += file_len + space_len

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
            

def calc_file_checksum(id, pos, size):
    avg = ((id * pos) + (id * (pos + size - 1))) / 2
    return int(avg * size)


def compact_layout_by_file(layout):
    checksum = 0
    pos = 0

    # Since we're updating the checksum on the fly we first need it for the original layout.
    for id in range(len(layout)):
        checksum += calc_file_checksum(id, pos, layout[id][0])  
        pos += layout[id][0] + layout[id][1]

    # Then we loop from back to front.
    for back_file in range(len(layout) - 1, 0, -1):
        back_size = layout[back_file][0]
        back_pos = layout[back_file][2]
        best_fit = back_file

        for front_file in range(len(layout)):
            front_size = layout[front_file][0]
            front_space = layout[front_file][1]
            front_pos = layout[front_file][2]

            # Find the slot closest to the front where the file fits.
            if back_size <= front_space and back_pos > front_pos and front_pos < layout[best_fit][2]:
                best_fit = front_file

        if layout[best_fit][2] < back_pos:            
            front_size = layout[best_fit][0]
            front_space = layout[best_fit][1]
            front_pos = layout[best_fit][2]
            # Move file and adjust checksum
            checksum -= calc_file_checksum(back_file, back_pos, back_size)
            layout[back_file][2] = front_pos + front_size
            layout[back_file][1] = front_space - back_size
            layout[best_fit][1] = 0
            checksum += calc_file_checksum(back_file, layout[back_file][2], back_size)

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