#문제 이해
# d : 부서별로 신청한 금액이 들어있는 배열, 길이는 1 이상 100 이하.
# budget : 예산 금액
# answer : 물품을 지원해줄 수 있는 부서의 수의 최댓값

def solution(d, budget):
    answer = 0
    sum_d=0
    d = sorted(d)
    for i in d:
        sum_d+=i
        if sum_d<=budget:
            answer+=1
        else:
            break
    return answer