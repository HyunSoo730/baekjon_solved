import sys
from collections import deque
import copy
input = sys.stdin.readline

# 0의 개수

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

#0 빈칸, 1 벽 2 바이러스
#벽 3개 세워야함.
#벽 세우고 안전영역 개수 구해야함.

dx = [1,-1,0,0]
dy = [0,0,1,-1]

res = 0
def BFS(): #벽 3개를 만들면 이제 실행하는거야
    global res
    dq = deque()
    temp = copy.deepcopy(g)

    for i in range(n):
        for j in range(m):
            if g[i][j] == 2: #바이러스
                dq.append((i,j))
    
    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m: #경계선
                if temp[nx][ny] == 0: #빈칸인 경우 바이러스로 채워야지
                    temp[nx][ny] = 2 #방문처리라고 생각
                    dq.append((nx,ny))
    
    #전부 다 돌면서 바이러스 퍼트렸따면 이제 안전지대 개수
    cnt = 0
    for i in range(n):  
        cnt += temp[i].count(0) # 안전지대 계산
    res = max(res,cnt)


def wall(cnt): #벽을 3개 만들어야한다 즉 조합으로 빈칸 중에 3곳 뽑음
    if cnt == 3:
        BFS()
        return
    
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0: #선택
                g[i][j] = 1
                wall(cnt+1)
                g[i][j] = 0 #백트랙킹시 원상복구

wall(0)
print(res)