def solution(n, arr1, arr2):
    arrs = [arr1, arr2]
    for arr in arrs:
        for idx in range(len(arr)):
            num=[]
            temp=arr[idx]
            while True:
                a = temp//2
                b = temp%2
                temp=a
                num.append(b)
                if len(num)==n:
                    break
            arr[idx]=num[::-1]
    answer = []
    for i in range(n):
        temp=""
        for j in range(n):
            if arrs[0][i][j]==0 and arrs[1][i][j]==0:
                temp+=" "
            else:
                temp+="#"
        answer.append(temp)
    return answer