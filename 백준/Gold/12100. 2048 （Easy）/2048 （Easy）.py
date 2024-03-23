import sys

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

def move(g): # ! 해당 보드 왼쪽으로 밀기
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        flag = False # ! 연속 갱신 x -> 이전에 갱신이 있었는지 없었는지 확인하기 위해
        pos = -1 # ! 현재 조작 위치 (타겟점)
        for j in range(n):
            if g[i][j] == 0: continue # 값이 없으면 무시
            if flag == True and g[i][j] == temp[i][pos]: # ! 한번 값이 옮겨졌었고(flag == True) and 내가 지금 옮기려는 값과 지도에 옮겨져 있는 값이 같으면 업데이트
                flag = False # ! 값이 합쳐졌다는 소리
                temp[i][pos] *= 2
            else:
                pos += 1
                temp[i][pos] = g[i][j] # ! 아니라면 값만 복사
                flag = True
    return temp


def rotate_90(g):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1] = g[i][j]
    return temp

MAX_VAL = -int(1e9)
def DFS(L, g):
    global MAX_VAL
    if L == 5:
        maxData = 0
        for i in range(n):
            temp = max(g[i])
            maxData = max(maxData, temp)
        MAX_VAL = max(MAX_VAL, maxData)
    else:
        for i in range(4):
            temp_g = move(g)
            DFS(L+1, temp_g)
            g = rotate_90(g)

DFS(0,g)
print(MAX_VAL)