import sys
import heapq

#최단거리. 그래프.
n,m,x = map(int, input().split()) #간선 노드 도착점
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    g[a].append((b,c))

INF = int(1e8)
def dijkstra(start):
    distance = [INF] * (n+1)
    q = [] #큐를 이용하여
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for node in g[now]:
            cost = dist + node[1]
            
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
                
    return distance

res = 0
for i in range(1,n+1):
    if i != x:
        toX = dijkstra(i)
        fromX = dijkstra(x)
        res = max(res, toX[x] + fromX[i])

print(res)
    
    
    
    
    
    
    
    
    
    
    
    

    
