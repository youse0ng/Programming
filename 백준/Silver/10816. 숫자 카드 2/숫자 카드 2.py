N = int(input())
own_cards = list(map(int,input().split()))
M = int(input())
question_card = list(map(int,input().split()))
result = {}

for i in own_cards:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for j in question_card:
    if j in result.keys():
        print(result[j], end=' ')
    else:
        print(0,end=' ')