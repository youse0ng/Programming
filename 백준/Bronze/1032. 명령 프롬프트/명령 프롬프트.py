N = int(input())
if N == 1:
    print(input())
elif N > 1:
    temp = list(input())
    for _ in range(N-1):
        compared_string = list(input())
        for i in range(len(compared_string)):
            if temp[i] == compared_string[i]:
                pass
            else:
                temp[i] = '?'
    print(''.join(temp))