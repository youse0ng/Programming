from collections import deque

N = int(input())
queue = deque()
for idx in range(N,0,-1):
    queue.append(idx)

for _ in range(N-1):
    print(queue.pop(), end = ' ')
    last = queue.pop()
    queue.appendleft(last)
print(queue[-1])
