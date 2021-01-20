def get_input():
    # Read input.
    input_file = open("resources/input13.txt")
    my_input = [a for a in input_file.read().strip().split('\n')]
    input_file.close()
    timestamp = int(my_input[0])
    ids = my_input[1].split(',')
    return (timestamp, ids)


def greatest_common_divisor(a, b):
   while(b):
       a, b = b, a % b

   return a


def smallest_common_multiple(ints):
    result = ints[0]
    
    for i in ints[1:]:
        result = result * i // greatest_common_divisor(result, i)
    
    return result


def part_1():
    my_input = get_input()
    basetime = my_input[0]
    buses = [int(a) for a in my_input[1] if a != 'x']
    # Last departure = basetime mod departure minute.
    # Next departure = departure minute - last departure.
    next_dept = [a - (basetime % a) for a in buses]
    min_index = next_dept.index(min(next_dept))
    return(buses[min_index] * next_dept[min_index])


def part_2():
    my_input = get_input()[1]
    buses = [(i, int(x)) for i, x in enumerate(my_input) if x != "x"]
    # Start with the first bus in the list, looping over its schedule until we 
    # find a matching pattern with any other bus in the list. We then have a 
    # recurring pattern for those two -> Update timestamp increase as smallest
    # common multiple of those schedules.
    # Then repeat until all buses have been matched.
    found = [buses[0]]
    timestamp = sum(found[0])

    while True:
        for idx, bus in buses:
            if (timestamp + idx) % bus == 0:
                if (idx, bus) not in found:
                    found.append((idx, bus))
        
        if len(found) == len(buses):
            return timestamp

        timestamp += smallest_common_multiple([b for (a, b) in found])

    return 0


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

