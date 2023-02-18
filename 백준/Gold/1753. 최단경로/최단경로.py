import sys

input = sys.stdin.readline
import heapq

v,e = map(int, input().split()) #노드, 간선
start = int(input()) #시작정점
g = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    g[a].append((b,c))

INF = int(1e8)
distance = [INF] * (v+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))  #시작점은 당연히 비용 0
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for node in g[now]: #현재 노드의 인접노드들 중
            cost = dist + node[1]  #현재노드(now)에서 인접노드 node까지의 비용 node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)
for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    
    
    
    
    
    
    
    
    
    

    
