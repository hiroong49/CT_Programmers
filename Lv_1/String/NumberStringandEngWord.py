# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0
    num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    for i in num:
        s = s.replace(i, str(num[i]))
    
    answer = int(s)
    return answer