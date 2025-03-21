n = int(input())
data = list(map(int, input().split()))
count = 0

for num in data:
    k = 0
    for i in range(1,num+1):
        if num % i == 0:
            k += 1
    if k == 2:
        count+=1
print(count)