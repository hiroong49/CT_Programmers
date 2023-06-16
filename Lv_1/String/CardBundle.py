# 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    c1, c2 = deque(cards1), deque(cards2)
    
    for i in goal:
        if c1 and i == c1[0]:
            c1.popleft()
        elif c2 and i == c2[0]:
            c2.popleft()
        else:
            return 'No'
    
    return 'Yes'

    # 반드시 카드 더미가 다 비워지는 것은 아니다.
    # goal을 완성해도 카드 뭉치에 남아 있을 수 있는 것이 포인트.
        
    #return answer