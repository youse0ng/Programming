import sys

input = sys.stdin.readline

N = int(input())
coordinates = []
answer = 0

A, B = map(int, input().split())

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# 탐색 속도를 위해 set으로 변환
coord_set = set(coordinates)

for x, y in coord_set:
    if (x + A, y) in coord_set and (x, y + B) in coord_set and (x + A, y + B) in coord_set:
        answer += 1

print(answer)
