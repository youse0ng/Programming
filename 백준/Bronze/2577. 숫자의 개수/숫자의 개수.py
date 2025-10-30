from collections import Counter
A,B,C = int(input()), int(input()), int(input())
check = Counter(str(A*B*C))
check.keys()
for i in range(10):
    if str(i) in check.keys():
        print(check[str(i)])
    else:
        print(0)