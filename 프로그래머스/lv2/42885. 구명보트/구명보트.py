from collections import deque
def solution(people, limit):
    #최대 2명
    #최대한 적게 사용하여.
    data = people
    n = len(data)
    data.sort()
    cnt = 0
    dq = deque(data)

    while True:
        if len(dq) == 0:
            break
        if len(dq) == 1:
            cnt += 1
            dq.popleft()      
        elif dq[0] + dq[-1] <= limit:
            cnt += 1
            dq.popleft()
            dq.pop()
        else:
            cnt += 1
            dq.pop()
    print(cnt)
    return cnt
        
        
        
        
        
        
        
        
        
        
        
    