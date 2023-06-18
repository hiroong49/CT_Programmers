# 명예의 전당 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer = []
    honor = []
    
    for i in range(len(score)):
        if i < k:
            honor.append(score[i])
        else:
            if score[i] > honor[-1]:
                honor.pop()
                honor.append(score[i])
        honor.sort(reverse=True)
        answer.append(honor[-1])
                
    return answer