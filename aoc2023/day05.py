def part_1(my_input):
    seeds = [int(i) for i in my_input[0].split(": ")[1].split(" ")]
    mappings = [line.split("\n")[1:] for line in my_input[1:]]
    result = float('inf')

    # For each seed...
    for seed in seeds:
        current = seed

        # ...iterate over the mappings to find the final location value.
        for mapping in mappings:
            for rng in mapping:
                dest, source, length = map(int, rng.split())
                
                if source <= current <= (source + length):
                    current += (dest - source)
                    break

        result = min(current, result)

    return result


def merge_maps(list1, list2):
    # Combine the two lists
    #print("list1", list1)
    #print("list2", list2)
    combined_list = list1 + list2
    #print("combined_list", combined_list)
    # Sort the combined list based on the start points of the ranges
    combined_list.sort(key=lambda x: x[0])
    print("sorted combined_list", combined_list)
    
    # Initialize the result list.
    result = []
    
    # Iterate through the sorted list and split overlapping or adjacent ranges
    for current_range in combined_list:
        if not result or current_range[0] >= result[-1][1]:
            # Non-overlapping range, add it to the result
            result.append(current_range)
        else:
            # Overlapping, split into separate ranges.
            result[-1] = (result[-1][0], current_range[0] - 1, result[-1][2])
            result.extend([(result[-1][1] + 1, current_range[0], result[-1][2] + current_range[2]), current_range])
    
    print("result", result)
    return result


def part_2(my_input):
    iterator = iter(my_input[0].split(": ")[1].split(" "))
    seeds = [(int(i), int(i) + int(next(iterator))) for i in iterator]
    tmp_maps = [line.split("\n")[1:] for line in my_input[1:]]
    mappings = []
        
    for tmp_map in tmp_maps:
        for rng in tmp_map:
            s2, s1, length = (int(x) for x in rng.split())
            mappings.append((s1, s1 + length  - 1, s2 - s1))

    result_map = []

    # Flatten the nested mappings into one, aggregated seed -> location mapping.
    for mapping in mappings:
        result_map = merge_maps(result_map, [mapping])
            
    print(result_map)
    result = float('inf')

    # For each seed...
    for seed in seeds:
        print("seed", seed)
        for endpoint in seed:
            current = endpoint

            # ...iterate over the mappings to find the final location value.
            for rng in result_map:                   
                if rng[0] <= current <= rng[1]:
                    current += rng[2]
                    break

            #print(current, result)
            result = min(current, result)

    return result


def main():
    # Read input into a list of strings.
    input_file = open("resources/example05.txt")
    my_input = input_file.read().strip().split("\n\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()