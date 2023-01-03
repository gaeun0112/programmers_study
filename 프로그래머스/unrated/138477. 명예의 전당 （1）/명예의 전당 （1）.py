def solution(k, score):
    answer = []
    top_k = []
    for day in range(len(score)):
        if len(top_k) < k:
            top_k.append(score[day])
        else:
            if min(top_k)<score[day]:
                top_k.append(score[day])
                min_k = min(top_k)
                top_k.remove(min_k)
        answer.append(min(top_k))
    return answer