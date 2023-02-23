def solution(answers):
    
    a = []
    n = len(answers)
    cnt = 1
    for i in range(n):
        a.append(cnt)
        cnt += 1
        if cnt == 6:
            cnt = 1  
    #1번 학생 답안지 완성
    b = [2,1,2,3,2,4,2,5]
    while len(b) < n:
        b = b * 2
    b = b[:n]   
    #2번 학생 답안지 완성
    c = [3,3,1,1,2,2,4,4,5,5]
    while len(c) < n:
        c = c * 2
    c = c[:n]
    #3번 학생 답안지 완성
    
    cnt = [0] * 3
    for i in range(n):
        if a[i] == answers[i]:
            cnt[0] += 1
        if b[i] == answers[i]:
            cnt[1] += 1
        if c[i] == answers[i]:
            cnt[2] += 1
    
    max_cnt = max(cnt)
    res = []
    for i in range(3):
        if cnt[i] == max_cnt:
            res.append(i + 1)
    return res    
            
