import sys
import heapq

# n개의 회의. 각 회의는 시작시간, 끝나는 시간
# 한 회의실에 하나의 회의만 진행
# N개의 회의를 모두 진행할 수 있는 최소 회의실 개수 구하기
# O(N^2) 안됨. -> 시간 복잡도 고려하면서.

n = int(input())
data = []
for _ in range(n):
    a,b = map(int, input().split())
    data.append((a,b))

data.sort(key = lambda x : (x[0], x[1])) # 시작시간 오름차순

heap = []
heapq.heappush(heap, data[0][1]) # 가장 빨리 끝나는 시간 넣어두고.
cnt = 1
for i in range(1,n):
    start,end = data[i]
    if start < heap[0]: # 진행중인 회의의 끝나는시간보다 현재 회의 시작시간이 작으면
        cnt += 1
    else: # 시작시간이 같거나 크면. 이어서 가능 -> 꺼내기
        heapq.heappop(heap)
    heapq.heappush(heap, end) # 끝나는 시간 넣어.

print(cnt)