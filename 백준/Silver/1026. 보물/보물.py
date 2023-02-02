import sys


N = int(input())
dataA = list(map(int, input().split()))
dataB = list(map(int, input().split()))

dataA.sort()
res = 0
for i in range(N):
    max_A = dataA[i]
    min_B = dataB.pop(dataB.index(max(dataB)))
    res += max_A * min_B

print(res)