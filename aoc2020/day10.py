def get_input():
    # Read input.
    input_file = open("resources/input10.txt")
    my_input = [int(a) for a in input_file.read().strip().split('\n')]
    input_file.close()
    my_input.sort()
    my_input.insert(0, 0)
    my_input.append(my_input[-1] + 3)
    return my_input


def part_1():
    my_input = get_input()
    jolt_1_count = 0
    jolt_3_count = 0

    for i in range(1, len(my_input)):
        if my_input[i] - my_input[i - 1] == 1:
            jolt_1_count += 1
        elif my_input[i] - my_input[i - 1] == 3:
            jolt_3_count += 1

    return jolt_1_count * jolt_3_count


# Idea:
# 1) Read input. 
# 2) Sort input. Add 0 and max + 3 to start and end.
# 3) Split into subchains whereever the difference between two items is 3.
# 4) Each subchain represents a fork in the solution tree with all valid 
#    combos of the subchain as paths.
# 5) The first and last item in each subchain are not optional, so count all
#    combinations of the middle x items => 2^x possible combinations.
# 6) ...but, if the first and last item are more than three jolts apart, then
#    we cannot exclude all items => fewer combos. 
# 7) The answer is the product of the possible paths of all forks.
def part_2():
    my_input = get_input()
    combos = 1
    sublength = 1

    for i in range(len(my_input) - 1):
        if my_input[i + 1] - my_input[i] == 1:
            sublength += 1
        else:
            # TODO: This is not a general solution, it only works for diffs of 1 or 3 jolts.
            if sublength > 4:  
                forks = (2 ** (sublength - 2)) - 1
            elif sublength > 1:
                forks =  2 ** (sublength - 2)
            else: 
                forks = 1

            combos *= forks
            sublength = 1

    return combos


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__": 
    main()