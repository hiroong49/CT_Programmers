# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    bab = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for j in bab:
            # 연속된 같은 발음이 없을 때
            if j*2 not in i:
                # ' '으로 치환
                i = i.replace(j, ' ')
        
        # 공백 제거했을 때 아무것도 없다면 발음 가능
        if i.strip() == '':
            answer += 1
            
    return answer