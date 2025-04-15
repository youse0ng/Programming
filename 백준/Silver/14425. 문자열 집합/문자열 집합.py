N,M = map(int,input().split())
primary = set()
result = 0 
for _ in range(N):
    primary.add(input())
for _ in range(M):
    checkstring = input()
    if checkstring in primary:
        result +=1 
print(result)