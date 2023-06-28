# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    
    d.sort()
    
    while budget > 0 and d:
        if budget >= d[0]:
            budget -= d[0]
            d.remove(d[0])
            answer += 1
        else:
            break
            
    return answer