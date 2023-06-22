# 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    
    for i in s:
        cnt = index
        word = ord(i)
        while cnt != 0:
            word += 1
            if word > ord('z'):
                word -= 26
            if chr(word) in skip:
                continue
            cnt -= 1
        
        answer += chr(word)
        
    return answer