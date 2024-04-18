import heapq
from collections import defaultdict


# n개의 정점, m개의 간선
n = int(input())
m = int(input())
g = defaultdict(list)

for _ in range(m):
    a,b,c = map(int, input().split())
    g[a].append((c,b)) # a->b 비용 c
s,e = map(int, input().split()) # 시작점, 도착점

INF = int(1e9)
dis = [INF] * (n+1) # 1번 인덱스부터

def dijkstra(start): # 시작 정점 기준
    pq = [] # 우선순위큐처럼 쓰기 위해
    dis[start] = 0 # 시작점 0으로
    heapq.heappush(pq, (0,start)) #  시작점 세팅

    while pq:
        distance,now = heapq.heappop(pq) # 거리 가장 짧은 거 꺼내서
        if dis[now] < distance: # 이미 갱신된 곳
            continue
        # 갱신 시켜야 하는 곳이라면 진행
        for cost, node in g[now]: # 현재 정점 인접 확인
            if dis[now] + cost < dis[node]: # 기존값보다 더 갱신 가능.
                dis[node] = dis[now] + cost
                heapq.heappush(pq, (dis[node], node)) # 갱신한 값 기준 다시 탐색해야지

dijkstra(s)
print(dis[e])