# 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        point = 0
        for j in i:
            if j in name:
                point += yearning[name.index(j)]
        answer.append(point)
    
    return answer