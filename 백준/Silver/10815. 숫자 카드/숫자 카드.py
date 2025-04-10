N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))

dic = {}
for i in b:
    dic[i] = 0

for i in a:
    if i in dic:
        dic[i]=1
        
for d in dic:
    print(dic[d], end=' ')