import sys
from collections import deque


n,k = map(int, input().split())

dis = [0] * 100001
ch = [0] * 100001
def bfs(v):
    ch[v] = 1 # 방문처리
    dq = deque()
    dq.append(v)

    while dq:
        now = dq.popleft()
        if now == k:
            break
        for nv in (now-1, now+1, now*2):
            if 0<=nv<100001 and ch[nv] == 0:
                ch[nv] = 1
                dq.append(nv)
                dis[nv] = dis[now] + 1

bfs(n)
print(dis[k])
