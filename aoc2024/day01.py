def part_1(my_input):
    list1, list2 = zip(*(map(int, line.split()) for line in my_input))
    list1 = sorted(list(list1))
    list2 = sorted(list(list2))

    result = sum(abs(a - b) for a, b in zip(list1, list2))
    
    return result

def part_2(my_input):
    result = 0

    return result



def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input01.txt")
    my_input = input_file.readlines()
    input_file.close()

    print(part_1(my_input))
    #print(part_2(my_input))


if __name__ == "__main__":
    main()