import sys

N, K = map(int ,input().split())

data = []
for i in range(N):
    data.append(int(input()))

data.sort(reverse = True)
cnt = 0
for i in range(N):
    if data[i] > K:
        continue
    cnt += K // data[i]
    K = K % data[i]

    if K == 0:
        break

print(cnt)
