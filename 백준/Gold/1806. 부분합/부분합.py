import sys

n,m = map(int, input().split())
data = list(map(int, input().split()))

res = int(1e9)
e = 0
flag = False
interval_sum = 0 # 부분합
for s in range(n):
    while interval_sum < m and e < n:
        interval_sum += data[e]
        e += 1
    if interval_sum >= m:
        flag = True
        length = e-s
        if length < res:
            res = length
    interval_sum -= data[s]
if flag:
    print(res)
else:
    print(0)

