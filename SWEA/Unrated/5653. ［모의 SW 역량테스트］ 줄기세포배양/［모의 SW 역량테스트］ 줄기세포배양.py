
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def simulate():
    grid = {} # ! 딕셔너리로 관리

    # ! 1, 초기 세팅
    for i in range(n):
        for j in range(m):
            if g[i][j] > 0:
                grid[(i,j)] = [g[i][j], g[i][j], 0] # ! 생명력, 활성화까지 시간, 활성화된 후부터 시간
    # ! 2. 시뮬
    for _ in range(k):
        newCell = {}  # ! 이번 타임에 번식 진행
        for (x,y) , value in grid.items():
            if value[1] > 0: # ! 아직 비활성화
                grid[(x,y)][1] -= 1 # ! 갱신 -> 리스트로 설정해야 값 변경 가능
            else: # ! 활성화 상태 -> 1, 4방 탐색, 이미 했다면 활성화된 시간 감소
                if value[0] > value[2]: # ! 활성화된 시간이 생명력보다 작을 때만 작동
                    if value[2] == 0: # ! 첫 활성화 -> 4방 탐색
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if (nx,ny) not in grid.keys() and (nx,ny) not in newCell.keys(): # ! 첫 등장 -> 그냥 삽입
                                newCell[(nx,ny)] = [value[0], value[0], 0]
                            elif (nx,ny) in newCell.keys(): # 이미 존재한다면 더 큰 생명력으로
                                if newCell[(nx,ny)][0] < value[0]:
                                    newCell[(nx,ny)] = [value[0], value[0], 0]
                    grid[(x,y)][2] += 1 # ! 활성화 된 시간 + 1
        # ! 번식한 세포 추가
        for pos, val in newCell.items():
            grid[pos] = val

    # ! 비활성 상태 + 활성 상태
    cnt = 0
    for (x,y), value in grid.items():
        if value[0] > value[2] or value[1] > 0: # ! 비활성 상태 or 살아있음
            cnt += 1
    return cnt



T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    cnt = simulate()
    print(f"#{t} {cnt}")
