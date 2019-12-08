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

    #for wire in wires:
    for i in range(len(wires)):
        board = {}
        current_x, current_y, steps = 0, 0, 0 
        wire = wires[i]

        for edge in wire:
            direction = edge[0]
            length = int(edge[1:])

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

    # Find all common points on two wires.
    return list(board[0].keys() & board[1].keys())
        

def find_closest(crossings):
    return min([abs(pos[0]) + abs(pos[1]) for pos in crossings])


def find_shortest(board, crossings):
    return min([board[0][pos] + board[1][pos] for pos in crossings])


my_input = [row.strip().split(',') for row in open("03input.txt").read().split('\n')]
#print(my_input)
board = initialize_board(my_input)
crossings = find_crossings(board)
closest = find_closest(crossings)
shortest = find_shortest(board, crossings)
#print(crossings)
print(closest)
print(shortest)
