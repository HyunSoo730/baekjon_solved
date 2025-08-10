import sys
from collections import deque


# 건물 n개 존재.
# 가희 건물 기준 왼쪽, 단비 건물 기준 오른쪽
# n < 10^5
n, a, b = map(int, input().split()) # a는 가희가 볼 수 있는 건물 수 b는 단비가 볼 수 있는 건물 수

res = deque()
for i in range(1,a):
    res.append(i)
res.append(max(a,b))
for i in range(b-1, 0, -1):
    res.append(i)

if len(res) > n:
    print(-1)
else:
    temp = res.popleft()
    for _ in range(n - (len(res)+1)):
        res.appendleft(1)
    res.appendleft(temp)
    print(*res)
