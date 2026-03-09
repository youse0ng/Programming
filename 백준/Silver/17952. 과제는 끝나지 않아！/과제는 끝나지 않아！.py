import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0 

for _ in range(N):
    assignments = list(map(int, input().split()))
    
    if assignments[0] == 1:
        stack.append((assignments[1], assignments[2]))
    
    if stack:
        score, time = stack.pop()
        time -= 1
        if time == 0:
            result += score
        else:
            stack.append((score, time))

print(result)