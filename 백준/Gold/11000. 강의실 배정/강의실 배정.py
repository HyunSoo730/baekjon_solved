import heapq
import sys

# 각 수업 시작시간, 끝시간 존재
# 기준 2개
# n <= 200,000
n = int(input())
data = []
for _ in range(n):
    start,end = map(int, input().split())
    data.append((start,end))

data.sort(key = lambda x : (x[0], x[1])) # 시작시간으로 먼저 오름차순 정렬하는 것이 핵심 !

heap = [] # 힙에는 끝나는 시간만 저장.
cnt = 0

for start,end in data:
    if heap and heap[0] <= start: # 현재 강의실이 가장 빨리 끝나는 강의의 끝나는 시간보다 같거나 크면 이어서 가능
        heapq.heappop(heap) # 현재꺼 없애고 이어가면 돼
    heapq.heappush(heap, end) # 현재꺼는 계속 넣어야 해

res = len(heap)
print(res)