a,b,c,d,e,f = map(int,input().split())
x,y = -999,-999
for i in range(x,1000):
    for j in range(y,1000):
        if (a*i +b*j == c) and (d*i +e*j == f):
            print(i,j)