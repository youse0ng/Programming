n = int(input())

def tile(num):
    cache = [1 for i in range(num+1)]
    cache[1] = 2

    for i in range(2,num+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[num-1] % 10007

print(tile(n))