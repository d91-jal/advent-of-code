import string


def convert_input_to_seat_ids():
    # Read input into an array of passport parameter lists.
    input_file = open("resources/input05.txt")

    # F=0, B=1, L=0, R=1 in this binary representation.
    my_input = [a.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1') \
        for a in input_file.read().strip().split('\n')]
    
    input_file.close()
    seat_ids = [(int(a[:7], 2) * 8) + int(a[7:], 2) for a in my_input]
    return seat_ids


def part_1():
    seat_ids = convert_input_to_seat_ids()
    return max(seat_ids)
    

def part_2():
    seat_ids = convert_input_to_seat_ids()
    # The id of the missing seat must be the difference between the sum of 
    # all possible seat ids and the sum of the ones actually in the list. 
    return (((max(seat_ids) + min(seat_ids)) / 2) * (len(seat_ids) + 1)) - sum(seat_ids)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__": 
    main()
