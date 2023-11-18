import sys
from collections import deque

n,m = map(int, input().split())
visited = [0] * (n+1)
res = []
def dfs(L):
    if L == m: # m개 뽑음. 종료조건
        print(*res)
    else:
        for i in range(1,n+1):
            if visited[i] == 0:
                visited[i] = 1 # 방문처리 후
                res.append(i)
                dfs(L+1)
                res.pop()
                visited[i] = 0 # 백트랙킹 시 원상복구

dfs(0)