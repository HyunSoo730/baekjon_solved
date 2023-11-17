import sys

from collections import deque

# dfs 한바퀴 돌면 하나의 연결요소! 즉 순열사이클
def dfs(v):
    ch[v] = 1
    node = data[v] # 다음 번 노드
    if ch[node] == 0:
        ch[node] = 1
        dfs(node)

T = int(input())
for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    data.insert(0,-1)
    ch = [0] * (n+1)
    cnt = 0
    for i in range(1,n+1):
        if ch[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)