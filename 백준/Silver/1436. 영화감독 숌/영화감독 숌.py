# 666 1666 2666 3666 4666 5666 
# 6660 6661 6662 6663 6664 6665 6666 6667 6668 6669 
# 7666 8666 9666 10666 11666 12666 13666 14666 15666 !16660! 16661 16662 16663 16664
# 규칙을 찾기 너무 힘듦...
# 차라리 666,1666,10666,... 등 최소 6이 3개들어간 모든 Case들에 대해서 N번째를 찾으면될거같다는 생각이 듦.
# 모든 Case 666을 구하기
# N번째인거 구하기
N = int(input())
start = 666
end = 10000000
cases = []
for i in range(start,end):
    if '666' in str(i):
        cases.append(i)
print(cases[N-1])