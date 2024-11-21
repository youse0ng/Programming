a,b = map(int,input().split())
c = int(input())
h = c//60 # 시간
m = c%60 # 분

# 경우 1. b+m 분이 60을 안넘어갈 때는 h+1을 해줄 필요가 없다.
# 경우 2. b+m 분이 60을 넘어갈때 h+1을 할 필요가 있다.
# 경우 3. a+h 시간이 24를 일 때는 0으로 바꿔주기
# 경우 4. a+h 시간이 24가 아닐 때, a+h로 표현

if (b+m) >= 60: # b+m이 60을 넘을 때 추가적으로 a+h에 +1이 필요
    if (a+h+1) ==24:# a+h+1이 24이면 0으로
        print(0,(b+m)%60) # a+h+1과 (b+m)%60 해주기
    elif (a+h) > 24:
        print((a+h+1)%24,(b+m)%60)
    else:
        print(a+h+1,(b+m)%60)
else: # b+m이 60을 넘지 않을 때, a+h에 +1을 할 필요가 없음
    if (a+h) == 24: # (a+h가 24이면 0으로 변환)
        print(0,(b+m)%60)
    elif (a+h) > 24:
        print((a+h)%24,(b+m)%60)
    else:
        print(a+h,b+m)
    