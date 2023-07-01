# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        s = ''
        bin_num = bin(arr1[i] | arr2[i])[2:].zfill(n)
        
        for j in bin_num:
            if j == '1':
                s += '#'
            else:
                s += ' '
        answer.append(s)
        
    return answer