def all_sub_lists(lst):
    result = []

    for i in range(len(lst)):
        new_list = lst[:i] + lst[i+1:]
        result.append(new_list)
    
    return result


def is_safe(levels):
    diffs = [b - a for a, b in zip(levels[:-1], levels[1:])]
    growing = diffs[0] > 0
    safe = True
    
    for i in diffs:
        if i == 0 or abs(i) > 3 or (i > 0) != growing:
            safe = False
            break

    return safe


def part_1(my_input):
    result = 0

    for line in my_input:
        levels = [int(a) for a in line.split()]
    
        if is_safe(levels):
            result += 1
#        levels = [int(a) for a in line.split()]
#        diffs = [b - a for a, b in zip(levels[:-1], levels[1:])]
#        growing = diffs[0] > 0
#        safe = True
        
#        for i in diffs:
#            if i == 0 or abs(i) > 3 or (i > 0) != growing:
#                safe = False
#                break

#        if safe:
#            result += 1
            
    return result


def part_2(my_input):
    result = 0

    for line in my_input:
        levels = [int(a) for a in line.split()]

        if is_safe(levels):
            result += 1
        else:
            all_sub_levels = all_sub_lists(levels)

            for sub_levels in all_sub_levels:
                if is_safe(sub_levels):
                    result += 1
                    break

    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input02.txt")
    my_input = input_file.readlines()
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()