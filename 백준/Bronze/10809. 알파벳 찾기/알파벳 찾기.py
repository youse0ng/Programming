string = input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    try: 
        print(string.index(i),end=' ')
    except:
        print(-1,end=' ')