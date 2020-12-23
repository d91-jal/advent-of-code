def get_input():
    # Read input.
    input_file = open("resources/input09.txt")
    my_input = [int(a) for a in input_file.read().strip().split('\n')]
    input_file.close()
    return my_input


# Basically the same solution as day 1 adapted to the larger search space.
def terms_exist(num_list, target_idx, preamble_length):
    terms = set()

    for x in range(target_idx - preamble_length, target_idx):
        target_sum = num_list[target_idx]
        i = num_list[x]

        if i >= target_sum:
            continue

        # Check if this term has a matching term in the preamble.
        if (target_sum - i) in terms:            
            # We have a matching term, return result.
            return True
        else:
            # Add the tested term to the set.
            terms.add(i)

    # No solution found.
    return False


def find_contiguous_terms(num_list, sum_idx):
    # Find a contiguous range of numbers which add up to the number in num_list[sum_idx].
    target = num_list[sum_idx]
    high_idx = sum_idx - 1
    low_idx = high_idx - 1
    result = num_list[high_idx] + num_list[low_idx]

    while result != target:
        # No result found, return 0 as indication of failure.
        if low_idx <= 0:
            return low_idx

        # Begin by making sure we have a valid starting point
        while num_list[high_idx] > target or result > target:
            high_idx -= 1
            low_idx = high_idx - 1 
            result = num_list[high_idx] + num_list[low_idx]

        # Grow the range as long as the sum is less than the target.
        while result < target and low_idx > 0:
            low_idx -= 1
            result += num_list[low_idx]
        
    return min(num_list[low_idx:high_idx+1]) + max(num_list[low_idx:high_idx+1])


def part_1():
    my_input = get_input()
    preamble_length = 25

    for i in range(preamble_length, len(my_input)):
        if terms_exist(my_input, i, preamble_length):
            i += 1
        else: 
            return my_input[i]

    return 0


def part_2():
    my_input = get_input()
    target = part_1()
    target_idx = 0

    while my_input[target_idx] != target:
        target_idx += 1

    return find_contiguous_terms(my_input, target_idx)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__": 
    main()