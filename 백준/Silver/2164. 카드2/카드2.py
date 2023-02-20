import sys

input = sys.stdin.readline
from collections import deque
n = int(input())
data = list(range(1,n+1))
#시작 1이 가장 위 n이 가장 아래
dq = deque(data)
res = -1 
while len(dq) > 1:
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)
res = dq.popleft()
print(res)
    
    