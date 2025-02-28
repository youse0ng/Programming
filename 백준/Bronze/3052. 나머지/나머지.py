ListRest = []
for _ in range(10):
    n = int(input())
    ListRest.append(n%42)
print(len(set(ListRest)))
