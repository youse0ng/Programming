N = int(input())
for _ in range(N):
    strings= input()
    length = len(strings)
    if length ==2:
        if strings == '0!':
            print(1)
        elif strings == '1!':
            print(1)
        elif strings == '!0':
            print(1)
        elif strings == '!1':
            print(0)
            
    elif length == 1:
        print(strings)
        
    elif length >= 3:
        criterion = strings.find('0') if strings.find('0') != -1 else strings.find('1')
        if strings[criterion+1:length].count('!') > 0: # !!0!! 처럼 0 뒤에 !이 하나라도 있을때
            if strings[0:criterion].count('!') % 2 == 0:
                print(1)
            elif strings[0:criterion].count('!')% 2 ==1:
                print(0)
        else: # !!0 처럼 0이 뒤 !이 하나라도 없을때,
            if strings[0:criterion].count('!')%2 == 0: # !!n일경우
                if strings[criterion] == '0':
                    print(0)
                elif strings[criterion] =='1':
                    print(1)
            elif strings[0:criterion].count('!')%2 == 1: # !!!n
                if strings[criterion] == '1':
                    print(0)
                elif strings[criterion] == '0':
                    print(1)