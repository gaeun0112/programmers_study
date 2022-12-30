def solution(s):
    answer = ''
    num_list=s.split(" ")
    for i in range(len(num_list)):
        num_list[i]=int(num_list[i])
    answer+= str(min(num_list)) + " "
    answer+= str(max(num_list))
    return answer