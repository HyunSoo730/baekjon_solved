import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = 1 # ! 시작 방향은 오른쪽
n = int(input())
k = int(input()) # ! 사과 개수

g = [[0] * n for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    g[a-1][b-1] = 1 # ! 해당 칸에는 사과 존재

move = deque()
L = int(input())
for _ in range(L):
    t, d = map(str, input().split())
    move.append((int(t),d)) # ! 해당 시간에 해당 방향으로 이동

headX,headY = 0,0 # ! 시작 위치 및 머리 위치
dq = deque() # ! 뱀의 몸 좌표 저장
dq.append((headX,headY)) # ! 시작 위치 삽입 후 진행

def step1(dir): # ! 해당 방향으로 이동
    global headX,headY
    headX += dx[dir]
    headY += dy[dir]

def step2(): # ! 종료조건인지 확인 : 벽, 자기자신
    global headX, headY
    if not (0<= headX < n and 0<= headY < n): #! 범위 벗어나.
        return False
    if (headX, headY) in set(dq): # ! 몸통에 부딪힘
        return False
    return True

def step3():
    if g[headX][headY] == 0: # ! 해당 위치 사과 아닌 경우
        dq.popleft()  # ! 꼬리 부분 제거
    else: # ! 그렇지 않은 경우 ! 사과 없애야 해
        g[headX][headY] = 0 # ! 사과 없앰.

def step4(): # ! 해당 시간이 바꿀 시간이라면 바꿔
    global time, direction
    if move and time == move[0][0]: # ! 방향 바꿀 시간
        if move[0][1] == "L": # ! 현재 방향 기준 왼쪽으로 방향 전환\
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4
        move.popleft() # ! 앞에꺼 삭제


time = 0 # ! 시간
direction = 1 # ! 시작 방향.
# print(f"시작 좌표 : ({headX}, {headY})")
while True:
    step1(direction) # ! 현재 방향으로 이동
    # print(f"이동 후 좌표 : ({headX}, {headY})")
    time += 1
    if not step2(): # ! 종료조건인지 확인
        break
    else: dq.append((headX,headY))
    step3() # ! 아니라면 해당 칸 사과 확인
    step4() # ! 방향 바꿀 시간이라면 바꿔

print(time)