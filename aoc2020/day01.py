def find_terms(my_input, bitmap, target_sum):
    for i in my_input:
        if i >= target_sum:
            continue

        if bitmap[target_sum - i] == True:
            # We have a matching term, return result.
            return i, target_sum - i
        else:
            # Set the corresponding bit in the map of available terms.
            bitmap[i] = True

    # No solution found.
    return 0, 0


def part_1():
    # Read input into an array.
    input_file = open("resources/input01.txt")
    my_input = [int(a) for a in input_file.read().strip().split("\n")]
    input_file.close()
    
    # Set up a bit array for keeping track of already tested terms.
    target_sum = 2020
    bitmap = [False for _ in range(target_sum)]
    return find_terms(my_input, bitmap, target_sum)


def part_2():
    # Read input into an array.
    input_file = open("resources/input01.txt")
    my_input = [int(a) for a in input_file.read().strip().split("\n")]
    input_file.close()
    
    # Set up a bit array for keeping track of already tested terms.
    target_sum = 2020
    bitmap = [False for _ in range(target_sum)]
 
    for i in my_input:
        result = find_terms(my_input, bitmap, target_sum - i) 
        if result != (0, 0):
            return i, result[0], result[1]
    
    return 0, 0, 0


def main():
    result1 = part_1()
    print(result1[0], "+", result1[1], "=", sum(result1))
    print(part_2())


if __name__ == "__main__":
    main()