import itertools

params = [0, 1, 2, 3, 4]
my_input = [a for a in open("07input.txt").read().strip().split(",")]

perms = list(itertools.permutations(params))

print(perms)