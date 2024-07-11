import sys
from collections import deque

# 일직선. 다양한 높이의 건물 n개 존재.
# 가희는 건물의 왼쪽에, 단비는 건물의 오른쪽에
# 가희, 1번 건물, 2번 건물 ... n번, 단비

# 현재 위치의 건물보다 왼쪽에 있는 건물들이 모두 현재 위치 건물보다 높이 작으면
# 가희는 현재 위치 건물 볼 수 있음

# 현재 위치 건물보다 오른쪽에 있는 건물들이 모두 현재 위치보다 높이가 작으면
# 단비는 현재 위치 건물 볼 수 있음

# 두 사람이 볼 수 있는 건물의 개수가 주어질 때,
# N개의 건물 높이 중 사전 순으로 가장 앞선 것 ??


n,a,b = map(int, input().split()) # 건물 개수, 가희가 볼 수 있는 a개, 단비가 볼 수 있는 b개

# 1~(a-1) ~ max(a,b) ~ (b-1) ~ 1


res = deque()

for i in range(1,a):
    res.append(i)
res.append(max(a,b))
for i in range(b-1, 0, -1):
    res.append(i)

if len(res) > n:
    print(-1)
else:
    temp = res.popleft() # 가장 첫번째 꺼 일단 꺼낸 다음에
    for _ in range(n - len(res) - 1): # 일단 한개 뺏으니까 그거만큼 반영
        res.appendleft(1)
    res.appendleft(temp)
    print(*res)