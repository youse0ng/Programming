N, M = map(int,input().split())
result = {}
for idx, _ in enumerate(range(N)):
    pocketmon_name = input()
    result[pocketmon_name] = idx+1
    result[idx+1] = pocketmon_name
for _ in range(M):
    question = input()
    if question.isdigit():
        print(result[int(question)])
    else:
        print(result[question])