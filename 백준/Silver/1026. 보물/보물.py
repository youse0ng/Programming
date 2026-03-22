N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A,reverse=True)
B = sorted(B)
result = 0

for idx in range(N):
    result += A[idx] * B[idx]
print(result)