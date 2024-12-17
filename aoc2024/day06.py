import re

directions = { 
        '>' : (0, 1),  # Right
        '<' : (0, -1), # Left
        'v' : (1, 0),  # Down
        '^' : (-1, 0)   # Up
}

def turn_right(dir):
    if dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, 1)
    else:
        return (-1, 0)
    

def part_1(my_input):
    guard = r'\^|v|<|>'
    height = len(my_input)
    width = len(my_input[0])
    result = 1
    done = False
    y = 0
    charmap = []
    
    # Find the starting position and direction, and convert the map into 
    # lists of chars for easier manipulation.
    for line in my_input:
        match = re.search(guard, line)
        charmap.append(list(line))
                
        if match != None:
            dir = directions[match.group(0)]
            pos = (y, (match.span(0)[0]))
            charmap[pos[0]][pos[1]] = 'X'
            print("Initial state:", pos, dir)
        else:
            y += 1

    
    # Traverse the map, updating the count of new locations visited.
    while not done:
        next = tuple(map(lambda x, y: x + y, pos, dir))
        
        if next[0] < 0 or next[1] < 0 or next[0] >= height or next[1] >= width:
            done = True
            break
        elif charmap[next[0]][next[1]] == '.':
            result += 1
            pos = next
            charmap[pos[0]][pos[1]] = 'X'
        elif charmap[next[0]][next[1]] == 'X':
            pos = next
        elif my_input[next[0]][next[1]] == '#':
            dir = turn_right(dir)

    return result


def part_2(my_input):
    result = 0
    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input06.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()