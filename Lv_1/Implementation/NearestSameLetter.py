# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    dic = {}
    
    for i in range(len(s)):
        if s[i] in dic:
            answer.append(i - dic[s[i]])
        else:
            answer.append(-1)
        dic[s[i]] = i
            
    return answer
