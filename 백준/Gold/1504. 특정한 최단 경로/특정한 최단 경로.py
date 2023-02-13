import sys
import heapq
input = sys.stdin.readline

n,e = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    g[a].append((b,c))
    g[b].append((a,c))
# (행선지, 가중치)
v1,v2 = map(int, input().split())

#1 v1 v2 N
#1 v2 v1 N
INF = 242424242424
def ddd(start, end):
    dis = [INF] * (n+1)
    dis[start] = 0 #시작
    hq = [(0,start)] #거리, 현재노드
    while hq:
        length, now = heapq.heappop(hq)
        if length > dis[now]: #최단거리니까
            continue
        for x, val in g[now]: 
            if dis[x] > dis[now] + val: #최단거리 갱신
                dis[x] = dis[now] + val
                heapq.heappush(hq, (dis[x], x))
    return dis[end]

v1_p = ddd(1,v1) + ddd(v1,v2) + ddd(v2,n)
v2_p = ddd(1,v2) + ddd(v2,v1) + ddd(v1,n)

res = min(v1_p, v2_p)
if res >= INF:
    print(-1)
else:
    print(res)
    