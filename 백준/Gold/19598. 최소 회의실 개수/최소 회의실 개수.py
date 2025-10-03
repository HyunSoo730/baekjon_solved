import sys
import heapq

# N개의 회의 모두 진행할 수 있는 최소 회의실 개수.
# N^2 불가.
# 끝나는 시간대ㅐ로 꺼내서. 현재 가지고 있는 회의실에서 진행 가능한지 판단. 가능하면 + 불가능이면 회의실 + 1
n = int(input())
data = []
for _ in range(n):
    start,end = map(int, input().split())
    data.append((start,end))

data.sort(key = lambda x : x[0])
heap = []
for start, end in data:
    # 가장 빨리 끝나는 회의실이 현재 회의 시작 전에 끝나는가 ?
    if heap and heap[0] <= start: # heap 에는 종료시간 있어.
        heapq.heappop(heap) # 해당 회의실 재사용 해야함.
    # 현재 회의 종료 시간 추가 (무조건)
    heapq.heappush(heap, end)
res = len(heap)
print(res)