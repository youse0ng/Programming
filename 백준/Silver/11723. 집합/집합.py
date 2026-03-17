import sys
input = sys.stdin.readline

S = set()
N = int(input())
for _ in range(N):
    process = input().split()
    if process[0] == 'add' and process[1] not in S: # 없으면 추가
        S.add(process[1])
    elif process[0] == 'remove' and process[1] in S: # 있으면 제거
        S.remove(process[1])
    elif process[0] == 'check':
        if process[1] in S:
            print('1')
        else:
            print('0')
    elif process[0] == 'toggle':
        if process[1] not in S:
            S.add(process[1])
        elif process[1] in S:
            S.remove(process[1])
    elif process[0] == 'all':
        S = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif process[0] == 'empty':
        S.clear()