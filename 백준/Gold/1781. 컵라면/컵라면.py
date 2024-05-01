import heapq
import sys
from collections import deque


# n개의 문제 각 문제 풀었을 때 컵라면 몇개 줄 것인지 제시
# 받을 수 있는 최대 컵라면 수 구하기
# 각 문제마다 (데드라인, 컵라면 수) 가 주어진다.
# 데드라인 까지만 문제를 풀면 된다.

# -> 그리디. 결국 컵라면을 가장 많이 받는 문제를 푼다. 그리디적인 생각. 어떻게 ???
# 데드라인 많은 날짜에서부터 줄여나가면서 처리..
n = int(input())
data = []
for _ in range(n):
    deadline, cnt = map(int, input().split())
    data.append((deadline, cnt))

data.sort(key = lambda x : -x[0]) # 데드라인 내림차순
# print(data)

heap = []
res = 0
max_deadline = data[0][0]
dq = deque(data)
for deadline in range(max_deadline,0,-1):
    while dq and dq[0][0] >= deadline:
        d,cnt = dq.popleft()
        heapq.heappush(heap,-cnt)
    if heap:
        res += -heapq.heappop(heap)
print(res)