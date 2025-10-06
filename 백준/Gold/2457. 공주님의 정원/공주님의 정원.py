import sys
import heapq

# N개의 꽃. 꽃이 피는 날, 지는 날 정해져있음
# 1. 3월 1일 ~ 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록
# 2. 정원에 심는 꽃 수 최소화
# 날짜를 어떻게 변환 ? -> 월 * 100으로 해주면 됨

n = int(input())
data = []
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, input().split())
    start,end = start_m * 100 + start_d, end_m * 100 + end_d # end 값은 제외해야함.
    data.append((start,end))

start, end = 301, 1130
idx = 0
res = 0
pos = 301
data.sort(key = lambda x : (x[0], -x[1]))

while pos <= end:
    next_pos = pos # 갱신될 다음 위치
    while idx < n and data[idx][0] <= pos:
        next_pos = max(next_pos, data[idx][1])
        idx += 1
    # 갱신 안되면 불가능
    if next_pos == pos:
        print(0)
        exit(0)
    res += 1
    pos = next_pos
print(res)
