N = int(input())
# (의상 종류 + 1) = -1 하는 이유는 안 입을 가지 수
for _ in range(N): # N번 시행
    n_clothes = int(input())
    kinds_of_clothes = {}
    result = 1
    for _ in range(n_clothes):
        name, kind = input().split()
        if kind in kinds_of_clothes:
            kinds_of_clothes[kind].append(name)
        elif kind not in kinds_of_clothes:
            kinds_of_clothes[kind] = [name]
    for key in kinds_of_clothes:
        result *= (len(kinds_of_clothes[key])+1)
    print(result-1)