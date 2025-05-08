def fibonacci(int):
    """10번째 피보나치 수열을 구하라."""
    n = int
    if n <= 2 and n != 0:
        return 1
    elif n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
print(fibonacci(n))