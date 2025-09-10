N = int(input())

students = list(map(int,input().split()))
stack = []

now_turn = 1
for student in students:
    # 대기열 한명 스택으로
    stack.append(student)
    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn += 1
if stack:
    print("Sad")
else:
    print("Nice")