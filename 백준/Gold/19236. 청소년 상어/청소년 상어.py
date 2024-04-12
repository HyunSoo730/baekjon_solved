import sys
from collections import defaultdict


# 4x4 보드, 각 칸은 (x,y)
# 각 칸은 물고기 번호와 방향. 존재
# 번호는 1~16 사이의 자연수, 번호 중복 안됨. 방향은 8가지 (상하좌우, 대각선)
# 청소년 상어가 이 공간에 들어가 물고기를 먹는다.
# 1.  (0,0) 에 있는 물고기 먹고  (0,0)에 들어가게 되고, 먹은 물고기 방향이 됨
# 이후 물고기가 이동.
# 물고기는 번호 작은 물고기부터 순서대로 이동.
# 이동 가능 : 빈칸, 다른 물고기가 있는 칸
# 이동 불가 : 상어, 내부 좌표 아닌 경우
# 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전, 이동 가능한 순간 이동.
# 이동할 수 있는 칸이 없으면 이동 X
# 그 외의 경우는 이동할 수 있는 칸으로 이동.  물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾼다.
# 물고기들 이동이 끝나면 상어가 이동. 상어는 방향에 있는 칸으로 이동. 한번에 여러개의 칸 이동 가능
# 상어가 물고기가 있는 칸으로 이동했다면 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.  이동하는 중에 지나는 칸에 있는 물고기는 먹지 않음. + 물고기가 없는 칸으로 이동할 수 없음
# 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나서 집으로.
# 구하고자 : 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]  # 0~7 방향
g = [[0] * 4 for _ in range(4)]  # 4x4 미리 만들어 두고
fish = [[] for _ in range(17)]
for x in range(4):
    data = list(map(int, input().split()))
    for y in range(4):
        a,b = data[y*2], data[y*2+1]
        fish[a] = [x,y,b-1] # a번 물고기의 x좌표, y좌표, 방향 저장. 방향은 0번부터 사용하기 위해
        g[x][y] = a # 물고기 위치를 따로 저장

die = [False] * 17 # 1~17번 물고기 죽었는지 확인

def DFS(sharkX, sharkY, sum_data, fish, g): # 상어의 위치, 현재까지의 합, 현재 이동 경로의 물고기, 보드
    global res
    global die
    copy_g = [arr[:] for arr in g]
    copy_fish = [arr[:] for arr in fish] # 둘 다 복사해놓고 시작
    # 복사한 애들 사용

    # step1. 상어가 현재 방향의 물고기 먹기
    fish_num = copy_g[sharkX][sharkY] # 현재 보드에 위치한 물고기 번호
    sum_data += fish_num # 해당 물고기 먹었음
    shark_dir = copy_fish[fish_num][2] # 물고기의 방향으로 변경
    die[fish_num] = True # 해당 물고기 죽이기
    copy_g[sharkX][sharkY] = -1 # 죽은 처리

    # 상어가 먹은 후 매 순간 검사
    res = max(res, sum_data) # 매 순간 최대값 겁사


    # step2. 물고기 움직임
    fish_move(sharkX,sharkY,copy_fish, copy_g)

    # step3.  상어 움직임 - 현재 이동하려는 방향에 물고기가 있다면 다 갈 수 있음

    while True:
        sharkX += dx[shark_dir]
        sharkY += dy[shark_dir]
        if not isInner(sharkX,sharkY): # 상어가 못 움직인다면
            break # 끝
        if copy_g[sharkX][sharkY] != -1: # 해당 위치에 물고기 존재하면 이동 가능
            DFS(sharkX,sharkY,sum_data, copy_fish, copy_g)

    # 백트랙킹 시 원상복구 -> 물고기 살리기
    die[fish_num] = False


def isInner(x,y):
    if 0<=x<4 and 0<=y<4:
        return True
    return False
def fish_move(sharkX,sharkY,fish,g): # 살아있는 물고기 움직이기
    global die
    for i in range(1,17):
        if die[i]: continue

        x,y,dir = fish[i] # 현재 물고기의 위치, 방향
        for d in range(8):
            direction = (dir + d) % 8
            nx = x + dx[direction]
            ny = y + dy[direction]
            if isInner(nx,ny) and (nx,ny) != (sharkX,sharkY): # 내부이면서 상어위치가 아니면 이동 가능
                if g[nx][ny] != -1: # 해당 위치에 물고기 존재.
                    # 위치 변경
                    target = g[nx][ny] # 이동할 방향의 물고기 번호
                    fish[target][0],fish[target][1] = x,y # 이동할 방향의 물고기의 위치를 현재 물고기의 위치로 변경
                    fish[i][0],fish[i][1] = nx,ny # 현재 물고기 위치를 이동할 위치로 변경
                    fish[i][2] = direction # 물론 현재 물고기는 방향까지 바꿔줘야함.
                    # 물고기 위치 정보 변경
                    g[x][y] = target
                    g[nx][ny] = i # 물고기의 위치를 저장하는 보드에도 반영
                else: # 만약 해당 위치에 물고기가 없다면 그냥 옮겨주면 돼
                    fish[i][0],fish[i][1] = nx,ny
                    fish[i][2] = direction
                    g[nx][ny] = i
                    g[x][y] = -1 # 보드도 갱신
                # print(f"현재 {i}번 물고기 기존 위치 : {x,y,dir} -> 이동 위치 : {nx,ny,dir}")
                # print(f"{i}번 물고기 움직임 후 위치에 따른 물고기 번호")
                # 보드출력해보기(g)
                break # 현재 물고기의 행동이 끝났다면 끝 !

def 보드출력해보기(g):
    for i in range(4):
        for j in range(4):
            print(g[i][j], end = " ")
        print()
    print("-----------------")

# 물고기 이동. 번호 작은 순서대로
res = 0
DFS(0,0,0,fish,g)
print(res)