N = int(input())
# 출력 부분을 나누어서 풀기 
for i in range(1,N+1): # 별이 하락해서 퍼지는 과정
    print(" "*(N-i) + "*"*(2*i-1)) # 띄어쓰기와 *의 개수 파악이 중요
    
for i in range(N-1,0,-1): # 별이 하락해서 수렴하는 과정
    print(" "*(N-i) + "*"*(i*2-1))
    
    
# 처음 풀었던 방식
#N = int(input())
#for i in range(1,5):
#    j = 5 - i # 띄어쓰기
#    print(' '*j,end='')
#    print('*'*(i*2-1))
#print('*********')
#for i in range(1,5):
#   j = 5 - i # 별 개수
#    print(' '*i,end='')
#    print('*'*(j*2-1))