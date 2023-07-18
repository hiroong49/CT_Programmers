# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    answer = 0
    arr = []

    for i in list(combinations(nums, 3)):
        arr.append(sum(i))
            
    for i in arr:
        chk = 0
        for j in range(2, i):
            if i % j == 0:
                chk += 1
        if chk == 0:
            answer += 1

    return answer