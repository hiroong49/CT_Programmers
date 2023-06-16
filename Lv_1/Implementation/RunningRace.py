# 달리기 경주
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    answer = []
    
    # 리스트를 딕셔너리로 변환
    player = {string: i for i, string in enumerate(players)}
    
    for i in callings:
        # 불린 이름은 인덱스를 하나 땡기고, 앞에 있던 이름은 한 칸 뒤로
        pre, name = player[i] - 1, player[i]
        # 불린 이름과 앞에 있던 선수 바꾸기
        players[pre], players[name] = players[name], players[pre]
        # 딕셔너리도 변경해주기
        player[players[pre]], player[players[name]] = player[players[pre]] - 1, player[players[pre]]
    
    answer = players
    return answer