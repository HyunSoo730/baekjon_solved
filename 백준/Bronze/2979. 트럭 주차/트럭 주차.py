import sys
temp = list(map(int, input().split()))

data = []
timeA = 24242424
timeB = -24242424
for _ in range(3):
    start, end = map(int, input().split())
    data.append((start,end))
    timeA = min(timeA, start)
    timeB = max(timeB, end)

res = 0
for time in range(timeA, timeB + 1):
    cnt = 0
    for i in range(3):
        if data[i][0] <= time < data[i][1]:
            cnt += 1
    if cnt == 1: #한 트럭만
        res += temp[0]
    elif cnt == 2: #두 트럭만
        res += temp[1] * 2
    elif cnt == 3:
        res += temp[2] * 3

print(res)













