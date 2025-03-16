A = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())
for _ in range(N):
    y,x = map(int,input().split())
    
    for row in range(x,x+10):
        for col in range(y,y+10):
            A[row][col] = 1
            
result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += A[k].count(1)  # 1 개수만 세어준다

print(result)