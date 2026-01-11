from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()
for _ in range(N):
    order = input()
    order = order.split()
    if order[0] == "push_back":
        queue.append(order[1])
    if order[0] == "push_front":
        queue.appendleft(order[1])
    if order[0] == "front":
        if queue.__len__() == 0:
            print("-1")
        else:
            print(queue[0])
    if order[0] == "size":
        print(queue.__len__())
    if order[0] == "pop_front":
        try:
            print(queue.popleft())
        except:
            print(-1)
    if order[0] == "pop_back":
        try:
            print(queue.pop())
        except:
            print(-1)
    if order[0] == "empty":
        if queue.__len__() == 0:
            print("1")
        else:
            print("0")
    if order[0] == "back":
        if queue.__len__() == 0:
            print("-1")
        else:
            print(queue[-1])