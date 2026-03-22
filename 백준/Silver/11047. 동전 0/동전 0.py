N, K = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

counts = 0
for idx in range(N-1,-1,-1):
    if K // coins[idx] == 0:
        continue
    elif K // coins[idx] > 0:
        counts += K//coins[idx]
        K = K - (K//coins[idx] * coins[idx])
print(counts)