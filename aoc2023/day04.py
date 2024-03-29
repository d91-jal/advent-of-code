def part_1(my_input):
    result = 0 

    for row in my_input:
        # Split into winning numbers and own hand.
        card = row.split(":")[1:][0].split("|")
        # List all the winning numbers present in own hand
        match = [i for i in card[0].split(" ") if len(i) > 0 and i in card[1].split(" ")]
        
        # Calculate score
        if len(match) > 0:            
            result += 2**(len(match) - 1) 

    return result


def part_2(my_input):
    result = [0 for i in range(0, len(my_input))]
    rowidx = 0 

    for row in my_input:    
        # Split into winning numbers and own hand.
        card = row.split(":")[1:][0].split("|")
        # List all the winning numbers present in own hand
        match = [i for i in card[0].split(" ") if len(i) > 0 and i in card[1].split(" ")]

        # Add current row + forward matches to result.        
        result[rowidx] += 1
        
        if len(match) > 0:
            for i in range(1, len(match) + 1):
                result[rowidx + i] += (1 * result[rowidx])

        rowidx += 1

    return sum(result)


def main():
    # Read input into a list of strings.
    input_file = open("resources/input04.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()