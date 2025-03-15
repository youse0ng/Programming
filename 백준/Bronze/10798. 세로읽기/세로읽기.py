a =[]
for _ in range(5):
    a.append([i for i in input()])

maximum = 0
for i in range(len(a)):
    if maximum < len(a[i]):
        maximum = len(a[i])

for i in range(len(a)):        
    needed_space = maximum - len(a[i])
    for _ in range(needed_space):
        a[i].append('')

for j in range(maximum):
    for i in range(len(a)):
        print(a[i][j],end='')