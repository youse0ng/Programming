N = int(input())
stack = []
answer = 0 
for _ in range(N):
    words = input()
    if len(words) % 2 == 1 and len(words)==0: # 길이가 홀수인 것과 입력되지 않은 단어는 좋은 단어가 될 수 없다.
        continue
# stack 안이 비어있으면 그래그래 좋은단어
# stack 안이 비어있지 않으면 그래그래 나쁜단어
    for alphabet in words:
        if not stack: # 스택에 아무것도 없으면,
            stack.append(alphabet)
        elif stack: # 스택에 뭐 있으면,
            if stack[-1] == alphabet: # 스택에 맨위요소와 비교
                stack.pop()
            elif stack[-1] != alphabet:
                stack.append(alphabet)
    if not stack:
        answer += 1
    stack = [] # 스택 초기화
print(answer)