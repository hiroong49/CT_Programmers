# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    dartResult = dartResult.replace('10', 'A')
    cnt = 0
    now = 0
    arr = []
    
    for i in dartResult:
        if i.isdigit():
            cnt = int(i)
        if i == 'A':
            cnt = 10
            
        if i == 'S':
            now = cnt ** 1
            arr.append(now)
        elif i == 'D':
            now = cnt ** 2
            arr.append(now)
        elif i == 'T':
            now = cnt ** 3
            arr.append(now)
        
        if i == '*':
            arr[-1] *= 2
            if len(arr) > 1:
                arr[-2] *= 2
        elif i == '#':
            arr[-1] = -arr[-1]
    
    answer = sum(arr)
    return answer