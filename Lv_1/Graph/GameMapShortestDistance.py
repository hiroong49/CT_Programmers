# 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
    bfsQueue = deque([])
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    def bfs():
        while bfsQueue:
            curLoc = bfsQueue.popleft()
            curY = curLoc[0]
            curX = curLoc[1]
            for i in range(4):
                ny = curY + dy[i]
                nx = curX + dx[i]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if maps[ny][nx] == 0:
                    continue
                if visited[ny][nx] != 0:
                    continue
                visited[ny][nx] = visited[curY][curX] + 1
                bfsQueue.append((ny, nx))
    
    visited[0][0] += 1
    bfsQueue.append((0, 0))
    bfs()
    
    if visited[n-1][m-1] == 0:
        answer = -1
    else:
        answer = visited[n-1][m-1]
            
    return answer