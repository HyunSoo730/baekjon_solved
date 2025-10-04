import sys
import heapq

# n개의 문제. 각 문제를 풀었을 때 컵라면 몇개 줄 것인지 제시
# 데드라인 존재. -> 뒤에서부터 하면 그리디적으로 해결가능하지 않을까 ?
# 동호가 받을 수 있는 최대 컵라면 수 구하기

n = int(input())
data = []
for _ in range(n):
    d, cnt = map(int, input().split())
    data.append((d, cnt))

data.sort(key = lambda x : -x[0])
max_deadline = data[0][0]
res = 0
idx = 0
heap = [] # 가능한 애들
for deadline in range(max_deadline, 0, -1):
    # step1. deadline 이후인 애들 중에서 가능한 애들 모두 추출
    while idx < n and data[idx][0] >= deadline:
        heapq.heappush(heap, -data[idx][1])
        idx += 1
    # step2. 가능한 애들중에 오늘자에 추출할 최대값 선택
    if heap:
        cost = -heapq.heappop(heap)
        res += cost

print(res)