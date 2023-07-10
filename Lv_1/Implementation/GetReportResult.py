# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    cnt = [0 for _ in id_list]
    warn = [[] for _ in id_list]
    
    report = list(set(report))
    
    for i in report:
        cnt[id_list.index(i.split()[-1])] += 1
        warn[id_list.index(i.split()[0])] += [i.split()[-1]]

    for i in range(len(warn)):
        for j in range(len(warn[i])):
            if cnt[id_list.index(warn[i][j])] >= k:
                answer[i] += 1

    return answer