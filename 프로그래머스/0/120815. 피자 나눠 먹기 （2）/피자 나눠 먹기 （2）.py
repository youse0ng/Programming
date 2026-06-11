def solution(n):
    # 피자 조각을 모두 다 똑같은 개수를 먹어야함
    order_num: int = 1
    while True:
        total_pieces = 6 * order_num
        if total_pieces % n == 0:
            break
        else:
            order_num += 1
    return order_num