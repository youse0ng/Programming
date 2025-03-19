initial=1
k=1
n = int(input())
while True:
    if n <= initial:
        break
    initial = initial + (6*k)
    k += 1
print(k) 