n = 0
origin_number = int(input())
modified_number = origin_number

while 0 <= origin_number and origin_number < 100:
    if modified_number < 10:
        modified_number = '0' + str(modified_number)
    a, b = str(modified_number)
    summation = int(a) + int(b)
    modified_number = int(b + str(summation)[-1])
    n += 1
    if modified_number == origin_number:
        break
print(n)