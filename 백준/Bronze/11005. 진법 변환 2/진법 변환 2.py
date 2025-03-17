N, B = map(int,input().split())
num_to_alpha = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',
 24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}
share = []
while True:
    if B <= 10:
        k = N % B
        if N != 0:
            share.append(str(k))
            N = N // B
        else:
            break
    else:
        k = N % B
        if N != 0:
            if k > 9:
                share.append(str(num_to_alpha[k]))
                N = N // B
            else: 
                share.append(str(k))
                N = N // B
        else:
            break
print(''.join(reversed(share)))