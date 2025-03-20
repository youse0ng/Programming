while True:
    factors = []
    N = int(input())
    if N == -1:
        break
    for i in range(1,N):
        if N % i == 0:
            factors.append(i)
    if sum(factors) == N:
        print(f'{N} = ',end='')
        for letter in factors[:-1]:
            print(f'{letter} + ',end='')
        print(f'{factors[-1]}')
    else:
        print(f'{N} is NOT perfect.')