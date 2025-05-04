N = int(input())
result = []
for _ in range(N):
    x,y = map(int,input().split())
    result.append((x,y))
for i in sorted(result, key=lambda k: (k[1],k[0])):
    for j in i:
        print(j,end=' ')
    print()