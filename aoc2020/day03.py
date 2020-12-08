import math


def count_trees(my_input, move_vec):
    x_pos = 0
    y_pos = 0
    tree_count = 0 

    while y_pos < len(my_input):
        if my_input[y_pos][x_pos] == '#':
            tree_count += 1
        
        x_pos = (x_pos + move_vec[0]) % len(my_input[0])
        y_pos += move_vec[1]

    return tree_count


def part_1():
    # Read input into an array.
    input_file = open("resources/input03.txt")
    my_input = [a for a in input_file.read().strip().split("\n")]
    input_file.close()
    move_vec = (3, 1)
    return count_trees(my_input, move_vec)


def part_2():
    # Read input into an array.
    input_file = open("resources/input03.txt")
    my_input = [a for a in input_file.read().strip().split("\n")]
    input_file.close()
    move_vecs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_count = math.prod(map(lambda x:count_trees(my_input, x), move_vecs))

    return tree_count


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()