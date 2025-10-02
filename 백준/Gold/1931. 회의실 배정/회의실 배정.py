import sys

# 회의실 -> N개의 회의에 대하여 회의실 사용표 만들기
# 각 회의에 대해 시작시간, 끝시간 존재.
# 각 회의가 겹치지 않게, 최대 사용할 수 있는 회의의 최대 개수
# N^2 불가.
"""
겹치면 안됨. 그러면서도 사용할 수 있는 최대의 회의 개수. 
회의를 선택하거나 버림 -> 한번 선택하면 끝. 다시 고려 X
"""

n = int(input())
data = []
for _ in range(n):
    start,end = map(int, input().split())
    data.append((start,end))

data.sort(key = lambda x : (x[1], x[0]))

cnt = 0
last_end_time = 0
for start, end in data:
    if last_end_time <= start:
        cnt += 1
        last_end_time = end

print(cnt)