def calc_sum(row):
    integers = [i for i in row if i.isdigit()]
    
    if len(integers) > 0:
        return int(integers[0] + integers[-1])

    return 0


def part_1(my_input):
    result = 0
    
    for row in my_input:
        result += calc_sum(row)

    return result


def part_2(my_input):
    num_values = [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), \
                  ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), \
                  ("zero", 0), ("one", 1), ("two", 2), ("three", 3), \
                  ("four", 4), ("five", 5), ("six", 6), ("seven", 7), \
                  ("eight", 8), ("nine", 9)]

    result = 0

    for row in my_input:
        first_num_pos_and_value = (len(row), 0)
        last_num_pos_and_value = (-1, 0) 
    
        for (num, value) in num_values:
            pos = row.find(num)

            if pos < 0:
                continue

            if pos < first_num_pos_and_value[0]:
                first_num_pos_and_value = (pos, value)

            pos = row.rfind(num)

            if pos > last_num_pos_and_value[0]:
                last_num_pos_and_value = (pos, value)
        
        result += (10 * first_num_pos_and_value[1]) + last_num_pos_and_value[1]

    return result


def main():
    # Read input into an array.
    input_file = open("resources/input01.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()