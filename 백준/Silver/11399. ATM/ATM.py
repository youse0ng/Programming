N = int(input())
a = list(map(int,input().split()))
result = 0
accum = 0
for i in sorted(a):
    accum += i
    result += accum
print(result)
