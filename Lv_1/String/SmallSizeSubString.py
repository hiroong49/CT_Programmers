# 크기가 작은 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    arr = []
    
    for i in range(len(t)):
        arr.append(t[i:len(p)+i])

    for i in arr:
        if len(i) < len(p):
            continue
        if p >= i:
            answer += 1
        
    # 코드 개선
    # range를 (len(t) - len(p) + 1)로 바꾸면 문자열 p 길이로 일정하게 나눌 수 있음
    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer