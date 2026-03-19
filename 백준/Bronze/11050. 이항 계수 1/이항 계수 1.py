m, n = map(int,input().split())
numerator = 1
denominator_1 = 1
denominator_2 = 1

for i in range(m,0,-1):
    numerator *= i

for j in range(n,0,-1):
    denominator_1 *= j

for k in range(m-n, 0 , -1):
    denominator_2 *= k

print(int(numerator / (denominator_2 * denominator_1)))