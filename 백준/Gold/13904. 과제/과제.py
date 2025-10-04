import sys
import heapq

# 과제. 과제마다 마감일 존재. 모든 과제를 끝내지 못할 수도 있음
# 과제마자 마감일 | 점수가 있음 -> 가장 점수를 많이 받을 수 있도록.

n = int(input())
data = []
for _ in range(n):
    d, w = map(int, input().split())
    data.append((d,w))

data.sort(key = lambda x : -x[0]) # 데드라인 기준 내림차순

res = 0
idx = 0
heap = []
max_deadline = data[0][0]

for deadline in range(max_deadline, 0, -1):
    # step1. 데드라인 이상인, 즉 가능한 경우를 모두 추출
    while idx < n and data[idx][0] >= deadline:
        heapq.heappush(heap, -data[idx][1]) # 얻는 점수를 내림차순으로 넣어둬야함
        idx += 1
    # step 2.  해당 날짜에 뽑아낼 수 있는 것이 있다면 최대 치 뽑아냄
    if heap:
        cost = -heapq.heappop(heap)
        res += cost

print(res)

