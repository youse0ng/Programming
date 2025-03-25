N = int(input())
for i in range(1,N):
    summation = i
    for string in str(i):
        summation += int(string)
    if summation == N:
        print(i)
        break
else:
    print(0)