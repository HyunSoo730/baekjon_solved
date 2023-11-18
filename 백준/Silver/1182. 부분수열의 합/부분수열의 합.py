import sys
from collections import deque

n,s = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
res = []
def dfs(L, res):
    global cnt
    if L == n: # 모두 확인. 종료조건
        if sum(res) == s and len(res) != 0:
            cnt += 1
    else:
        dfs(L+1, res + [data[L]])
        dfs(L+1, res)
dfs(0,res)
print(cnt)
