A = int(input())
B = int(input())
C = int(input())

degree = A + B + C 

if degree != 180:  
    print('Error')
elif A == B == C:  
    print('Equilateral')
elif A == B or A == C or B == C: 
    print('Isosceles')
else:
    print('Scalene')