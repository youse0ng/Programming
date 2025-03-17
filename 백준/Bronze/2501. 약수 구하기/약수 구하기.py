N, K = map(int,input().split())
factors = []
for i in range(1,N+1):
    if N % i == 0:
        factors.append(i)
try: 
    print(factors[K-1])
except:
    print(0)