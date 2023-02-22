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

cnt = [0] * timeB
for i in range(3):
    start = data[i][0]
    end = data[i][1]
    for j in range(start, end): #시작점을 포함시킬꺼면 끝점은 빼야함.
        cnt[j] += 1

res = 0
for x in cnt:
    if x == 1:
        res += temp[0]
    elif x == 2:
        res += temp[1] * 2
    elif x == 3:
        res += temp[2] * 3
print(res)