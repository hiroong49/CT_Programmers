# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # words 배열 안에 타겟 단어가 없으면 변환 불가
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        word, index = queue.popleft()
        visited = [0 for _ in range(len(words))] # visited 매번 초기화되어야 함
        if word == target:
            break
        
        # 단어가 몇 개 같은지 확인
        for i in range(len(words)):
            for j in range(len(words[i])):
                if word[j] == words[i][j]:
                    visited[i] += 1
                
        # visited 개수가 타겟 단어와 하나 다르면 변환
        for i in range(len(visited)):
            if visited[i] == len(target) - 1:
                queue.append((words[i], index+1))

    answer = index
    return answer