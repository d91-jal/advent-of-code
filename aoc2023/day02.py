def part_1(my_input):
    offset = { "red": 0, "green": 1, "blue": 2 }
    id = 0
    result = 0

    for row in my_input:
        id += 1
        # Remove game ID, split actual hands into separate items.
        hands = row.split(":")[1].split(";")
        impossible = False

        for hand in hands:
            cubes = hand.split(",")

            for cube in cubes:
                num_type = cube.strip().split(" ")

                if int(num_type[0]) - offset[num_type[1]] > 12:
                    impossible = True

        if not impossible: 
            result += id

    return result


def part_2(my_input):
    result = 0
    index = { "red": 0, "green": 1, "blue": 2 }

    for row in my_input:
        # Remove game ID, split actual hands into separate items.
        hands = row.split(":")[1].split(";")
        rgb_max = [0, 0, 0]

        for hand in hands:
            cubes = hand.split(",")

            for cube in cubes:
                num_type = cube.strip().split(" ")

                if int(num_type[0]) > rgb_max[index[num_type[1]]]:
                    rgb_max[index[num_type[1]]] = int(num_type[0])

        result += rgb_max[0] * rgb_max[1] * rgb_max[2]

    return result    


def main():
    # Read input into an array.
    input_file = open("resources/input02.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()