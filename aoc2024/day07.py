from itertools import product

def part_1(my_input):
    result = 0    

    for line in my_input:
        target, terms = line.split(":")
        target = int(target)
        terms = [int(a) for a in terms.strip().split()]
        # Generate a list of all possible combinations of operations for the 
        # current list of operands.
        operations = list(product(['+', '*'], repeat=len(terms) - 1))

        # Loop over the possible combinations of the current list length.
        for i in range(len(operations)):
            total = terms[0]
            ops = operations[i]

            # Apply operations to operands from left to right.
            for j in range(len(ops)):
                op = ops[j]

                if op == '+':
                    total += terms[j+1]
                else:
                    total *= terms[j+1]
                
                if total > target:
                    break

            # Check if we have a match.
            if total == target:
                result += target
                break

    return result


def part_2(my_input):
    result = 0    

    for line in my_input:
        target, terms = line.split(":")
        target = int(target)
        terms = [int(a) for a in terms.strip().split()]
        # Generate a list of all possible combinations of operations for the 
        # current list of operands.
        operations = list(product(['+', '*', '|'], repeat=len(terms) - 1))

        # Loop over the possible combinations of the current list length.
        for i in range(len(operations)):
            total = terms[0]
            ops = operations[i]

            # Apply operations to operands from left to right.
            for j in range(len(ops)):
                op = ops[j]

                if op == '+':
                    total += terms[j+1]
                elif op == '*':
                    total *= terms[j+1]
                elif op == '|':
                    total = int(str(total) + str(terms[j+1]))

                if total > target:
                    break   

            # Check if we have a match.
            if total == target:
                result += target
                break

    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input07.txt")
    my_input = input_file.read().strip().split("\n")
    input_file.close()

    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()