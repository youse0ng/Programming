N = int(input())
num_list = list(map(int,input().split()))

students = [i for i in range(1,N+1)]
answer = []

for num, student in zip(num_list,students):
    answer.insert(num,str(student))

print(' '.join(answer[::-1]))