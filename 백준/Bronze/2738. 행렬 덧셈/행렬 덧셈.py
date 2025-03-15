A=[]
B=[]
N,M = map(int,input().split())
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))
    
result = []
for i in range(len(A)):
    sub_mat = []
    for j in range(len(A[i])):
        sub_mat.append(A[i][j] + B[i][j])
    result.append(sub_mat)

for i in result:
    for j in i:
        print(j,end=' ')
    print()