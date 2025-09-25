def solution(nums):
    answer = 0
    pocket = {}
    check = set()
    for i in nums:
        pocket[i] = pocket.get(i, 0) + 1
        
    for no,num in pocket.items():
        if no not in check and answer < len(nums)/2:
            answer += 1
    return answer