def get_notes():
    input_file = open("resources/input16_1.txt")
    notes = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return notes


def get_ticket():
    input_file = open("resources/input16_2.txt")
    notes = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return notes


def get_nearby_tickets():
    input_file = open("resources/input16_3.txt")
    notes = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    return notes


def get_valid_numbers():
    notes = get_notes()
    intervals = []
    match_list = []

    for note in notes:
        parts = note.split(": ")
        for part in parts[1].split(" or "):
            intervals.append(part)

    for x in intervals:
        interval = x.split('-')
        match_list.append((int(interval[0]), int(interval[1])))

    return match_list


def part_1():
    valid = get_valid_numbers()
    
    
    print(match_list)



    return 1


def part_2():
    return 2


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
