def get_input():
    # Read input into an array of answer lists.
    input_file = open("resources/input06.txt")
    # Items are separated by a blank row.
    my_input = [a.split() for a in input_file.read().strip().split('\n\n')]
    input_file.close()
    # Put each group into a single list item and remove duplicates within each item.
    return my_input


def part_1():
    merged_input = [set(''.join(a)) for a in get_input()] 
    return sum(len(a) for a in merged_input)


def part_2():
    my_input = get_input()
    section = []

    for group in my_input:
        l = []

        for yes_answers in group:
            # Split up each character string into a set of characters
            foo = set(''.join(a) for a in yes_answers)
            l.append(foo)

        # For each group of yes answers, get the ones present in all members of the group.
        section.append(len(set.intersection(*l)))

    return sum(section)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__": 
    main()
