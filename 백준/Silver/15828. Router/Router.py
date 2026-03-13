from collections import deque
MAX_BUFFER_SIZE = int(input()) # 최대 큐 사이즈
queue = deque() # 패킷을 담을 큐
queue_size = 0 # 현재 큐 사이즈 
while True:
    k = int(input()) # 패킷 정보
    if queue_size >= MAX_BUFFER_SIZE: # 현재 큐에 존재하는 패킷 == 최대 큐사이즈
        if k == -1:
            break
        elif k == 0:
            queue.popleft()
            queue_size -= 1
    else: # 현재 큐 < 최대 큐 사이즈
        if k == -1:
            break
        elif k == 0:
            queue.popleft()
            queue_size -= 1
        else:
            queue.append(k)
            queue_size += 1
if queue_size == 0:
    print('empty')
else:
    for i in queue:
        print(i, end=' ')
    
        