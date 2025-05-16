N = int(input())
result = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        result.append(command[1])
    elif command[0] == 'top':
        if len(result) <= 0:
            print(-1)
        else:
            print(result[-1])
    elif command[0] == 'size':
        print(len(result))
    elif command[0] == 'empty':
        if len(result) <=0:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if len(result) <= 0:
            print(-1)
        else:
            print(result.pop())