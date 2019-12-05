test0 = [['R6', 'R2', 'U3']]
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
    # Define the board as a two-dimensional grid.
    size = 20
    board = [[0 for x in range(size)] for y in range(size)]
    current_x = current_y = size // 2
    board[current_x][current_y] = 1

    for wire in wires:
        new_x = new_y = current_x = current_y = size // 2

        for edge in wire:
            direction = edge[0]
            length = int(edge[1:])

            if direction == 'R':
                for x in range(current_x + 1, current_x + length + 1):
                    board[x][current_y] += 1
                    new_x = x

                current_x = new_x
            elif direction == 'L':
                for x in range(current_x - 1, (current_x - length) - 1, -1):
                    board[x][current_y] += 1
                    new_x = x

                current_x = new_x
            elif direction == 'U':
                for y in range(current_y - 1, (current_y - length) - 1, -1):
                    board[current_x][y] += 1
                    new_y = y

                current_y = new_y
            elif direction == 'D':
                for y in range(current_y + 1, current_y + length + 1):
                    board[current_x][y] += 1
                    new_y = y

                current_y = new_y
            else:
                print('Unknown direction supplied: {s}', direction)

    return board


result = initialize_board(test1)
for row in result:
    print(row)
