def solution(answers):
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    n = len(answers)
    cnt = [0] * 3
    
    for i in range(n):
        ans = answers[i]
        if a[i%len(a)] == ans:
            cnt[0] += 1
        if b[i%len(b)] == ans:
            cnt[1] += 1
        if c[i%len(c)] == ans:
            cnt[2] += 1
        
        
    
    max_cnt = max(cnt)
    res = []
    for i in range(3):
        if cnt[i] == max_cnt:
            res.append(i + 1)
    return res    
            
