i = 1
n = int(input())
while n > i:
    n -= i
    i += 1
    
if i % 2 == 0:
    a = n
    b = i - n +1
elif i % 2 == 1:
    a = i - n + 1
    b = n
print(f'{a}/{b}')