from itertools import permutations
n = int(input())
m = int(input())
perm = []
for _ in range(n):
    perm.append(input())

result = []

for comb in permutations(perm,m):
    card = ''
    for num in comb:
        card += num
    result.append(card)
print(len(set(result)))