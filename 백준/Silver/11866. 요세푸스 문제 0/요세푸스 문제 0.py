N, k = map(int,input().split())
josepus = [i for i in range(1,N+1)]
plus = k
result = []
while len(josepus) > 0:
    i = len(josepus)
    k = k - 1
    k = k % i
    result.append(str(josepus.pop(k)))
    k += plus
print("<", ", ".join(result), ">", sep="")