dials = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
word = input().upper()
total = 0
for alphabet in word:
    for dial in dials:
        if alphabet in dial:
            total += dials[dial]
print(total)