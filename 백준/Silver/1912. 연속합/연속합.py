# 최대구간합
def max_interval(a:list):
    S = [None] * len(a) # DP 테이블
    S[0] = a[0]
    for i in range(1,len(a)):
        S[i] = max(S[i-1]+a[i],a[i])

    return max(S)
n = int(input())
a = list(map(int,input().split()))

print(max_interval(a))