import sys
N, M = map(int,sys.stdin.readline().split())
sorted_sequence = sorted([int(sys.stdin.readline()) for _ in range(N)])

def binary_search(sorted_sequence:list,target):
    """
    sorted_sequence: 정렬된 배열
    target: 찾고자 하는 원소
    """
    start = 0 # 시작 커서
    end = len(sorted_sequence) - 1 # 마지막 커서

    while start <= end:
        mid = (start+end)//2
        if sorted_sequence[mid] == target: # 가장 첫 요소를 고를 수 있도록 설계
            if mid == end:
                break
            end = mid
        elif sorted_sequence[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if sorted_sequence[mid] == target: # 가장 첫 번째 요소를 고를 수 있도록
        return mid
    else:
        return -1


for _ in range(M):
    target = int(sys.stdin.readline())
    print(binary_search(sorted_sequence,target))