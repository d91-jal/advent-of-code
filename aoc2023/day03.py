def has_symbol(my_input, row, start_col, end_col):
    non_symbols = set('0123456789.')
    from_row = max(0, row - 1)
    to_row = min(len(my_input) - 1, row + 1)
    from_col = max(0, start_col - 1)
    to_col = min(len(my_input[row]) - 1, end_col + 1)

    #print("start_col", start_col, "end_col", end_col)
    #print("rows", from_row, to_row, "cols", from_col, to_col)
    #print(my_input[row][from_col], my_input[row][to_col])

    if start_col > 0 and my_input[row][from_col] not in non_symbols:
        return True
    if my_input[row][to_col] not in non_symbols:
        return True
    
    for col in range(from_col, to_col + 1):
        if my_input[from_row][col] not in non_symbols:
            return True
        if my_input[to_row][col] not in non_symbols:
            return True
        
    return False


def has_gear(my_input, row, start_col, end_col):
    from_row = max(0, row - 1)
    to_row = min(len(my_input) - 1, row + 1)
    from_col = max(0, start_col - 1)
    to_col = min(len(my_input[row]) - 1, end_col + 1)

    if start_col > 0 and my_input[row][from_col] == '*':
        return (row, from_col)
    if my_input[row][to_col] == '*':
        return (row, to_col)
    
    for col in range(from_col, to_col + 1):
        if my_input[from_row][col] == '*':
            return (from_row, col)
        if my_input[to_row][col] == '*':
            return (to_row, col)

    return None


def get_numbers(my_input):
    digits = set('0123456789')
    result = []

    # Scan each row for integers
    for row in range(0, len(my_input)):
        # Initialize new scan
        start_col = end_col = -1

        for col in range(0, len(my_input[row])):
            if my_input[row][col] in digits:
                # Mark start of scan if found
                if start_col == -1:
                    start_col = col
            else:
                # Mark end of scan if found
                if start_col > -1:
                    end_col = col - 1
            
            # Ugly special case for end of row.
            if col == len(my_input[row]) - 1 and end_col == -1 and start_col > -1:
                end_col = col

            # If an integer has been scanned, check for symbols around it.
            if end_col >= start_col > -1:
                result.append((row, start_col, end_col, int(my_input[row][start_col:end_col + 1])))
                start_col = end_col = -1
        
    return result


def part_1(my_input):
    # Get a list of number tuples from the input (row, start column, end column, value)
    numbers = get_numbers(my_input)
    result = 0

    for number in numbers:
        if has_symbol(my_input, number[0], number[1], number[2]):
            result += number[3]
        
    return result


def part_2(my_input):
    # Get a list of number tuples from the input (row, start column, end column, value)
    numbers = get_numbers(my_input)
    gears = {}

    for number in numbers:
        gear_pos = has_gear(my_input, number[0], number[1], number[2])
        
        if gear_pos != None:
            if gear_pos in gears:
                gears[gear_pos].append(number[3])                
            else:
                gears[gear_pos] = [number[3]]
        
    #print(gears)
    return sum([gears[i][0] * gears[i][1] for i in gears if len(gears[i]) == 2])


def main():
    # Read input into a list.
    input_file = open("resources/input03.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()