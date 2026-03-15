from collections import deque
n = int(input())
T = int(input())
queue = deque(input().split())
n_floor = list(map(int,input().split()))

for idx in range(T):
    now_status = 0
    for _ in range(n_floor[idx]):
        x = queue.popleft()
        now_status += 1
        if now_status == n_floor[idx]:
            queue.appendleft(x)
            print(queue[0], end = ' ')
        else:
            queue.append(x)