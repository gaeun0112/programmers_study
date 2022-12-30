def solution(s):
    answer = []
    temp=[]
    for idx in range(len(s)):
        if s[idx] not in temp:
            answer.append(-1)
            temp.append(s[idx])
        else:
            index = [i for i,ele in enumerate(temp) if ele==s[idx]]
            answer.append(idx-index[-1])
            temp.append(s[idx])
    return answer