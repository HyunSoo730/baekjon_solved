import sys
from collections import deque


n,m = map(int, input().split())
x,y,d = map(int, input().split()) #청소기 시작위치, 처음 바라보는 방향
#d가 0:북, 1:동, 2:남, 3:서
g = [list(map(int, input().split())) for _ in range(n)] #nxm 보드판
#0이면 청소하지 않은 빈칸, 1이면 벽
#멈출 때까지 청소하는 칸의 개수
ch = [[0] * m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1] #북 동 남 서 순으로 방향벡터 적용
cnt = 0
while True:
    if g[x][y] == 0 and ch[x][y] == 0:
        ch[x][y] = 1 #방문처리 -> 방문한 빈칸
        cnt += 1

    flag = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if g[nx][ny] == 0 and ch[nx][ny] == 0:
            flag = True
            #청소되지 않은 빈칸 존재
            break

    if flag == False: #방문 불가면 후진
        temp = (d + 2) % 4 #바라보는 방향은 유지.
        tx = x + dx[temp]
        ty = y + dy[temp]
        if 0<=tx<n and 0<=ty<m and g[tx][ty] == 0: #후진 가능 방문했는지는상관없음.
            x,y = tx,ty
            continue
        else:
            break
    else: #방문 가능
        d = (d+3) % 4 #반시계 이동후
        tx = x + dx[d]
        ty = y + dy[d]
        if 0<=tx<n and 0<=ty<m and g[tx][ty] == 0 and ch[tx][ty] == 0:
            x,y = tx,ty


print(cnt)






