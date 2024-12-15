def validate(pre_pages, post_pages, dep_pages):
    for page in pre_pages:
        if page not in dep_pages:
            return False
        
    for page in post_pages:
        if page in dep_pages:
            return False
        
    return True


def part_1(my_input):
    result = 0
    deps = {}

    # Add all the dependencies for each page number in a list.
    for pair in my_input[0]:
        a, b = map(int, pair.split("|"))
        if b in deps:
            deps[b] += [a]
        else:
            deps[b] = [a]    

    # For each page in a batch, check that all dependencies are in fulfilled.
    for batch in my_input[1]:
        page_list = [int(a) for a in batch.split(",")]
        validated = True
        i = 0 

        while validated and i < len(page_list):
            page_num = page_list[i]
            
            if page_num in deps:                    
                if not validate(page_list[:i], page_list[i:], deps[page_num]):
                    validated = False

            i += 1

        # If validated, or if the page has no dependencies:
        if validated: 
            result += page_list[int((len(page_list) - 1) / 2)]

    return result




def part_2(my_input):
    result = 0

    return result


def main():
    # Read input into a list.
    input_file = open("aoc2024/resources/input05.txt")
    my_input = [a.split() for a in input_file.read().strip().split('\n\n')]
    input_file.close()
    print(part_1(my_input))
    print(part_2(my_input))


if __name__ == "__main__":
    main()