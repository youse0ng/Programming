n_operands = int(input())
post_notation = input()
operands_only = {i:0 for i in post_notation if i.isalpha()}
stack = []
result = 0
for key in operands_only:
    operands_only[key] = int(input())
    
for string in post_notation:
    if string.isalpha():
        stack.append(operands_only[string])
    
    elif not string.isalpha() and string == '*':
        operand_1 = stack.pop()
        operand_2 = stack.pop()
        result = operand_2 * operand_1
        stack.append(result)
    elif not string.isalpha() and string == '/':
        operand_1 = stack.pop()
        operand_2 = stack.pop()
        result = operand_2 / operand_1
        stack.append(result)
        
    elif not string.isalpha() and string == '+':
        operand_1 = stack.pop()
        operand_2 = stack.pop()
        result = operand_2 + operand_1
        stack.append(result)
        
    elif not string.isalpha() and string == '-':
        operand_1 = stack.pop()
        operand_2 = stack.pop()
        result = operand_2 - operand_1
        stack.append(result)
        
print(f"{result:.2f}")