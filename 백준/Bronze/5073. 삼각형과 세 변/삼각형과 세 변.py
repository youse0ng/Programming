while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0: # 0 0 0 이면 Stop 
        break
    listing = [a,b,c]
    maximum = max(listing)
    listing.remove(maximum)
    if sum(listing) <= maximum: # 삼각형 조건에 안맞는 경우
        print('Invalid')
    elif a==b and a==c and b==c:
        print("Equilateral")    
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")