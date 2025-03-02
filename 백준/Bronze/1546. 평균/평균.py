N = int(input())
grade = list(map(int,input().split()))
max_value = max(grade)
new_grade = [(i/max_value)*100 for i in grade]
print(sum(new_grade)/len(new_grade))