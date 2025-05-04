N = int(input())
result = list(set([input() for _ in range(N)]))
for word in sorted(result,key=lambda x: (len(x),x)):
    print(word)