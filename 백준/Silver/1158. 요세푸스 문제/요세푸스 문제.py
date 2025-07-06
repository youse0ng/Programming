from collections import deque
N, k = map(int,input().split())
queue = deque([i for i in range(1,N+1)])
result = []
while len(queue) > 0:
    for _ in range(k-1):
        popout = queue.popleft()
        queue.append(popout)
    result.append(str(queue.popleft()))
print(f"<{', '.join(result)}>")
