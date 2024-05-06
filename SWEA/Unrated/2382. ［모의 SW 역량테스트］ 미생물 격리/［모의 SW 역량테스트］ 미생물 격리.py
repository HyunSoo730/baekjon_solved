from collections import defaultdict, deque

# k개의 미생물 군집
# nxn 맵, 가장 바깥쪽 가장자리 부분의 칸들은 특수약품 칠해져있음
# 초기상태 : 각 미생물 군집의 위치, 수, 방향 주어진다.
# 각 미생물 군집은 1시간마다 이동방향에 있는 다음 셀로 이동
# 약품이 칠해진 셀(가장 가장자리) 도착 시 군집 내 미생물의 절반이 죽고, 이동방향 반대로 바꾸기
# -> 2로 나눈 후 소수점 버리기
# 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집 합치기
# -> 합쳐진 군집의 미생물 수는 군집들의 미생물 수의 합, 이동방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향.
# M시간 동안 미생물 격리, M시간 후 살아남은 미생물 수의 총합 구하기

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1] # 상 1 하 2 좌 3 우 4
def isInner(x,y):
    if 1<=x<n-1 and 1<=y<n-1:
        return True
    return False
def 방향전환(dir):
    if dir == 1: return 2
    elif dir == 2: return 1
    elif dir == 3: return 4
    elif dir == 4: return 3
def 이동():
    global 군집
    while dq:
        x,y,cnt,dir = dq.popleft() # 현재 군집의 위치, 개수, 방향
        x += dx[dir]
        y += dy[dir]
        if not isInner(x,y): # 약품의 위치에 들어감
            dir = 방향전환(dir)
            cnt = int(cnt/2)
            if cnt > 0:
                군집[(x,y)].append((cnt,dir))
        else: # 내부 좌표라면 그냥 추가
            군집[(x,y)].append((cnt,dir))
    # 모든 애들을 다 넣어준 후에 이제 진행
    for (x,y), value in 군집.items(): # value의 첫번째 인덱스는 각 좌표에 추가된 애들, 두번째 인덱스는 0은 cnt, 1은 dir을 나타내
        if len(value) == 1: # 해당 위치에 하나의 군집만 위치
            dq.append((x,y,value[0][0], value[0][1]))
        else: # 이제 여기서 하나씩 확인
            max_cnt = 0
            max_dir = -1
            sum_cnt = 0
            for i in range(len(value)):
                sum_cnt += value[i][0]
                if value[i][0] > max_cnt:
                    max_cnt = value[i][0]
                    max_dir = value[i][1]
            dq.append((x,y,sum_cnt, max_dir))

def 남은미생물개수():
    cnt = 0
    while dq:
        _,_,c,_ = dq.popleft()
        cnt += c
    return cnt

def 군집출력():
    for i in range(len(dq)):
        print(f"현재 군집의 위치 :{dq[i][0], dq[i][1]} 군집 수 : {dq[i][2]} 군집 방향 : {방향변환(dq[i][3])}")
def 방향변환(dir):
    if dir == 1:
        return "상"
    elif dir == 2:
        return "하"
    elif dir == 3:
        return "좌"
    elif dir == 4:
        return "우"

T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split()) # nxn, m의 격리시간, k개의 군집 수
    data = [] # 군집 정보
    for _ in range(k):
        x,y,cnt,dir = map(int, input().split()) # 세로,가로,군집수,방향
        data.append((x,y,cnt,dir))
    # 1. 각 미생물 이동방향으로 이동 시키기
    # 2. 가장자리로 이동한 군집은 군집 수 반으로 줄이기, 방향 반대로 만들기
    # 3. 같은 위치로 이동한 애들은 군집 합치기, 군집 수는 합치고, 방향은 최대 군집의 방향 유지
    # -> 모두 움직인 후에 알 수 있으므로 바로 움직이는게 아니라, 각 값들을 저장 후에 한번에 이동시켜야함.
    time = 0
    dq = deque(data) # 하나씩 꺼내면서 위치를 이동시킬 것.
    while True:
        군집 = defaultdict(list)
        # print(f"현재 시간 :{time} 에서의 군집 출력")
        # 군집출력()
        이동()
        time += 1
        if time == m:
            break
    # 미생물 수의 총 합
    res = 남은미생물개수()
    print(f"#{t} {res}")