import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A_LIST = [] # 본인이 좋아하는 메뉴를 먹은 학생 목록
B_LIST = [] # 본인이 좋아하지 않은 메뉴를 먹은 학생 목록
C_LIST = [] # 식사를 못 먹은 학생 목록
queue = deque()

for _ in range(N): # N번 입력 처리
    process = list(map(int, input().split()))
    if process[0] == 1: # 유형 1번이면, 입력을 학생 번호, 좋아하는 메뉴번호
        student_number, favorite_number = process[1], process[2]
        queue.append((student_number, favorite_number))
    elif process[0] == 2: # 유형 2번이면, 식당에서 음식 처리 (나온 메뉴 번호)
        restaurant_menu_number = process[1]
        student_number, favorite_number = queue.popleft()
        if favorite_number == restaurant_menu_number: # 좋아하는 메뉴 번호 == 나온 음식 메뉴
            A_LIST.append(student_number)
        else: # 다른 음식 메뉴가 나온 경우
            B_LIST.append(student_number)

if A_LIST:
    print(*sorted(A_LIST))
else:
    print("None")

if B_LIST:
    print(*sorted(B_LIST))
else:
    print("None")

if queue:
    C_LIST = [student for student, _ in queue]
    print(*sorted(C_LIST))
else:
    print("None")