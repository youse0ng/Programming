a = int(input())
b = int(input())
hundred = b // 100
one = b % 10
ten = (b-hundred*100)//10

print(a*one)
print(a*ten)
print(a*hundred)
print(a*b)