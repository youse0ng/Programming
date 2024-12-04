integers = [int(input()) for _ in range(9)]
max_val = max(integers)
print(max_val)
print(integers.index(max_val) + 1)