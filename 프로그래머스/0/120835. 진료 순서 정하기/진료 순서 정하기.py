def solution(emergency:list):
    answer: list = []
    sorted_emergency: list = sorted(emergency, reverse=True)
    
    for idx in range(len(emergency)):
        i = 1
        for jdx in range(len(emergency)):
            if emergency[idx] == sorted_emergency[jdx]:
                answer.append(i)
                break
            else:
                i += 1
    return answer