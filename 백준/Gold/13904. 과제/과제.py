import sys
import heapq

# 하루에 과제 하나.
# 과제마다 끝낼 때 얻을 수 있는 점수. 마감일이 지난 과제는 점수 X
# 가장 많은 점수

n = int(input())
data = []
for _ in range(n):
    d,w = map(int, input().split())
    data.append((d,w)) # 과제 마감일, 과제 점수

data.sort(key = lambda x : (-x[0], -x[1])) # 과제 마감일 내림차순
max_deadline = data[0][0]
res = 0
idx = 0
heap = [] # 뽑을 수 있는 후보군. 즉 해당 날짜에 선택 가능한 애들 모음

for deadline in range(max_deadline, 0, -1): # 하루씩 줄여나가면서...
    # step1. 데드라인 이상. 즉 추출 가능
    while idx < n and data[idx][0] >= deadline:
        heapq.heappush(heap, -data[idx][1]) # 점수 내림차순으로
        idx += 1
    # step2. 해당 날짜에 뽑아낼 수 있어 ? -> 최대치
    if heap:
        cost = -heapq.heappop(heap)
        res += cost

print(res)