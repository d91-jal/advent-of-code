
def validate_page(pre_pages, post_pages, dep_pages):
    for page in pre_pages:
        if page not in dep_pages:
            return page
        
    for page in post_pages:
        if page in dep_pages:
            return page
        
    return -1


def validate_batch(pages, dep_pages):
    validated = True
    fails = []
    i = 0

    while i < len(pages):
        page = pages[i]

        if page in dep_pages:
            fail = validate_page(pages[:i], pages[i:], dep_pages[page])
            if fail >= 0:
                fails += [i, pages.index(fail)]
                break

        i += 1

    return fails


def middle(pages):
    return pages[(len(pages) - 1) // 2]


def build_dependency_map(my_input):
    result = {}

    # Add all the dependencies for each page number in a list.
    for pair in my_input:
        a, b = map(int, pair.split("|"))
        if b in result:
            result[b] += [a]
        else:
            result[b] = [a]    

    return result


def part_1(my_input):
    result = 0
    deps = build_dependency_map(my_input[0])

    # For each page in a batch, check that all dependencies are in fulfilled.
    for batch in my_input[1]:
        pages = [int(a) for a in batch.split(",")]
        fails = validate_batch(pages, deps)

        # If validated, or if the page has no dependencies:
        if len(fails) == 0:
            result += middle(pages)

    return result


def part_2(my_input):
    result = 0
    deps = build_dependency_map(my_input[0])

    # For each page in a batch, check that all dependencies are in fulfilled.
    for batch in my_input[1]:
        pages = [int(a) for a in batch.split(",")]
        fails = validate_batch(pages, deps)
        
        if len(fails) == 0: continue

        # If a rule is broken, switch places of the offending pages.
        while len(fails) > 0:
            pages[fails[0]], pages[fails[1]] = pages[fails[1]], pages[fails[0]]
            fails = validate_batch(pages, deps)
                
        result += middle(pages)

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