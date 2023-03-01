def solution(n, lost, reserve):
    #전체 학생 수 n
    #체육복 없는 학생 리스트 lost
    #여벌 체육복 있는 학생들의 번호 reserve
    res = [1] * (n+1)
    for x in lost:
        res[x] -= 1
    for x in reserve:
        res[x] += 1
    
    for i in range(1,n+1):
        if res[i] == 0: #빌려야함
            if i-1 >= 1 and res[i-1] == 2:
                res[i-1] -= 1
                res[i] += 1
            elif i+1 <= n and res[i+1] == 2:
                res[i+1] -= 1
                res[i] += 1
                
    
    cnt = 0
    for i in range(1,n+1):
        if res[i] >= 1:
            cnt += 1
    return cnt