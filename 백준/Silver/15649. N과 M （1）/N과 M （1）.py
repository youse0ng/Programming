def N_M(N, M):
    results = []

    def backtracking(sequence, visited):
        if len(sequence) == M: # 뽑힌 숫자들이 M개일 때,
            results.append(sequence.copy()) # 상태를 저장
            return

        else: # 다 뽑히지 않았다면, 더 뽑아야함
            for i in range(1, N+1):
                if i in visited: # 이미 그 숫자를 이미 뽑았다면, 다시 뽑으면 안됨 (중복 배제 조건)
                    continue
                # 뽑아야 하는 숫자일 때, 뽑고 기록
                sequence.append(i)
                visited.append(i)
                backtracking(sequence, visited) # 재귀 호출을 통해서 현재 상태에 대해 넘겨줌
                sequence.pop() # 끝까지 들어갔다면, 다시 원복
                visited.pop()

    backtracking([],[])
    return results

n, m = map(int,input().split())
for i in N_M(n,m):
    print(*i)