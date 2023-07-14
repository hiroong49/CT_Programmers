# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    
    for i in s:
        if i.isupper() and ord(i)+n > 90 or i.islower() and ord(i)+n > 122:
            answer += chr(ord(i) + n - 26)
        elif ord(i)+n < 65:
            answer += chr(ord(i))
        else:
            answer += chr(ord(i)+n)
            
    return answer