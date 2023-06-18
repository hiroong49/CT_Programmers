# 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    paint = 0
    
    for i in section:
        if i > paint:
            answer += 1
            paint = i + m - 1

    return answer