import sys
from collections import deque

n,m = map(int, input().split())
res = []
def dfs(L):
    if L == m: # m개 뽑음. 종료조건
        print(*res)
    else:
        for i in range(1,n+1):
            res.append(i)
            dfs(L+1)
            res.pop()
dfs(0)