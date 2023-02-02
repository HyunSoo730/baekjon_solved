import sys


N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

cnt = 0
for i in range(N-1, 0, -1):
    while data[i-1] >= data[i]:
        cnt += 1
        data[i-1] -= 1

print(cnt)
