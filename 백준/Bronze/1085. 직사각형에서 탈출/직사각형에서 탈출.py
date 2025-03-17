x,y,w,h = map(int,input().split())
minimum = []
minimum.append(w-x)
minimum.append(x)
minimum.append(h-y)
minimum.append(y)
print(min(minimum))