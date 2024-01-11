def part_1(my_input):
    seeds = [int(i) for i in my_input[0].split(": ")[1].split(" ")]
    mappings = [line.split("\n")[1:] for line in my_input[1:]]
    result = float('inf')

    for seed in seeds:
        current = seed

        for mapping in mappings:
            for rng in mapping:
                dest, source, length = map(int, rng.split())
                
                if source <= current <= (source + length):
                    current += (dest - source)
                    break

        result = min(current, result)

    return result


def part_2(my_input):
    return


def main():
    # Read input into a list of strings.
    input_file = open("resources/input05.txt")
    my_input = input_file.read().strip().split("\n\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()