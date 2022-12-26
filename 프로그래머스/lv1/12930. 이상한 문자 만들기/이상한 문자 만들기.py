def solution(s):
    s_list = s.split(" ")
    for idx in range(len(s_list)):
        if s_list[idx]!="":
            word=""
            for i in range(len(s_list[idx])):
                if (i+1)%2 != 0:
                    word+=s_list[idx][i].upper()
                else:
                    word+=s_list[idx][i].lower()
            s_list[idx] = word
    answer = " ".join(s_list)
    return answer