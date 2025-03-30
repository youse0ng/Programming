N,M = map(int,input().split())
board = []
result = []

for _ in range(N):
    board.append(input())
 
for i in range(N -7): # 8*8 윈도우마다의 시작점 X,Y좌표
    for j in range(M - 7):
        black = 0
        white = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0: # [0][0]이 W,B 두가지 경우를 나눠서 생각함
                    if board[a][b]!='W': # [0][0]이 B일때, 
                        white+=1
                    if board[a][b]!='B': # [0][0]이 W일때,
                        black+=1
                else: #[0][1]
                    if board[a][b]!= 'W':
                        black+=1
                    if board[a][b]!= 'B':
                        white+=1
        result.append(white)
        result.append(black)

print(min(result))