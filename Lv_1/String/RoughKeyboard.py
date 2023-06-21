# 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    least_click = {}
    
    # 키맵 알파벳 최소 누르는 횟수
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in least_click:
                least_click[keymap[i][j]] = j + 1
            # 더 적은 방법이 있으면 교체
            elif least_click[keymap[i][j]] > j + 1:
                least_click[keymap[i][j]] = j + 1

    # 타겟 알파벳 횟수 계산      
    for i in targets:
        cnt = 0
        for j in i:
            # 딕셔너리 key에 없으면 변환 불가
            if j not in least_click.keys():
                cnt = -1
                break
            else:
                cnt += least_click[j]
        answer.append(cnt)
                
    return answer