import sys

N= int(input())

data = list(map(int ,input().split()))
data.sort()
sum = 0
res = 0
for i in range(N):
    sum += data[i]
    res += sum

print(res)
