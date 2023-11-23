import sys
from collections import deque


# N개의 수로 된 수열
# i ~ j 번째까지의 수의 합이 M 이 되도록

n, m = map(int, input().split())
data = list(map(int, input().split()))

s,e = 0,0
interval_sum = 0 # 구간 합
cnt = 0
for s in range(n):
    while interval_sum < m and e < n:
        interval_sum += data[e]
        e += 1
    # 탈출하는 경우는 구간 합이 m 이거나 그보다 크거나
    if interval_sum == m:
        cnt += 1
    interval_sum -= data[s] # m인 경우, 그보다 큰 경우 모두 빼야함

print(cnt)