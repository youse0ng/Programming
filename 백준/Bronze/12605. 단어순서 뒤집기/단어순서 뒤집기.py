N = int(input())
case_list = []
for _ in range(N):
    case_list.append(input().split(' '))

for idx, case in enumerate(case_list):
    print(f'Case #{idx+1}: ', end='')
    for i in range(len(case)-1, -1, -1):
        print(case[i], end=' ')
    print()