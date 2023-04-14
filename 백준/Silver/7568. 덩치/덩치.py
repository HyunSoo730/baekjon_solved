import sys


n = int(input())
data = []
for _ in range(n):
    m,k = map(int, input().split()) #몸무게, 키
    data.append((m,k))

res = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    res.append(cnt)
for x in res:
    print(x, end = " ")