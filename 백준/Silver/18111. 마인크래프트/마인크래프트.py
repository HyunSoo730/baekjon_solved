import sys
from collections import deque

#1번 작접 2초 2번 작업 1초
#최소시간, 땅의 높이

n,m,inventory = map(int, input().split()) #세로, 가로, 인벤토리 블록 개수
g = [list(map(int, input().split())) for _ in range(n)] #nxm 땅의 높이

res = int(1e9)
height = 0

for target in range(257): #0~256층까지 반복
    max_target = 0
    min_target = 0

    for x in range(n):
        for y in range(m):
            #블록이 층수보다 더 크면
            if g[x][y] >= target:
                max_target += g[x][y] - target
            #블록이 층수보다 더 작으면
            else:
                min_target += target - g[x][y]
    #블록을 뺸 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    #블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음. 인벤토리 부족하면 안되니깐.
    if max_target + inventory >= min_target:
        if min_target + max_target * 2 <= res: #최저 시간과 비교. 그러나 같은 값이면 그 중에서 땅의 높이가 가장 높은 것을 출력해야 하므로 = 필요
            res = min_target + max_target * 2
            height = target

print(res, height)


