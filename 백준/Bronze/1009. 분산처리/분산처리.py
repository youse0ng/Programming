N = int(input())

for _ in range(N):
    cycle = []
    a,b = map(int, input().split())
    temp = 1
    for _ in range(4):
        temp = (temp * a)%10
        cycle.append(temp)
    print(cycle[(b-1) % len(cycle)] or 10)