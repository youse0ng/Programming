N = int(input())
result = {}
sorting = []
for _ in range(N):
    name, state = input().split()
    result[name] = state
for name in result:
    if result[name] == 'enter':
        sorting.append(name)

for name in sorted(sorting,reverse=True):
    print(name)