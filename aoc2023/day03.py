def find_adjacent_sum(my_input, row, col):
    return 0


def part_1(my_input):
    non_symbols = set('0123456789.')
    digits = set('0123456789')
    result = 0 

    for row in my_input:  # row in range(0, len(my_input) - 1):
        ints = [(s, row.index(s)) for s in row.split(".") if len(s) > 0]# [int(s) for s in row.split(".") if s.isdigit()]
        print(ints)

                

        #result += find_adjacent_sum(my_input, row, col)
                # print(my_input[row][col])
        
    return


def part_2(my_input):
    return





def main():
    # Read input into an array.
    input_file = open("resources/input03.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()