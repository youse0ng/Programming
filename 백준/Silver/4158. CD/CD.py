import sys
while True:
    N, M = map(int,sys.stdin.readline().split())
    sang = {int(sys.stdin.readline()) for _ in range(N)}
    sun = {int(sys.stdin.readline()) for _ in range(M)}

    if N == 0 and M == 0:
        break
    
    print(len(sun.intersection(sang)))