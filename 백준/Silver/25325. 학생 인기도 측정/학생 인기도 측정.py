N = int(input())
name = input().split()
result = {i:0 for i in name}
for _ in range(N):
    vote = input().split()
    for v in vote:
        result[v] += 1
sort_result = sorted(result.items(), key= lambda x:x[1],reverse=True)
for name, value in sort_result:
    print(name, value)