# 기사단원의 무기
# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = 0
    arr = []
    
    # 약수 구하기
    for i in range(1, number+1):
        yak = 0
        # 제곱근 사용
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                yak += 2
                # 제곱수면 약수 개수 하나 감소
                if i / j == j:
                    yak -= 1
                
        arr.append(yak)
    
    for i in arr:
        if i > limit:
            answer += power
        else: answer += i
        
    return answer