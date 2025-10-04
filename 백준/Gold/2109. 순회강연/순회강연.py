import sys
import heapq

# n개의 강연 요청 (n<=10^4)
# 각 대학에서 d일 안에 강연 해주면 p만큼의 강연료 지불
# 가장 많은 돈을 벌 수 있도록 순회강연. 하루에 한 곳만 강연 가능
# n == 0 고려

n = int(input())
if n == 0:
    print(0)
    exit(0)
data = []
for _ in range(n):
    p, d = map(int, input().split())
    data.append((d,p))

# 데드라인 내림차순
data.sort(key = lambda x : -x[0])
max_day = data[0][0]
heap = []
res = 0
idx = 0
for day in range(max_day, 0, -1): # 시작부터 끝까지 확인
    # step1. 해당 날짜까지 가능한 애들 모두 모으기
    while idx < n and data[idx][0] >= day:
        heapq.heappush(heap, -data[idx][1])
        idx += 1
    # step2. 해당날짜에 가능한 최대치 추가
    if heap:
        cost = -heapq.heappop(heap)
        res += cost

print(res)