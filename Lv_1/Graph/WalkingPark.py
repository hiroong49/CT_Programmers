# 공원 산책
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []
    
    h = len(park)
    w = len(park[0])
    
    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                curY = i
                curX = j
                break
    
    # 산책하기
    for r in range(len(routes)):
        op, n = routes[r].split()
        ny = curY
        nx = curX
        
        for i in range(int(n)):
            # 다음으로 이동할 곳이 map 안에 있어야 하고(1번 조건), 장애물이 있는 길이면 안 된다(2번 조건)
            if op == 'N' and ny != 0 and park[ny-1][nx] != 'X':
                ny -= 1
                # 만약 거리 n만큼 갔다면, 현재 위치를 바꿔줌
                if i == int(n)-1:
                    curY = ny
            elif op == 'E' and nx != w-1 and park[ny][nx+1] != 'X':
                nx += 1
                if i == int(n)-1:
                    curX = nx
            elif op == 'S' and ny != h-1 and park[ny+1][nx] != 'X': 
                ny += 1
                if i == int(n)-1:
                    curY = ny
            elif op == 'W' and nx != 0 and park[ny][nx-1] != 'X':
                nx -= 1
                if i == int(n)-1:
                    curX = nx
            
                
    answer.append(curY) 
    answer.append(curX)
    return answer