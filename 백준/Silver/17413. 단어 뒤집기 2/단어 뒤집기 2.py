text = input() + ' '
stack = []
result = ""
mask = 0

for string in text:
    if string == '<':
        mask = 1
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(string)
    
    if string == '>':
        mask = 0
        for _ in range(len(stack)):
            result += stack.pop(0)
    
    if string == ' ' and mask == 0:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
print(result)