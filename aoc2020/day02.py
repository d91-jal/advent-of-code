def validate_pwd_policy_1(pwd, chars, min_occ, max_occ):    
    chars_count = pwd.count(chars)
    return chars_count >= min_occ and chars_count <= max_occ


def validate_pwd_policy_2(pwd, char, pos_1, pos_2):    
    return (pwd[pos_1 - 1] == char) ^ (pwd[pos_2 - 1] == char)


def part_1():
    # Read input into an array.
    input_file = open("resources/input02.txt")
    my_input = [a for a in input_file.read().strip().split("\n")]
    input_file.close()
    
    valid_count = 0
    
    for row in my_input:
        params = row.split(" ")
        occ = params[0].split("-")
        min_occ = int(occ[0])
        max_occ = int(occ[1])

        if validate_pwd_policy_1(params[2], (params[1])[0], min_occ, max_occ):
            valid_count += 1 

    return valid_count
    

def part_2():
    # Read input into an array.
    input_file = open("resources/input02.txt")
    my_input = [a for a in input_file.read().strip().split("\n")]
    input_file.close()
    
    valid_count = 0
    
    for row in my_input:
        params = row.split(" ")
        pos = params[0].split("-")
        pos_1 = int(pos[0])
        pos_2 = int(pos[1])

        if validate_pwd_policy_2(params[2], (params[1])[0], pos_1, pos_2):
            valid_count += 1 

    return valid_count


def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()