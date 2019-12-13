test1 = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']


def count_sat(universe, planet):
    subuniverse = [pair for pair in universe if pair.split(')')[0] == planet]
    subcount = 0

    for sat in [pair.split(')')[1] for pair in subuniverse]:
        subcount += count_sat(universe, sat)

    return len(subuniverse) + subcount


def find_path(universe, sat):
    result = [sat]

    while True:
        hub = [pair.split(')')[0] for pair in universe if pair.split(')')[1] == sat]

        if len(hub) == 0:
            break
        else:
            result.append(hub[0])
            sat = hub[0]

    result.reverse()
    return result


# my_input = test1
my_input = [a for a in open("06input.txt").read().strip().split("\n")]
# print(my_input)

coms = set([pair.split(")")[0] for pair in my_input])
comdict = dict.fromkeys(coms, 0)

# Brute force solution for part 1.
for com in coms:
    comdict[com] += count_sat(my_input, com)

print(sum(comdict.values()))
# print(comdict)

# For part 2, find closest common ancestors for the two satellites.
you_path = find_path(my_input, "YOU")
san_path = find_path(my_input, "SAN")

# print(you_path)
# print(san_path)

for i in range(min(len(you_path), len(san_path))):
    if you_path[i] != san_path[i]:
        print(you_path[i:])
        print(san_path[i:])
        distance = len(you_path[i:] + san_path[i:]) - 2
        break

print(len(distance) - 2)




