def Euclidean_algorithm(a:int, b:int) -> int:
    # 두 수중 가장 큰 값을 비교해서 큰 값을 비교해서 % 연산
    # 나머지가 없다면 나눈 수를 Return (그게 정답값임)
    # 나머지가 있다면 그 나머지 수를 다시 입력하도록 유도
    if a < b:
        if b % a <= 0:
            return a
        else:
            return Euclidean_algorithm(a, b%a)
    elif a > b:
        if a % b <= 0:
            return b
        else:
            return Euclidean_algorithm(b, a%b)
    else:
        return a

a,b = map(int, input().split())
print(int(a * b / Euclidean_algorithm(a,b)))