def solution(numbers):
    answer = 0
    zero_to_ten = [0,1,2,3,4,5,6,7,8,9]
    for num in zero_to_ten:
        if num not in numbers:
            answer += num
    return answer