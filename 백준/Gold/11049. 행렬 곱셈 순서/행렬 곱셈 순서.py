N = int(input())
matrix = []
for _ in range(N): # 연산량 계산 M'과 M''을 계산하기 위한 테이블 
    a,b = map(int,input().split())
    matrix.append(a)
matrix.append(b)

DP_TABLE = [[0]*(N+1) for _ in range(N+1)]# DP 테이블 초기화
for cnt in range(1,N): # 괄호치려는 구간 (1 ~ N-1)
    for start in range(1,N-cnt+1): # 구간의 시작점 (1 ~ N)
        end = start+cnt # 마지막 끝
        DP_TABLE[start][end] = 2**32
        for mid in range(start, end):
            DP_TABLE[start][end] = min(DP_TABLE[start][end],DP_TABLE[start][mid] + DP_TABLE[mid+1][end] + matrix[start-1]*matrix[mid]*matrix[end])
print(DP_TABLE[1][N])