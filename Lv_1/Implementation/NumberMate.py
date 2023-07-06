# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter

def solution(X, Y):
    answer = ''

    X = Counter(X)
    Y = Counter(Y)
    
    for i in range(9, -1, -1):
        num = min(X[str(i)], Y[str(i)])
        answer += str(i) * num
    
    if answer == '':
        return '-1'
    
    if answer[0] == '0':
        return '0'
        
    return answer