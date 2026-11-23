ans = list()
def hanoi(N, start, mid, end):
    global ans
    if N == 1:
        ans.append((start, end))
    else:
        hanoi(N-1, start, end, mid) # N-1개의 판들을 중간으로 옮김
        ans.append((start, end)) # Move(N번째 판: start -> end)
        hanoi(N-1, mid, start, end) # N-1개의 판들을 다시 끝으로 옮김

n = int(input())
hanoi(n,1,2,3)
print(len(ans))
for i,j in ans:
    print(i,j)