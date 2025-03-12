A,B = input().split()
A,B = int(A[::-1]),int(B[::-1])
print(B) if A < B else print(A)