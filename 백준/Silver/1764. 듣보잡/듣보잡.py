N, M = map(int,input().split())
unheard = set(input() for _ in range(N)) 
unseen = set(input() for _ in range(M))

print(len(unheard&(unseen)))
for i in sorted(unheard&(unseen)):
    print(i)