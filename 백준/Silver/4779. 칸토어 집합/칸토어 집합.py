def contour(N):
    if N <= 0:
        return "-"
    else:
        return contour(N-1) + " " * (3**(N-1)) + contour(N-1)
                                                         
while True:
    try:
        a = int(input())
        print(contour(a))
    except:
        break