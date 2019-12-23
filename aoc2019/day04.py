def is_valid_part_1(number):
    """ Loop through all candidate numbers and check if they abide by the rules. """
    if number < 347312 or number > 805915:
        return False

    numstring = str(number)
 
    return numstring[0] <= numstring[1] <= numstring[2] <= numstring[3] <= numstring[4] <= numstring[5] \
        and (            
            numstring[0] == numstring[1] or 
            numstring[1] == numstring[2] or 
            numstring[2] == numstring[3] or
            numstring[3] == numstring[4] or 
            numstring[4] == numstring[5])


def is_valid_part_2(number):
    """ Loop through all candidate numbers and check if they abide by the rules. """
    if number < 347312 or number > 805915:
        return False

    numstring = str(number)

    return numstring[0] <= numstring[1] <= numstring[2] <= numstring[3] <= numstring[4] <= numstring[5] \
        and (
            numstring[0] == numstring[1] != numstring[2] or 
            numstring[0] != numstring[1] == numstring[2] != numstring[3] or 
            numstring[1] != numstring[2] == numstring[3] != numstring[4] or
            numstring[2] != numstring[3] == numstring[4] != numstring[5] or 
            numstring[3] != numstring[4] == numstring[5])


def part_1():
    return len([a for a in range(347312, 805916) if is_valid_part_1(a)])


def part_2():
    return len([a for a in range(347312, 805916) if is_valid_part_2(a)])


def main():
    print("Day 4 part 1 answer: ", part_1())
    print("Day 4 part 2 answer: ", part_2())


if __name__ == "__main__":
    main()
