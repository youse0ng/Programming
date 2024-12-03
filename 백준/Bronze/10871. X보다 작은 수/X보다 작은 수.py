N, X = map(int,input().split())
integers = list(map(int,input().split()))
for i in [i for i in integers if i < X]:
    print(i,end=' ')