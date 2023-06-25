# 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    first_letter = ''
    first_cnt = 0
    diff_cnt = 0
    
    for i in s:
        # 첫 글자 분리 및 횟수 카운트
        if first_letter == '':
            first_letter = i
            first_cnt += 1
            continue
            
        # 첫 글자와 같은 글자가 나온 횟수
        if first_letter == i:
            first_cnt += 1
        # 첫 글자와 다른 글자가 나온 횟수
        else:
            diff_cnt += 1
            
        # 두 횟수가 같아지면 문자열 분리하고 초기화 & answer 값 1 증가
        if first_cnt == diff_cnt:
            answer += 1
            first_cnt = 0
            diff_cnt = 0
            first_letter = ''
            
    # 만약 남은 문자열이 있으면 횟수에 포함시키기
    if first_letter:
        answer += 1
            
    return answer