t = int(input())

context_lists = [input() for _ in range(t)]
for text in context_lists:
    print(text[0],end='')
    print(text[-1])