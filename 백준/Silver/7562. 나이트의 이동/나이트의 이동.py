import sys
from collections import deque
input = sys.stdin.readline

#최소 몇번만에 이동 → 최단거리 생각
dx = [-1,1,-1,1,-2,2,-2,2]
dy = [-2,-2,2,2,-1,-1,1,1]

def BFS(a,b, c,d):
    dq = deque()
    dq.append((a,b))
    ch[a][b] = 1 # 시작점 방문
    while dq:
        x,y = dq.popleft() 
        if x == c and y == d: 
            break
        for i in range(8):
            nx =  x + dx[i]
            ny =  y + dy[i]
            
            if 0<=nx<l and 0<=ny<l: #경계선
                if ch[nx][ny] == 0:
                    ch[nx][ny] = 1
                    dis[nx][ny] = dis[x][y] + 1
                    dq.append((nx,ny))
        

T = int(input())
for _ in range(T):
    l = int(input()) #체스판 한 변 길이
    x,y = map(int, input().split()) #나이트 현재 있는 칸
    ax,ay = map(int, input().split()) #이동하려고 하는 칸
    
    ch = [[0] * l for _ in range(l)]
    dis = [[0] * l for _ in range(l)]
    BFS(x,y,ax,ay)
    print(dis[ax][ay])
    
    
    

