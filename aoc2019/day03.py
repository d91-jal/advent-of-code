test0 = [['R6', 'R2', 'U3', 'K3']]
test1 = \
    [['R8', 'U5', 'L5', 'D3'],
     ['U7', 'R6', 'D4', 'L4']]
test2 = \
    [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
     ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
test3 = \
     [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
      ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]


def initialize_board(wires):
    result = []

    # Loop over wire definitions.
    for wire in wires:
        board = {}
        current_x, current_y, steps = 0, 0, 0 

        # Loop over wire sections.
        for edge in wire:
            direction = edge[0]
            length = int(edge[1:])

            # Add each coordinate the section passes to a dictionary and store the cumulative distance. 
            # TODO: refactor code duplication below.
            if direction == 'R':
                for x in range(current_x + 1, current_x + length + 1):
                    steps += 1
                    board[(x, current_y)] = steps
 
                current_x += length 
            elif direction == 'L':
                for x in range(current_x - 1, (current_x - length) - 1, -1):
                    steps += 1
                    board[(x, current_y)] = steps
 
                current_x -= length
            elif direction == 'U':
                for y in range(current_y - 1, (current_y - length) - 1, -1):
                    steps += 1
                    board[(current_x, y)] = steps

                current_y -= length
            elif direction == 'D':
                for y in range(current_y + 1, current_y + length + 1):
                    steps += 1
                    board[(current_x, y)] = steps

                current_y += length
            else:
                print('Unknown direction supplied: ' + direction)
        
        result.append(board)

    return result


def find_crossings(board):
    if len(board) != 2:
        return []

    # Find all intersections of the two wires (i.e. coordinates existing in both wires).
    return list(board[0].keys() & board[1].keys())
        

def find_closest(crossings):
    # Return minimum physical distance from starting point.
    return min([abs(pos[0]) + abs(pos[1]) for pos in crossings])


def find_shortest(board, crossings):
    # Return minimum wire length from starting point.
    return min([board[0][pos] + board[1][pos] for pos in crossings])


def part_1():
    input_file = open("resources/03input.txt")
    my_input = [row.strip().split(',') for row in input_file.read().split('\n')]
    input_file.close()
    my_board = initialize_board(my_input)
    crossings = find_crossings(my_board)
    return find_closest(crossings)


def part_2():
    input_file = open("resources/03input.txt")
    my_input = [row.strip().split(',') for row in input_file.read().split('\n')]
    input_file.close()
    my_board = initialize_board(my_input)
    crossings = find_crossings(my_board)
    return find_shortest(my_board, crossings)


def main():
    print("Day 3 part 1 answer: ", part_1())
    print("Day 3 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()


