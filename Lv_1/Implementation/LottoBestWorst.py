# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    cnt, err = 0, 0
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
        
        if i == 0:
            err += 1
    
    high = 7 - (cnt + err)
    low = 7 - cnt
    
    if high > 6:
        high -= 1
    if low > 6:
        low -= 1
        
    answer.append(high)
    answer.append(low)
    
    return answer