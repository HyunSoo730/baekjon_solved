import sys
input = sys.stdin.readline
n = int(input())

data = [0] * n
cnt = 0
visited = [False] * n
def DFS(L):
    global cnt
    if L == n: # 끝까지 도달-> 종료조건
        cnt += 1
    else: # 현재 열에 공격을 받지 않을 행에 퀸을 놓어야 함
        for row in range(n): # 행은 0~n-1에 놓아야 하니까
            if visited[row]:
                continue
            data[L] = row # 현재 열에 row 행에 퀸 위치 (행, 열)
            if isValid(L):
                DFS(L+1)
def isValid(L):
    # 1. 같은 행인지 판단, 2. 같은 대각선인지 판단
    for col in range(L): # 이전 열까지 같은 행이 있는지 판단
        if data[L] == data[col] or abs(L - col) == abs(data[L] - data[col]):
            return False
    return True

DFS(0)
print(cnt)