import sys


N, M = map(int, input().split())

data = []
for i in range(M):
    data.append(int(input()))

data.sort()
res = 0 #최대 수익
egg = 0  #달걀을 책정한 가격
for i in range(M):
    cnt = min(M-i, N)  #팔 수 있는 달걀 개수

    if res < data[i] * cnt:
        res = data[i] * cnt
        egg = data[i]


print(egg, res)
