def solution(absolutes, signs):
    answer = 123456789
    real_num=[]
    for idx in range(len(absolutes)):
        if signs[idx] == True:
            real_num.append(absolutes[idx])
        else:
            real_num.append(-absolutes[idx])
    answer = sum(real_num)
    return answer