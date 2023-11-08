import sys

import heapq

n,m,x = map(int, input().split())
g = [[] for _ in range(n+1)] #1번 인덱스부터 사용
for _ in range(m):
    a,b,c = map(int, input().split())
    g[a].append((b,c)) # a번 노드에서 b번 노드로 c만큼 든다

INF = int(1e9)
dis = [INF] * (n+1)
# 여기까지 기본세팅

# 다익스트라 알고리즘
def dijkstra(start): # 시작노드
    q = [] # 우선순위 큐 사용
    heapq.heappush(q, (0, start)) # 거리, 노드
    dis[start] = 0
    #출발 노드에 대한 세팅 끝

    while q:
        distance, now = heapq.heappop(q)
        if dis[now] < distance: # 저장된 값이 더 작으면 돌 이유가 없음
            continue

        #현재 노드와 인접노드들 확인
        for node in g[now]:
            cost = node[1] + distance
            # 현재 노드(now)를 거쳐서 node[0]으로 가는데 걸리는 비용 cost
            if cost < dis[node[0]]:
                dis[node[0]] = cost # 갱신
                heapq.heappush(q, (cost, node[0]))

res = [0] * (n+1)
for i in range(1,n+1):
    dis = [INF] * (n+1)
    dijkstra(i) # 시작 노드별로 기록 갱신
    disA = dis[x]
    dis = [INF] * (n+1)
    dijkstra(x)
    disB = dis[i]
    res[i] = disA + disB

max_val = max(res[1:])
print(max_val)