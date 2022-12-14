def solution(x):
    answer = True
    num_list = []
    for i in str(x):
        num_list.append(int(i))
    if x%sum(num_list)==0:
        answer=True
    else:
        answer=False
    return answer