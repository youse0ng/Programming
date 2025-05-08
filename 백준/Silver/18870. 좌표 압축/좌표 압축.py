N = int(input())
initial = list(map(int,input().split()))
result = sorted(list(set(initial)))
mapping = {order:idx for idx,order in enumerate(result)}
for element in initial:
    print(mapping[element],end=' ')