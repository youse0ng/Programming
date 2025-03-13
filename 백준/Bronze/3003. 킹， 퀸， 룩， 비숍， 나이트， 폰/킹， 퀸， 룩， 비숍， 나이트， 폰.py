white = [1,1,2,2,2,8]
missed_white = list(map(int, input().split()))
for i in range(len(white)):
    if white[i] == missed_white[i]:
        print(0,end=' ')
    elif white[i] > missed_white[i]:
        print(white[i]-missed_white[i],end=' ')
    elif white[i] < missed_white[i]:
        print(white[i]-missed_white[i],end=' ')