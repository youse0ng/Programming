grades = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
summation = 0
scoresum = 0
for _ in range(20):
    _, score, grade = input().split()
    if grade == 'P':
        continue
    summation += float(score) * grades[grade]
    scoresum += float(score)
print(f'{(summation / scoresum):.6f}')