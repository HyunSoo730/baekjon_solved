from collections import deque, defaultdict

# n개의 정점, m개의 간선
n,m,k,start = map(int, input().split()) # 최단거리가 k인 도시 번호
g = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b) # a->b 가능

INF = int(1e9)
dis = [INF] * (n+1)

def dijkstra(start):
    dq = deque()
    dq.append((start,0))
    dis[start] = 0

    while dq:
        now, t = dq.popleft()
        for node in g[now]: # 인접 노드들 하나씩 확인
            if t + 1 < dis[node]:
                dis[node] = t + 1
                dq.append((node, t + 1))

dijkstra(start)
if dis.count(k) == 0:
    print(-1)
else:
    for i in range(1,n+1):
        if dis[i] == k:
            print(i)