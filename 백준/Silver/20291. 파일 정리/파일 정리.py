N = int(input())
file_dict = {}
for _ in range(N):
    file = input()
    extension = file.split('.')[1]
    if extension in file_dict:
        file_dict[extension] += 1
    elif extension not in file_dict:
        file_dict[extension] = 1

for key in sorted(file_dict):
    print(key, end =' ')
    print(file_dict[key])
