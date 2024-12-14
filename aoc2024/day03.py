import re


def part_1(my_input):
    expr = r'mul\((\d+),(\d+)\)'
    result = 0

    for line in my_input:
        for args in re.findall(expr, line):
            result += (int(args[0]) * int(args[1]))

    return result


def part_2(my_input):
    do = r'do\(\)'
    dont = r'don\'t\(\)'
    expr = r'mul\((\d+),(\d+)\)'
    result = 0 
    merged_input = ''.join(my_input)
    
    # Partition on do() instructions.
    for start in re.split(do, merged_input):
        # Find cutoff for each do.
        remaining = re.split(dont, start)[0]
        # Parse the cleaned instructions.
        for args in re.findall(expr, remaining):
            result += (int(args[0]) * int(args[1]))
            
    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input03.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()