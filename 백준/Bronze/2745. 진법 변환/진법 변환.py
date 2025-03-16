word, number = input().split()
word_to_number = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,
                  'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,
                  'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}
word = [i for i in word]
number = int(number)

result = 0
for idx,alphabet in enumerate(reversed(word)):
    if alphabet.isalpha():
        result += number**(idx) * word_to_number[alphabet]
    else:
        result += number**(idx) * int(alphabet)
print(result)