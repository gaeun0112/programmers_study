def solution(n):
    three = []
    temp=n
    while True:
        a = temp//3
        b = temp%3
        temp=a
        three.append(b)
        if a==0:
            break
    three = reversed(three)
    answer=0
    up=0
    for i in three:
        answer+=i * (3**up)
        up+=1
    return answer