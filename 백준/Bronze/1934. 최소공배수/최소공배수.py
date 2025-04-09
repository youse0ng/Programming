def gcd(a,b):
    if b%a == 0:
       return a 
    return gcd(b%a,a)
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    gcd_num = gcd(a,b)
    print(gcd_num * a//gcd_num * b//gcd_num)
