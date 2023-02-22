import sys
from collections import deque


T = int(input())
for _ in range(T):
    n, m = map(int, input().split()) #문서의 개수, 몇번쨰 문서인지
    data = list(map(int, input().split())) #중요도. 중복 가능.
    #중복 가능해서 인덱스 확인해야함.
    dq = []
    for i in range(n):
        dq.append((i,data[i]))
    dq = deque(dq)
    cnt = 0
    while True:
        idx, val = dq.popleft() #우선순위와 idx값 같이
        if all(val >= x[1] for x in dq): #탈출해야함.
            cnt += 1
            if idx == m:
                break
        else:
            dq.append((idx,val))
    print(cnt)
            
        
    
    
    





