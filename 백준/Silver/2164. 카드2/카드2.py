import collections
N = int(input())
a = collections.deque(range(1,N+1))
while len(a) > 1:
    a.popleft() # 첫 번째 꺼냄
    GoBack = a.popleft()
    a.append(GoBack)
print(a[0])