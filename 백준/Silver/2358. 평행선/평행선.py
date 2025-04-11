from collections import defaultdict
x_dict = defaultdict(list)
y_dict = defaultdict(list)

N = int(input())
answer = 0
for _ in range(N):
    a,b = map(int,input().split())
    x_dict[a].append(b)
    y_dict[b].append(a)

for key in x_dict:
    if len(x_dict[key]) >= 2:
        answer += 1
for key in y_dict:
    if len(y_dict[key]) >= 2:
        answer +=1 
print(answer)