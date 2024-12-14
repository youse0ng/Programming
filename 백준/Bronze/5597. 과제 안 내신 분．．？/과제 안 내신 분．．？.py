check_list = {i for i in range(1,31,1)}
attend_list = {int(input()) for _ in range(28)}
for num in sorted(check_list - attend_list):
    print(num)