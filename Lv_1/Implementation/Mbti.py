# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    mbti = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = [0 for _ in mbti]
    
    for i in range(len(choices)):
        if 4 < choices[i] <= 7:
            score[mbti.index(survey[i][-1])] += choices[i] - 4
        elif 1 <= choices[i] < 4:
            score[mbti.index(survey[i][0])] += 4 - choices[i]

    for i in range(len(score)//2):
        if score[i*2] >= score[i*2+1]:
            answer += mbti[2*i]
        else:
            answer += mbti[2*i+1]
        
    return answer