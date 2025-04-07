N = int(input())
stack = []
for _ in range(N):
    integer = int(input())
    if integer != 0:
        stack.append(integer)
    elif integer == 0 and (len(stack) > 0):
        stack.pop()
print(sum(stack))