def part_1(my_input):
    list1, list2 = zip(*(map(int, line.split()) for line in my_input))
    list1 = sorted(list(list1))
    list2 = sorted(list(list2))

    result = sum(abs(a - b) for a, b in zip(list1, list2))
    
    return result


def part_2(my_input):
    list1, list2 = zip(*(map(int, line.split()) for line in my_input))
    list1 = sorted(list(list1))
    map2 = {}
    
    for num in list2:
        if num in map2:
            map2[num] += 1
        else:
            map2[num] = 1

    result = 0

    for num in list1:
        if num in map2:
            result += num * map2[num]

    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input01.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()