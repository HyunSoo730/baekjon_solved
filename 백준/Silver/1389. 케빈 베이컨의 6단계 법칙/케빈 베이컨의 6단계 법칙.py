import sys

input = sys.stdin.readline
from collections import deque

#몇단계만에 만날지 계산
#최단거리
#최단거리를 가지는 사람 구하기

n,m = map(int ,input().split()) #노드, 간선
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def BFS(v):
    dq = deque()
    ch[v] = 1 #방문 처리
    dq.append(v) #노드, 거리
    while dq:
        now = dq.popleft() #현재 노드
        for x in g[now]: #현재 노드의 인접 노드
            if ch[x] == 0: #아직 방문 전
                ch[x] = 1 #
                dis[x] = dis[now] + 1 #x까지 가는 최단거리는 now까지의 거리 + 1
                dq.append(x)
                # print("length : " , length)
        # print(dis)
res = []
for i in range(1,n+1):
    ch = [0] * (n+1)
    dis = [0] * (n+1)   #체크 변수와 dis 최단거리 리스트를 따로 만들어도 될까..? 하나로 통합해서 사용하는거 연습해야 할듯?
    BFS(i)
    res.append(sum(dis))

r_idx = res.index(min(res))
print(r_idx + 1)







    