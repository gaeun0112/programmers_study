def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        num_of_div=0
        for i in range(1, num+1):
            if num%i==0:
                num_of_div += 1
        if num_of_div%2==0:
            answer+=num
        else:
            answer-=num
    return answer