a_1,a_0 = map(int,input().split())
c = int(input())
n_0 = int(input())

if a_1 * n_0 + a_0 <= c * n_0 and a_1 <= c:
    print(1)
else:
    print(0)