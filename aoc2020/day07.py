def get_input():
    # Read input.
    input_file = open("resources/input07.txt")
    my_input = [a.split(' contain ') for a in input_file.read().strip().split('\n')]
    input_file.close()
    return my_input


def count_contents(table, color):
    result = 0

    for bag in table[color]:
        if bag[1] > 0:
            result += (bag[1] + (bag[1] * count_contents(table, bag[0])))

    return result


def find_containers(result, table, target):
    for color in table[target]:
        result.append(color)

        if color in table:
            find_containers(result, table, color)
    
    return result


def part_1():
    my_input = get_input()
    table = {}

    # Loop over rules...
    for rule in my_input:
        container = rule[0].split(' ')
        container = container[0] + container[1]
        contents = rule[1].split(',')

        # ...create a lookup table with color as key, and all colors able to contain the key color as values.
        for content in contents:
            content_color = content.split()[-3:]
            content_color = content_color[0] + content_color[1]

            if content_color in table:
                (table[content_color]).append(container)
            else:
                table[content_color] = [container]

    possible_containers = []

    # Recursively build a list of all values directly and implicitly pointed to by a start color.
    find_containers(possible_containers, table, 'shinygold')

    return len(set(possible_containers))
    

def part_2():
    my_input = get_input()
    table = {}

    # Loop over rules...
    for rule in my_input:
        container = rule[0].split(' ')
        container = container[0] + container[1]
        contents = rule[1].split(',')

        # ...create a lookup table with color as key, and all colors contained by the key color as values.
        for content in contents:
            all_content = content.strip().split()
            content_color = all_content[-3:]
            content_color = content_color[0] + content_color[1]
            num = 0 if all_content[0] == 'no' else int(all_content[0])

            if container in table:
                (table[container]).append([content_color, num])
            else:
                table[container] = [[content_color, num]]

    # Recursively count all contents of a container.
    return count_contents(table, 'shinygold')


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__": 
    main()
