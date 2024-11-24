import sys
n = int(sys.stdin.readline()) # 5
for i in range(1,n+1): # 1,2,3,4,5
    print(' '*(n-i),end='')
    print('*'*i)

    