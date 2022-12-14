def solution(x, n):
    answer = []
    inner = x
    while n!=0:   
        answer.append(inner)
        inner +=x
        n -=1
    return answer