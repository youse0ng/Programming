import sys

input = sys.stdin.readline

N = int(input())
pillar_list = [int(input()) for _ in range(N)]

standard_point = pillar_list[-1]
answer = 1  # 마지막 막대기는 보이므로

for i in range(N - 2, -1, -1):
    if pillar_list[i] > standard_point:
        answer += 1
        standard_point = pillar_list[i]

print(answer)
