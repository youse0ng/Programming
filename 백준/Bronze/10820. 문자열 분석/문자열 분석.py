while True:
    try:
        lower = 0
        upper = 0
        num = 0
        space = 0
        a = input()
        for string in a:
            if string.isdigit():
                num += 1
            elif string.isupper():
                upper += 1
            elif string.islower():
                lower += 1
            elif string.isspace():
                space += 1
        print(lower,upper,num,space)
    except EOFError:
        break