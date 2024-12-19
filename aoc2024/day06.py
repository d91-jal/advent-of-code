
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
            charmap[pos[0]][pos[1]] = 'X'
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
    charmap, pos, dir = build_map(my_input)
    turn_hist = []
        
    # Each time we should take a step forward, look to the right and check if
    # we have already done a turn on that path. That will lead to a loop.
    while not done:
        next = tuple(map(lambda x, y: x + y, pos, dir))
        
        if next[0] < 0 or next[1] < 0 or next[0] >= height or next[1] >= width:
            done = True
            break
        elif my_input[next[0]][next[1]] == '#':
            turn_hist.append(pos)
            dir = turn_right(dir)
        elif charmap[next[0]][next[1]] == '.':
            foo = check_right(charmap, pos, dir, turn_hist)

            if len(foo) > 0: 
                #print(pos, foo)
                result += 1

            pos = next
            charmap[pos[0]][pos[1]] = 'X'
        elif charmap[next[0]][next[1]] == 'X':
            pos = next

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