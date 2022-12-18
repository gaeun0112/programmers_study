def solution(a, b):
    answer = 0
    if a==b:
        answer = a
    else:
        for num in range(min(a,b), max(a,b)+1):
            answer+=num
    return answer