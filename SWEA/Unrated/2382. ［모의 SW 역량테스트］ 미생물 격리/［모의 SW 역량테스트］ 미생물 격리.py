from collections import deque, defaultdict

# 상 하 좌 우 : 1 2 3 4
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

def isInner(x,y):
    if 1<=x<n-1 and 1<=y<n-1:
        return True # 약품 외 내부는 안전
    return False # 이 경우는 약품에 도달한 경우

def BFS():
    global dq
    time = 0 # 시간 시간
    res = 0
    while dq:
        time += 1 # 시간이 
        size = len(dq) # 시간에 따라서 진행해야 하므로 현재 시간에 저장되어 있는 애들만 돌아야지
        check = defaultdict(list) # 이동할 좌표의 겹침을 해결하기 위해
        for _ in range(size):
            x,y,cnt,d = dq.popleft() # 현재 미생물 군집의 좌표, 미생물 개수, 방향
            nx = x + dx[d]
            ny = y + dy[d]
            if not isInner(nx,ny): # 약품에 들어간 경우
                cnt = int(cnt/2)
                if d == 1: d = 2
                elif d == 2: d = 1
                elif d == 3: d = 4
                elif d == 4: d = 3
                dq.append((nx,ny,cnt,d))
            if isInner(nx,ny): # 이동 가능
                check[(nx,ny)].append((cnt,d)) # 현재 좌표에 미생물 개수, 방향을 일단 넣어두기


        # 현재 타입에서 모두 확인한 후 이제 겹치는지 확인하면서 큐에 넣기
        for (nx,ny), val in check.items():
            if len(val) == 1: # 특정 좌표에 딱 하나 존재한다면
                dq.append((nx,ny,val[0][0], val[0][1])) # 그대로 추가
            elif len(val) > 1: # 특정 좌표에 여러개가 존재
                cnt_sum = 0
                cnt_max = 0
                idx = 0
                for i in range(len(val)): # 하나씩 확인하면서 최대값
                    cnt_sum += val[i][0] # 미생물 개수는 다 더해주고
                    if val[i][0] > cnt_max:
                        cnt_max = val[i][0]
                        idx = i
                d = val[idx][1]
                dq.append((nx,ny,cnt_sum,d))
        # print(f"{time}초 지난 후 미생물 군집 상황")
        # for now in dq:
        #     print(f"좌표 : {now[0], now[1]}, 미생물 수 : {now[2]} 방향 : {now[3]}")


        if time == m: # 해당 시간에 도달하면 현재까지 존재하는 미생물 수 합 반환
            for now in dq:
                res += now[2]
            return res
            break



T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split())
    # k개의 미생물 군집의 정보
    dq = deque()
    for _ in range(k):
        x,y,cnt, d = map(int, input().split()) # 해당 군집의 x,y,미생물 개수,방향
        dq.append((x,y,cnt,d))

    res = BFS()
    print(f"#{t} {res}")
