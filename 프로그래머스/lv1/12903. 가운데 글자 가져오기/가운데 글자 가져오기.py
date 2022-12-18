def solution(s):
    answer = ''
    middle = len(s)//2
    if len(s)%2 != 0:
        answer += s[middle]
    else:
        answer += s[middle-1]
        answer += s[middle]
    return answer