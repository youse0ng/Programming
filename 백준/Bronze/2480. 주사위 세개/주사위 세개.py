# 같은 눈 3개 나옴 - 10000 + (같은 눈) * 1000
# 같은 눈 2개만 - 1000 + 같은 눈 *100
# 모두 다른 눈 - 그중 가장 큰 눈 *100

a,b,c = map(int, input().split())
max = a
if a==b==c: # 같은 눈 3개가 나올 때
    print(10000 + (a)*1000)
elif a==b:
    print(1000 + (a)*100)
elif a==c: 
    print(1000 + (a)*100)
elif b==c: # a랑 b가 같거나 a==c가 같거나 b==c가 같을 떄
    print(1000 + (b)*100)
else:
    for value in [a,b,c]:
       if max < value:
           max = value
    print(max*100)
