import heapq
import sys
from collections import deque


# 1km 가는데 1L의 연로가 필요
# 주유소 n개 존재
# 주유소에서 멈추는 횟수 최소화
# 각각의 주유소의 위치와 각 주유소에서 얻을 수 있는 연료의 양이 주어진다
# 주유소에서 멈추는 횟수 구하기 -> 가장 최소로 멈춰야 함

# 1. 시작점에서 도착점까지 필요한 연료
# L : 성경이의 위치에서 마을까지의 거리 P : 트럭에 원래 있던 연료 양
n = int(input())
data = []
for _ in range(n):
    a,b = map(int, input().split()) # 시작위치에서 현재 주유소까지 거리, 채울 수 있는 연료 양
    data.append((a,b))
L,P = map(int, input().split())
# 마지막 주유소 통과했을 때 검사하기 위해 도착점을 추가해줌. 
data.append((L,0))
data.sort(key = lambda x : x[0]) # 거리 기준 오름차순
if P >= L:
    print(0)
    exit(0)
# n <= 10,000 => n^2 가능
dq = deque(data)
cnt = 0
heap = []
for loc, power in data: # 하나씩 위치, 채울 수 있는 연료량 꺼내서
    if P >= L:
        break # 가능한 경우 끝
    while P < loc and heap: # 현재 연료로(위치로) 해당 주유소(loc,power) 못간다면
        # 현재까지의 주유소 중 가장 최대의 연료량을 꺼내서 넣어주기
        P += -heapq.heappop(heap)
        cnt += 1 # 넣어주면 해당 주유소 들린 거니깐 추가
    if P < loc: # 위 과정을 거쳤는데도 현재 주유소에 못간다는 것은 도달 못한다는 것.
        break
    heapq.heappush(heap, -power) # 주유소 우선순위 큐에 넣어두기 (어차피 거리순 정렬이라서 가능한 경우부터 만나게 된다.)

if P >= L:
    print(cnt)
else:
    print(-1)