import sys
from collections import deque

n = int(input())
k = int(input())
g = [[0] * n for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    g[a-1][b-1] = 1 #사과 위치

L = int(input()) #방향 변환 횟수
data = []
for _ in range(L):
    x,c = input().split()
    #x초 뒤에 c방향으로 회전
    data.append((int(x),c))

#자기 자신의 몸과 부딪히거나 벽과 부딪혀야 게임 끝.
g[0][0] = 2 #시작지점 (뱀)
x = y = 0 #시작위치
t = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]  #dx,dy는 이동하는 방향.
direction = 0 #방향 번호

dq = deque()
dq.append((0,0)) #뱀의 위치 큐로 관리

def turn(c):
    global direction
    if c == "L":
        direction = (direction - 1) % 4
    else: #오른쪽
        direction = (direction + 1) % 4
while True:
    t += 1
    x += dx[direction]
    y += dy[direction]

    if x<0 or x>=n or y<0 or y>=n: #벽에 부딪힘
        break
    if g[x][y] == 1: #사과를 먹음
        g[x][y] = 2 #뱀의 길이 증가. (머리부분)
        dq.append((x,y)) #위치 추가
    elif g[x][y] == 0: #그냥 도로
        g[x][y] = 2 #머리 이동하고 꼬리는 지우고
        dq.append((x,y))
        tx,ty = dq.popleft() #꼬리 부분
        g[tx][ty] = 0 #다시 도로로 포장.\
    else:
        break  #g[x][y] == 2 즉 이미 본인의 몸인 부분과 부딪힘.

    for a,b in data:
        if a == t: #회전할 타이밍.
            turn(b)
print(t)

