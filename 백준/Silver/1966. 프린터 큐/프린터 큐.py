from collections import deque
N = int(input())
for _ in range(N):
    idx = 0
    n_docs, m = map(int,input().split())
    queue = deque(map(int,input().split()))
    maximum = max(queue)
    if n_docs == 1:
        print(1)
        continue
    while queue:
        if queue[0] >= maximum:
            queue.popleft()
            if queue: 
                maximum = max(queue)
            idx +=1
            if m == 0:
                break
            m -= 1
        else: 
            x = queue.popleft()
            queue.append(x)
            m -= 1
        if m < 0:
            m = len(queue) - 1
    print(idx)
        