from collections import defaultdict, deque

# 정사각형 구역 안에 K개의 미생물 군집 존재
# 해당 구역 nxn, 가장 바깥쪽 영역 약품 칠해져있음
# 1. 초기 상태 : 미생물 군집의 위치(x,y), 군집 내 미생물 수 , 이동방향 주어짐, 이동방향 상하좌우
# 2 가장 바깥쪽 영역 약 품 칠해진 영역에 도착하면 군집 내 미생물 절반이 죽고(소수점 버림) 이동방향 반대로 바뀜
# 3. 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집 합침
# + 미생물 수 합하기 , 가장 많았던 군집의 이동방향으로.
# M시간 동안 미생물 격리, M시간 후 남아있는 미생물 수의 총합 구하기

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
def isInner(x,y):
    if 1<=x<n-1 and 1<=y<n-1:
        return True
    return False

def 방향전환(dir):
    if dir == 1: dir = 2
    elif dir == 2: dir = 1
    elif dir == 3: dir = 4
    elif dir == 4: dir = 3
    return dir

def 격리():
    temp = defaultdict(list)
    while 군집: # 일단 전부 하나씩 꺼내서 이동 시킴
        x,y,cnt,dir = 군집.popleft()
        x += dx[dir]
        y += dy[dir] # 일단 이동 시킨 후
        if not isInner(x,y): # 약품 위치로
            cnt = int(cnt/2) # 소수점 버리면서 개체 수 절반으로
            dir = 방향전환(dir)
        if cnt > 0:
            temp[(x,y)].append((cnt,dir)) # 해당 위치에 군집의 수, 방향 저장

    # 모든 애들 이동방향으로 이동 시킨 후 결집
    for (x,y) , value in temp.items():
        if len(value) == 1: # 해당 위치에 하나의 군집만
            군집.append((x,y,value[0][0], value[0][1]))
        else: # 여러개.
            max_cnt = 0
            max_dir = -1
            sum_cnt = 0
            for cnt,dir in value: # 하나씩 꺼내서
                sum_cnt += cnt
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_dir = dir
            군집.append((x,y,sum_cnt,max_dir))

T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split()) # 크기, 격리 시간, 미생물 군집 수
    군집 = deque()
    for _ in range(k): # 각 군집 정보
        x,y,cnt,dir = map(int, input().split())
        군집.append((x,y,cnt,dir))

    for _ in range(m): # m시간 격리 진행
        격리()
    # m시간 격리 후 남은 미생물 수 구하기
    res = 0
    for data in 군집:
        res += data[2]
    print(f"#{t} {res}")