def solution(arr):
    answer = []
    arr.append(-1)
    for idx in range(len(arr)):
        if idx<len(arr)-1:
            if arr[idx] != arr[idx+1]:
                answer.append(arr[idx])
    return answer