N = int(input())

for _ in range(N):
    x = input().split()
    for strings in x:
        print(strings[::-1],end=' ')
    print()
