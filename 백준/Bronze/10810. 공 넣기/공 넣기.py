# 초기화
N, M = map(int,input().split())
# N짜리 리스트가 필요
backet = [0] * N
for _ in range(M):   
    i, j, k = map(int,input().split())
    # I부터 J번까지의 K번 번호가 든 공 삽입
    backet[i-1:j] = [k] * (j - i + 1)
print(" ".join(map(str,backet)))