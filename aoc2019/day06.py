test1 = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']


def count_sat(universe, body):
    """ Calculate the sum of orbits and sub-orbits (recursively) of a body in the universe. """
    sub_universe = [pair for pair in universe if pair.split(')')[0] == body]
    sub_count = 0

    for sat in [pair.split(')')[1] for pair in sub_universe]:
        sub_count += count_sat(universe, sat)

    return len(sub_universe) + sub_count


def find_path(universe, body):
    """ Trace the path from the center of the universe to a body. """
    result = [body]

    while True:
        hub = [pair.split(')')[0] for pair in universe if pair.split(')')[1] == body]

        if len(hub) == 0:
            break
        else:
            result.append(hub[0])
            body = hub[0]

    result.reverse()
    return result


def part_1():
    """ TODO: Find more efficient solution... """
    input_file = open("resources/06input.txt")
    my_input = [a for a in input_file.read().strip().split("\n")]
    input_file.close()
    coms = set([pair.split(")")[0] for pair in my_input])
    comdict = dict.fromkeys(coms, 0)

    for com in coms:
        comdict[com] += count_sat(my_input, com)

    return sum(comdict.values())


def part_2():
    input_file = open("resources/06input.txt")
    my_input = [a for a in input_file.read().strip().split("\n")]
    input_file.close()
    you_path = find_path(my_input, "YOU")
    san_path = find_path(my_input, "SAN")

    for i in range(min(len(you_path), len(san_path))):
        if you_path[i] != san_path[i]:
            # print(you_path[i:])
            # print(san_path[i:])
            distance = len(you_path[i:] + san_path[i:]) - 2
            break

    return distance


def main():
    print("Day 6 part 1 answer: ", part_1())
    print("Day 6 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()



