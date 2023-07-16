# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    ppl = len(stages)
    ratio = []
    
    for i in range(1, N+1):
        if i in stages:
            ratio.append((i, stages.count(i) / ppl))
            ppl -= stages.count(i)
            
        else:
            ratio.append((i, 0))
        
    ratio = sorted(ratio, key=lambda x:x[1], reverse=True)
    
    for i in ratio:
        answer.append(i[0])
    
    return answer