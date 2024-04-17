import sys
# n개의 세로선, m개의 가로선, 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수를 H개, 모든 세로선이 같은 위치를 갖는다
# 가로선은 인접한 두 세로선 연결. 두 가로선이 연속하거나 접하면 안된다.
# 사다리 게임은 각각의 세로선마다 게임 진행, 세로선의 가장 위에서부터 아래 방향으로 내려감.
# 사다리에 가로선을 추가해서 사다리게임의 결과 조작.
# i번 세로선 -> i번이 나오도록 추가해야 하는 가로선 개수의 최솟값.

# 각 세로선마다 최대 가로선 H개.
# 각각의 위치마다 조합처럼 해보는 수밖에 ?

def check(): # 현재 상황에서 가능한지 확인
    for y in range(1,n+1): # 열 고정
        pos = y # 탐색 시작 열
        for x in range(1,h+1):
            if g[x][pos] == 1:
                pos += 1 # 오른쪽으로 이동
            elif g[x][pos-1] == 1:
                pos -= 1 # 왼쪽으로
        if pos != y: # 본인 위치로 와야만 함
            return False
    else:
        return True

def DFS(L, x,y): # 현재 레벨, 지금부터 시작하는 좌표.
    global res
    if L >= res: # 최적의 결과라서 더 나갈 필요가 없음
        return # 가지치기
    if check(): # 가능한 경우 -> 매순간 가능한지 체크
        res = min(res, L)
        return
    if L == 3: # 최대 3번 그을 수 있음
        return # 끝내야함.
    else:
        for i in range(x, h+1): # 행만큼
            for j in range(y,n): # 열 -1만큼
                if g[i][j] == 0 and g[i][j-1] == 0 and g[i][j+1] == 0: # 현재 위치 사다리 없으면서 양 옆 없어야 함.
                    g[i][j] = 1
                    DFS(L+1, i, j) # (i,,j)에 사다리 설치했으니
                    g[i][j] = 0 # 백트랙킹 시 원상복구
            y = 1

# 세로선 개수 n, 가로선 개수 m, 세로선마다 가로선 놓을 수 있는 위치 개수 H
n,m,h = map(int, input().split())
g = [[0] * (n+1) for _ in range(h+1)] # 1번 인덱스부터 사용 사다리 맵 초기화

for _ in range(m):
    a,b = map(int, input().split())
    g[a][b] = 1
res = int(1e9)

DFS(0,1,1)
if res == int(1e9):
    print(-1)
else:
    print(res)