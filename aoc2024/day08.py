def solve(my_input, rep_range):
    result = 0    
    nodes = {}
    antinodes = {}
    height = len(my_input)
    width = len(my_input[0])

    # Loop over the input.
    for i in range(height):
        line = my_input[i]

        for j in range(width):
            if line[j] != '.':
                if line[j] not in nodes:
                    # For each non . character, add it and its coords to the node map if not already present.
                    nodes[line[j]] = [(i, j)]
                else:
                    # If it is present, calculate the antinode coords for each new pair of coords and add 1 to the result 
                    # if the antinode coords are not in the node map.
                    for node in nodes[line[j]]:
                        # The antinodes are placed in line with the two nodes, at the same distance
                        # from each node as the distance between the two nodes.
                        offset = (abs(i - node[0]), abs(j - node[1]))
                        
                        for rep in rep_range:
                            y = min(node[0], i) - rep * offset[0]
                            x = node[1] + rep * offset[1] if j < node[1] else node[1] - rep * offset[1]
                            antinode = (y, x)
                            
                            if 0 <= y < height and 0 <= x < width and antinode not in antinodes:
                                result += 1
                                antinodes[antinode] = antinode

                            y = max(node[0], i) + rep * offset[0]
                            x = j - rep * offset[1] if j < node[1] else j + rep * offset[1]
                            antinode = (y, x)

                            if 0 <= y < height and 0 <= x < width and antinode not in antinodes:
                                result += 1
                                antinodes[antinode] = antinode

                    # Also, add the new coords to the list of coords for that character.
                    nodes[line[j]].append((i, j))

    return result


def part_1(my_input):
    # Solve for a single offset.
    return solve(my_input, range(1, 2))


def part_2(my_input):
    # Solve for a range of offsets 0 to the size of the input.
    return solve(my_input, range(len(my_input)))


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input08.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()