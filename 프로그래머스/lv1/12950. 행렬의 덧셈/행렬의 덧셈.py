def solution(arr1, arr2):
    answer = []
    for idx in range(len(arr1)):
        sum_arr=[]
        for x,y in zip(arr1[idx], arr2[idx]):
            sum_arr.append(x+y)
        answer.append(sum_arr)
    return answer