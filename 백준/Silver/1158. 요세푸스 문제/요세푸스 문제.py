import sys
from collections import deque


n,k = map(int, input().split())
dq = deque(range(1,n+1))
res = []

while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())

print("<" + ", ".join(map(str, res)) + ">")