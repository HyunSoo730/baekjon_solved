import sys
from collections import deque


def BFS(a,b):
    dq = deque()
    dq.append((a,b))

    while dq:
        x,y = dq.popleft()
        if abs(x-end[0]) + abs(y - end[1]) <= 1000: # ! 맥주병 20개로 갈 수 있는 최대 거리 1000
            return True
        for i in range(n): # ! 현재 위치로부터 방문 안했는지 확인
            nx,ny = store[i]
            if not visited[i]:
                if abs(x-nx) + abs(y-ny) <= 1000: # ! 맥주병 20개로 이동 가능한지
                    dq.append((nx,ny))
                    visited[i] = True
    else:
        return False


T = int(input())
for t in range(1,T+1):
    n = int(input())
    start = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))

    visited = [False] * (n+2)
    flag = BFS(start[0], start[1])

    if flag:
        print("happy")
    else:
        print("sad")