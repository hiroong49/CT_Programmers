# 삼총사
# https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations

def solution(number):
    answer = 0
    
    for i in list(combinations(number, 3)):
        if sum(i) == 0:
            answer += 1
    
    return answer