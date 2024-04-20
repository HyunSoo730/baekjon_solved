import heapq
import sys
from collections import deque


# 카드 정렬
# 정렬된 두 묶음의 숫자 카드.
# n개의 숫자카드 묶음의 각각의 크기 주어짐
# 최소한 몇번의 비교가 필요한지
# 우선순위큐.

n = int(input())
data = []
for _ in range(n):
    num = int(input())
    heapq.heappush(data, num) # 오름차순 우선순위큐

res = 0
while len(data) > 1:
    numA = heapq.heappop(data)
    numB = heapq.heappop(data)
    res += numA + numB
    heapq.heappush(data, numA + numB)

print(res)