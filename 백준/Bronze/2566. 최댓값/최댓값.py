row, col = 0,0
A = []
for _ in range(9):
    A.append(list(map(int,input().split())))
# 각 행에서 가장 큰 값 추출
maximum = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if maximum < A[i][j]:
            maximum = A[i][j] # 최대값 갱신
            row,col = i,j
print(maximum)
print(row+1,col+1)