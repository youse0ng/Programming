strings = input()
result = set()
for i in range(len(strings)): # 0 1 2 3 4
    for j in range(i, len(strings)): # (0,0), (0,1), (0,2) .. (0,4)
        result.add(strings[i:j+1])
print(len(result))