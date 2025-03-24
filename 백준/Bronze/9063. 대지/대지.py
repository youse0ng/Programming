N = int(input())
X,Y = [],[]
if N == 1:
    print(0)
else:
    for _ in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    x_min,y_min = min(X),min(Y)
    x_max,y_max = max(X),max(Y)
    print((x_max-x_min)*(y_max-y_min))