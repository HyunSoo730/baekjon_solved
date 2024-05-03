import heapq
import sys
from collections import deque


# 보석 털기
# 보석 총 N개, 각 보석 무게 m과 가격 v
# k개의 가방. 각 가방에 담을 수 있는 최대 무게 c
# 가방에는 한개의 보석만 넣을 수 있다.
# 훔칠 수 있는 보석의 최대 가격 구하기.
n, k = map(int, input().split())  # 보석 개수, 가방 개수
data = []
for _ in range(n):
    m, v = map(int, input().split())
    data.append((m, v))  # 각 보석의 무게, 가격

bags = []
for _ in range(k):  # k개 가방의 최대 무게
    bags.append(int(input()))  # 가방의 최대 무게

bags.sort() # 가장 최대 무게 오름차순 정렬
data.sort(key = lambda x : x[0]) # 보석을 무게 순으로 오름차순 정렬
res = 0
heap = []
dq = deque(data)
for weight in bags: # 각 가방의 최대 무게 하나씩 꺼내서
    while dq and dq[0][0] <= weight: # 현재 가방의 최대 무게보다 작다면
        m,v = dq.popleft() # 꺼낸 보석의 무게, 가격
        heapq.heappush(heap, -v) # 보석의 가격 최대 힙으로
    if heap: # 꺼낸 보석들이 존재한다면 그 중 최대 가치 꺼내야함
        res += -heapq.heappop(heap)
print(res)