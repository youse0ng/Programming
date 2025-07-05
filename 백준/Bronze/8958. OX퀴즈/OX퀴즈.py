N = int(input())
for _ in range(N):
    x = input()
    score = 0
    result = [0] * len(x)
    for i in range(len(x)):
        if x[i] == 'O':
            score += 1
            result[i] = score
        elif x[i] == 'X':
            score = 0
    print(sum(result))
