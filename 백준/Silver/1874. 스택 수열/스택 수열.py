import sys

N = int(sys.stdin.readline())
big = 1
check_list = []
answer_list = []

for _ in range(N):
    number = int(sys.stdin.readline())
    if number >= big:
        for idx in range(big, number+1):
            check_list.append(idx)
            answer_list.append("+")
        big = number + 1
        if number == check_list[-1]:
            check_list.pop()
            answer_list.append("-")
    elif number < big:
        while True:
            try:
                pop_number = check_list.pop()
            except:
                print("NO")
                sys.exit()
            answer_list.append("-")
            if pop_number == number:
                break

for char in answer_list:
    print(char)
