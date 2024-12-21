
def build_map(my_input):
    charmap = []
    y = 0

    # Find the starting position and direction, and convert the map into 
    # lists of chars for easier manipulation.
    for line in my_input:
        x = line.rfind(r'^')
        charmap.append(list(line))
                
        if x >= 0:
            dir = (-1, 0)
            pos = (y, x)
        else:
            y += 1

    return charmap, pos, dir


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
    

def check_right(charmap, pos, dir, hist):
    look_dir = turn_right(dir)

    #return [hist_pos for hist_pos in hist if hist_pos[abs(y)] == pos[abs(y)] and hist_pos[abs(x)] > pos[abs(x)] and charmap[hist_pos[0] + y][hist_pos[1] + x] == '#'] 


    if(look_dir == (0, 1)):        
        return [hist_pos for hist_pos in hist if hist_pos[0] == pos[0] and hist_pos[1] > pos[1] and charmap[hist_pos[0]][hist_pos[1] + 1] == '#'] 
    elif(look_dir == (0, -1)):
        return [hist_pos for hist_pos in hist if hist_pos[0] == pos[0] and hist_pos[1] < pos[1] and charmap[hist_pos[0]][hist_pos[1] - 1] == '#'] 
    elif (look_dir == (1, 0)):
        return [hist_pos for hist_pos in hist if hist_pos[1] == pos[1] and hist_pos[0] > pos[0] and charmap[hist_pos[0] + 1][hist_pos[1]] == '#'] 
    elif (look_dir == (-1, 0)):
        return [hist_pos for hist_pos in hist if hist_pos[1] == pos[1] and hist_pos[0] < pos[0] and charmap[hist_pos[0] - 1][hist_pos[1]] == '#'] 
    

def part_1(my_input):
    height = len(my_input)
    width = len(my_input[0])
    result = 1
    done = False
    charmap, pos, dir = build_map(my_input)
    charmap[pos[0]][pos[1]] = 'X'

        
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
    height = len(my_input)
    width = len(my_input[0])
    done = False
    charmap, orig_pos, orig_dir = build_map(my_input)
    charmap[orig_pos[0]][orig_pos[1]] = '.'
    path = []
    pos = orig_pos
    dir = orig_dir
        
    # First pass, build reference path.
    while not done:
        next = tuple(map(lambda x, y: x + y, pos, dir))
        
        if next[0] < 0 or next[1] < 0 or next[0] >= height or next[1] >= width:
            done = True
            break
        elif charmap[next[0]][next[1]] == '.':
            pos = next
            if pos not in path: path.append(pos) 
        elif my_input[next[0]][next[1]] == '#':
            dir = turn_right(dir)


    # Test with an obstacle for each step along the original path.
    for i in range(len(path)):
        pos = orig_pos
        dir = orig_dir
        test_pos = path[i]
        charmap[test_pos[0]][test_pos[1]] = '#'
        done = False
        new_len = 0

        while not done:
            next = tuple(map(lambda x, y: x + y, pos, dir))
            
            if next[0] < 0 or next[1] < 0 or next[0] >= height or next[1] >= width:
                done = True
                break
            elif charmap[next[0]][next[1]] == '#':
                dir = turn_right(dir)
            elif charmap[next[0]][next[1]] == '.':
                pos = next
                new_len += 1
                    
                    
            if new_len > (len(path) * 2):
                result += 1
                done = True

        charmap[test_pos[0]][test_pos[1]] = '.'
        
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