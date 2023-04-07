import sys
import copy


n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)] #nxm

dx = [-1,0,1,0]
dy = [0,1,0,-1] #북 동 남 서
#ㅗ 제외 모두 탐색 가능
res = -2424242424
temp = []
def DFS(L, x, y, sum):
    global res
    if L == 3: #3개 선택 완료. 종료조건
        # print(temp)
        res = max(res, sum)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m: #경계선 안에
                if ch[nx][ny] == 0: #방문 안했다면
                    ch[nx][ny] = 1
                    DFS(L+1, nx,ny,sum + g[nx][ny])
                    ch[nx][ny] = 0 #백트랙킹 시 원상복구

ch = [[0] * m for _ in range(n)] #방문 체크를 위한 리스트

#이제 ㅗ자형 따로 구해야함
def cal(x,y):
    global res
    for i in range(4): #시작 방향설정.
        sum_data = g[x][y] #초기값 설정
        for k in range(3):
            d = (i+k) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0<=nx<n and 0<=ny<m):
                break
            sum_data += g[nx][ny]
        res = max(res, sum_data)


for i in range(n):
    for j in range(m):
        ch[i][j] = 1 #시작 지점 역시 방문처리하고 들어가야해
        DFS(0, i,j,g[i][j])
        ch[i][j] = 0
        cal(i,j)


print(res)