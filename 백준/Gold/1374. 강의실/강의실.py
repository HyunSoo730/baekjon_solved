import sys
import heapq

# N개의 강의실. 모든 강의는 시작시간, 끝나는시간.
# 최대한 적은 수의 강의실 사용하여 모든 강의. -> 모든 강의 진행, 최소 강의실 (최소 자원)
# N^2 -> 그리디

n = int(input())
data = []
for _ in range(n):
    num, start, end = map(int, input().split())
    data.append((start, end))
data.sort(key = lambda x : x[0])

heap = []
for start, end in data:
    # step1. 가장 빨리 끝나는 자원 재사용 가능한가 ?
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    # step2. 현재 자원 사용 (재사용 or 신규)
    heapq.heappush(heap, end)

res = len(heap)
print(res)