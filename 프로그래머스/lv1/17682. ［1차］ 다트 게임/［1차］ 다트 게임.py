def solution(dartResult):
    answer_list=[]
    index=0
    dic={'S':1, 'D':2, 'T':3}
    for i in range(len(dartResult)):
        if dartResult[i].isdigit()==True:
            if dartResult[i]=='0' and dartResult[i-1]=='1':
                answer_list[index-1]=10
            else:
                answer_list.append(int(dartResult[i]))
                index+=1
        elif dartResult[i].isalpha()==True:
            answer_list[index-1] = answer_list[index-1]**dic[dartResult[i]]
        elif dartResult[i]=='*':
            if index==1:
                answer_list[index-1]*=2
            else:
                answer_list[index-1]*=2
                answer_list[index-2]*=2
        elif dartResult[i]=='#':
            answer_list[index-1]*=-1
    answer=sum(answer_list)
    return answer