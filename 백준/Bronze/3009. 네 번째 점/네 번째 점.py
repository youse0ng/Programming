X,Y = [],[]
for _ in range(3):
    a,b = map(int,input().split())
    X.append(a)
    Y.append(b)

factor_x = set(X)
factor_y = set(Y)
for i in factor_x:
    if X.count(i) == 2:
        continue
    elif X.count(i) ==1:
        print(f'{i}',end=' ')

for j in factor_y:
    if Y.count(j) == 2: 
        continue
    elif Y.count(j) == 1:
        print(f'{j}',end='')
    