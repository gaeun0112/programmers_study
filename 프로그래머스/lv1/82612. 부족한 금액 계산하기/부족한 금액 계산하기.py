def solution(price, money, count):
    answer = -1
    need_money=0
    for i in range(1, count+1):
        need_money += i * price
    if need_money>money:
        answer = need_money-money
    else:
        answer=0
    return answer