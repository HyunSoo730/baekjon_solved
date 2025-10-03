import sys
import heapq

# 과제 : 시작시간 ~ 끝나는 시간. N개 존재.
# 최소의 강의실을 사용해서 모든 수업 가능하게 해야함 -> 모두 사용. 즉 최소 자원
# N^2 불가 -> 그리디 + 우선순위 큐 생각해보자
n = int(input())
data = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

data.sort(key = lambda x : x[0]) # 시작시간으로

heap = []
for start, end in data:
    # step1. ~ (여기에 뭐라고 ㅈ거어놓는게 좋을까 ? )
    if heap and heap[0] <= start: # 현재 강의 시작시간이 가장 빨리 끝나는 강의의 종료시간 보다 빠르면 재사용 가능
        heapq.heappop(heap)
    # step2. 해당 자원은 항상 사용 ? (뭐라고 표기...)
    heapq.heappush(heap, end) # 종료시간순으로 !
res = len(heap)
print(res)