N,M = map(int,input().split())
backet = list(range(1,N+1))

for _ in range(M):
    i,j = map(int,input().split())
    backet[i-1],backet[j-1] = backet[j-1],backet[i-1]
print(" ".join([str(i) for i in backet]))