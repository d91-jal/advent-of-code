test1 = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']


def count_sat(universe, planet):
    subuniverse = [pair for pair in universe if pair.split(')')[0] == planet]
    subcount = 0

    for sat in [pair.split(')')[1] for pair in subuniverse]:
        subcount += count_sat(universe, sat)

    return len(subuniverse) + subcount


# my_input = test1
my_input = [a for a in open("06input.txt").read().strip().split("\n")]
coms = set([pair.split(")")[0] for pair in my_input])
comdict = dict.fromkeys(coms, 0)

for com in coms:
    comdict[com] += count_sat(my_input, com)

print(sum(comdict.values()))
print(comdict)




