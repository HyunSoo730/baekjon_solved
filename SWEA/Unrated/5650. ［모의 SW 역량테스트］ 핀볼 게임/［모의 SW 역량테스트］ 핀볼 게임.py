from collections import deque, defaultdict


# nxn 보드 , 5가지 블록, 웜홀, 블랙홀
# 핀볼은 블록이나 웜홀 또는 블랙홀을 만나지 않는 한 현재 방향 유지하면서 계속 전진
# 웜홀 6~10 블랙홀 -1 블록 1~5 0 빈공간

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def BFS():
    global res
    while dq: # 시작지점으로 가능한 좌표들을 다 꺼낸 후
        x,y = dq.popleft()
        for d in range(4):
            nx,ny = x,y # 출발점 저장
            cnt = 0
            while True:
                nx += dx[d]
                ny += dy[d]
                if not isInner(nx,ny): # 좌표 벗어남 : 반대 방향으로 바꿔준 후 이어서 진행
                    cnt += 1
                    d = (d+2) % 4 # 방향 전환
                    nx += dx[d]
                    ny += dy[d] #
                if nx == x and ny == y: # 시작점 도착
                    res = max(res, cnt)
                    break
                if g[nx][ny] == -1: # 블랙홀
                    res = max(res, cnt)
                    break
                if 1<= g[nx][ny] <= 5: # 블록인 경우 방향 전환
                    cnt += 1
                    d = change_direction(g[nx][ny], d)
                elif 6 <= g[nx][ny] <= 10: # 웜홀인 경우 위치 이동
                    holes = warmhole[g[nx][ny]] # 해당 원홀 두 개 꺼내서
                    if not (holes[0][0] == nx and holes[0][1] == ny): # 현재 위치 아닌경우
                        nx = holes[0][0]
                        ny = holes[0][1] # 해당 웜홀 위치로 이동
                    elif not (holes[1][0] == nx and holes[1][1] == ny): # 현재 위치 아닌 경우
                        nx = holes[1][0]
                        ny = holes[1][1] # 해당 웜홀 위치로 이동



def change_direction(num, direction): # 현재 블록번호와, 현재 방향
    if num == 1:
        if direction == 2: direction = 1
        elif direction == 3: direction = 0
        else: direction = (direction + 2) % 4
    elif num == 2:
        if direction == 0: direction = 1
        elif direction == 3: direction = 2
        else: direction = (direction + 2) % 4
    elif num == 3:
        if direction == 0: direction = 3
        elif direction == 1: direction = 2
        else: direction = (direction + 2) % 4
    elif num == 4:
        if direction == 1: direction = 0
        elif direction == 2: direction = 3
        else: direction = (direction + 2) % 4
    else:
        direction = (direction + 2) % 4
    return direction



T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    dq = deque() # 가능한 시작점 : 빈칸을 저장하기 위해
    warmhole = defaultdict(list) # 웜홀을 쌍을 저장하기 위해
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0: # 빈칸
                dq.append((i,j))
            if 6<=g[i][j]<=10: # 웜홀
                warmhole[g[i][j]].append((i,j)) # 웜홀의 번호를 키로 해서 값을 좌표로 저장

    # print(warmhole)
    res = 0
    BFS()

    print(f"#{t} {res}")
