N = int(input())
for _ in range(N):
    result = []
    string = input()
    if len(string)%2 == 1: # 문자 길이가 홀수이면 NO "((())"와 같이 이루어져 홀수면 무조건 NO이다.
        print('NO')
    else:
        for ps in string:
            if len(result) == 0 or ps == "(": # [] 비어있고, ps="(" 이면 추가
                result.append(ps)
            elif ps == ")" and result[-1] == "(":
                result.pop()            
        if len(result) == 0:
            print("YES")
        else:
            print('NO')