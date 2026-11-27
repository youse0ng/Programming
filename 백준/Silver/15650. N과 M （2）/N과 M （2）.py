def N_M(N,M):
    result = []
    def backtracking(sequence, visited):
        if len(sequence) == M:
            result.append(sequence.copy())
            return

        for i in range(1, N+1):
            if i in visited:
                continue

            if sequence and sequence[-1] > i:
                continue

            sequence.append(i)
            visited.append(i)
            backtracking(sequence, visited)
            sequence.pop()
            visited.pop()

    backtracking([],[])
    return result
n,m = map(int, input().split())
result = N_M(n,m)
for i in result:
    print(*i)