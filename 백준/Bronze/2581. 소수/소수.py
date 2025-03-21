primes = []
M = int(input())
N = int(input())
for num in range(M,N+1):
    k = 0
    for i in range(1,num+1):
        if num % i == 0:
            k+=1
            if k>2:
                break
    if k==2:
        primes.append(num)
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))