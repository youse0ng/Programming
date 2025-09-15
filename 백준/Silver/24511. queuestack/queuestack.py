import sys
from collections import deque
N = int(input()) # 자료구조 개수
is_stack = list(map(int,input().split())) # 스택이면 1 큐이면 0
element_list = list(map(int,input().split())) # 각 자료구조 원소
M = int(input()) # 입력될 시퀀스의 길이
input_list = list(map(int,input().split())) # 입력될 입력값
queue = deque()

for i in range(N):
    if is_stack[i] == 0: # 큐라면, 해당 원소를 pop
        queue.appendleft(element_list[i])
if queue:
    for k in range(M):
        print(queue.popleft(), end=' ')
        queue.append(input_list[k])
else:
    print(*input_list)