def solution(n):
    answer = 0
    num_list=[]
    for i in str(n):
        num_list.append(int(i))
    num_list = sorted(num_list, reverse=True)
    return int(''.join(str(s) for s in num_list))