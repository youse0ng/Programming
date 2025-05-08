def ispalindrome(string,l,r,count=1):
    if string[l] != string[r]:
        return 0, count
    elif string[l] == string[r] and (l < r):
        return ispalindrome(string,l+1,r-1,count+1)
    elif l >= r:
        return 1, count

N = int(input())
for _ in range(N):
    string = input()
    l,r = 0, len(string)-1
    result, count = ispalindrome(string,l,r)
    print(result,count)