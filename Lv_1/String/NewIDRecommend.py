# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    
    for i in new_id:
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
        
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))
    
    return answer