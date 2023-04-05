import sys
from collections import deque


n,m, x, y, k = map(int, input().split())
g = []
for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)

data = list(map(int, input().split())) #명령의 개수
dice = [0] * 7 #1번~6번까지 사용
dx = [0,0,-1,1]
dy = [1,-1,0,0] #동 서 북 남 순으로 방향벡터 사용
direction = 0 #방향 번호
def turn(direction): #방향에 따른 규칙성
    #위, 뒤, 오른쪽, 왼쪽, 앞쪽, 바닥쪽 #이 방식으로 저장.
    a,b,c,d,e,f = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    if direction == 1: #동쪽으로 이동
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = d, b, a, f, e, c
    elif direction == 2: #서쪽으로 이동
        dice[1],dice[2],dice[3],dice[4],dice[5],dice[6] = c,b,f,a,e,d
    elif direction == 3: #북쪽으로 이동
        dice[1],dice[2],dice[3],dice[4],dice[5],dice[6] = e,a,c,d,f,b
    else: #남쪽으로 이동
        dice[1],dice[2],dice[3],dice[4],dice[5],dice[6] = b,f,c,d,a,e
#바닥면은 dice[6], 윗면은 dice[1]

for direction in data:
    x += dx[direction-1]
    y += dy[direction-1]

    if x<0 or x>=n or y<0 or y>=m: #예외처리
        x -= dx[direction-1]
        y -= dy[direction-1] #원상복구 시키고 돌아가야함. 이 부분이 중요했음.
        #해당 명령 무시해야 하므로 원상복구.
        continue
    turn(direction)
    if g[x][y] == 0: #지도 상에 0이면 바닥면에 쓰여있는 수 지도에 복사
        g[x][y] = dice[6]
    else: #0이 아니라면 지도에 있는 수가 바닥면으로 복사, 지도는 0으로 바뀜.
        dice[6] = g[x][y]
        g[x][y] = 0
    print(dice[1])
