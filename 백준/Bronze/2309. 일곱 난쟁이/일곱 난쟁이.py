import itertools
for comb in list(itertools.combinations([int(input()) for _ in range(9)],7)):
    if sum(comb) == 100:
        for i in sorted(comb):
            print(i)
        break