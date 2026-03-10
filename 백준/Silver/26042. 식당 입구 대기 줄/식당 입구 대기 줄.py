import sys
from collections import deque

input = sys.stdin.readline

waiting = deque()
maximum = 0
candidates = []

n = int(input())

for _ in range(n):
    info = list(map(int, input().split()))

    if info[0] == 1:
        waiting.append(info[1])

        if len(waiting) > maximum:
            maximum = len(waiting)
            candidates = [waiting[-1]]

        elif len(waiting) == maximum:
            candidates.append(waiting[-1])

    elif info[0] == 2 and waiting:
        waiting.popleft()

print(maximum, min(candidates))