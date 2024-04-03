from collections import defaultdict, deque


east = 2
west = 6

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def BFS(v, d): # 회전 시작 자석 번호, 회전 방향 1 : 시계, -1 : 반시계
    dq = deque()
    dq.append((v,d)) # 현재 회전시킬 자석 번호, 방향
    visited = [False] * 5
    visited[v] = True
    while dq:
        now, dir = dq.popleft() # 현재 회전시킬 자석의 번호, 방향
        # 회전시키기 전 좌우 확인
        if dir == 1: # 시계
            if now + 1 <= 4 and not visited[now+1]: # 오른쪽 존재
                visited[now+1] = True
                if data[now][east] != data[now+1][west]: # 같지 않으면 옆에 애도 회전
                    dq.append((now+1, dir * (-1))) # 반대방향 회전
            if now - 1 >= 1 and not visited[now-1]: # 왼쪽 존재
                visited[now-1] = True
                if data[now][west] != data[now-1][east]: # 같지 않으면 회전
                    dq.append((now-1, dir* (-1)))
            # print(f"기존 값 = {data[now]}")
            data[now] = data[now][7:] + data[now][:7] # 마지막 1개 + 처음 7개
            # print(f"회전 후 값 = {data[now]}")
        else: # 반시계 회전
            if now + 1 <= 4 and not visited[now+1]:
                visited[now + 1] = True
                if data[now][east] != data[now+1][west]:
                    dq.append((now+1, dir*(-1)))
            if now -1 >= 1 and not visited[now-1]: # 왼쪽 존재
                visited[now-1] = True
                if data[now][west] != data[now-1][east]: # 같지 않으면 반대방향 회전
                    dq.append((now-1, dir*(-1)))
            # print(f"기존 값 = {data[now]}")
            data[now] = data[now][1:] + data[now][:1] # 마지막 7개 + 처음1개
            # print(f"회전 후 값 = {data[now]}")


def print_debug():
    for i in range(1,5):
        print(data[i])
    print()

T = int(input())
for t in range(1,T+1):
    k = int(input()) # 자석 회전시키는 횟수
    data = defaultdict(list)
    for i in range(1,5): # 자석 정보
        temp = list(map(int, input().split())) # 각 자석의 8개의 날 정보
        data[i] = temp

    # 회전 정보 (자석 번호, 회전방향) 1 : 시계, -1 : 반시계
    # print("시작 자석")
    # print_debug()
    for _ in range(k): # 자석을 1칸씩 회전시키는 회전 정보
        v, d = map(int, input().split())
        BFS(v,d)     # 회전 자석 번호, 방향
        # print("회전 후 상황 확인")
        # print_debug()
    res = 0
    for now in range(1,5):
        if data[now][0] == 1: # S극이면 더해
            res += pow(2,now-1)

    # print_debug()
    print(f"#{t} {res}")


