changes = [25,10,5,1]
N = int(input())
for _ in range(N):
    lists =[]
    money = int(input())
    for cent in changes:
        a = money//cent
        if a > 0:
            lists.append(str(a))
            money = money - a*cent
        elif a == 0:
            lists.append(str(0))
    print(' '.join(lists))