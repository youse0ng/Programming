N = int(input())
for _ in range(N):
    word = input()
    for i in range(0,len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            N = N-1
            break
print(N)