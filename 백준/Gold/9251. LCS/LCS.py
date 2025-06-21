X = input()
Y = input() 
def LCS(X:str,Y:str):
    """X와 Y의 최장 공통 부문자열의 길이 반환"""
    DP_TABLE = [[0] * (len(Y)+1) for _ in range(len(X)+1)] # DP 초기화
    for i in range(len(X)): # A B C D E F (0,1,2,3,4,5)
        for j in range(len(Y)): # G B C D F E (0,1,2,3,4,5)
            if X[i]==Y[j]:
                DP_TABLE[i+1][j+1] = DP_TABLE[i][j] + 1
            else: # x와 y가 같지 않은 경우
                DP_TABLE[i+1][j+1] = max(DP_TABLE[i][j+1], DP_TABLE[i+1][j])
    return DP_TABLE[len(X)][len(Y)]
print(LCS(X,Y))
