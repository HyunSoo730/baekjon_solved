import heapq
import sys

# 보석 총 n개, 각 보석은 무게m 가격v, 가방을 k개 가지고 있고 각 가방에 담을 수 있는 최대 무게 c
# 가방에 최대 한개의 보석만.
# 최대 가격 구하기.

# 하나의 보석이 하나의 가방에 대해서만 가능. -> 최대로 고른다면. 이후의 선택에 영향을 미치지 않음.
# n,k <= 300,000 -> 우선순위 큐 사용 ?
n,k = map(int, input().split())
data = []
for _ in range(n):
    a,b = map(int, input().split()) # 무게, 가격
    heapq.heappush(data, (a,-b)) # 우선적으로 무게를 기준 오름차순, 가격 기준 내림차순
bags = []
for _ in range(k):
    bags.append(int(input())) # 각 가방의 최대 무게

bags.sort() # 가방의 최대 무게는 오름차순
res = 0
temp = []

for i in range(k):
    max_weight = bags[i]
    while data and data[0][0] <= max_weight:
        weight, value = heapq.heappop(data)
        heapq.heappush(temp, (value, weight)) # 이미 음수로 넣어뒀기 때문에 그냥 진행
    if temp: # 들어가 있다면 진행
        v,w = heapq.heappop(temp) # 가능한 애들 중에 가치가 가장 큰 애를 넣어줌.
        res += -v
print(res)