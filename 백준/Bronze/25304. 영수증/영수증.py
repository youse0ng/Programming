total_price = int(input())
kind = int(input())
sum = 0
for _ in range(kind):
    a,b = map(int,input().split())
    sum += (a*b)
if sum == total_price:
    print('Yes')
else:
    print('No')