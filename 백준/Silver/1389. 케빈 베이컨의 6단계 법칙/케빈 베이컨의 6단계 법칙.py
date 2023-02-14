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
    dq.append((v,1)) #노드, 거리
    dis = 0
    while dq:
        now, length = dq.popleft() #현재 노드
        for x in g[now]: #현재 노드의 인접 노드
            if ch[x] == 0: #아직 방문 전
                ch[x] = 1 #
                dis += length
                dq.append((x,length+1))
                # print("length : " , length)
        # print(dis)
    return dis
res = []
for i in range(1,n+1):
    ch = [0] * (n+1)
    dis = BFS(i)
    res.append(dis)

r_idx = res.index(min(res))
print(r_idx + 1)







    