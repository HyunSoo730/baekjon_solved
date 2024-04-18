from collections import deque


# 수빈이의 위치 X, 1초 후 X-1, X+1, 0초 후 2*X
n,k = map(int, input().split()) # n에서 k로 이동하는데 최단시간
INF = int(1e9)
dis = [INF] * 10000000 # 최대한 크게 일단

dq = deque()
dq.append((n, 0)) # 시작 위치, 현재 경로 시작

def isInner(x):
    if 0<=x<=100000: return True
    return False

while dq:
    now, t = dq.popleft()
    if now == k: # 도착점 찾음
        if t < dis[now]:
            dis[now] = t # 갱신
        continue # 도착점에서는 더 찾아나서면 안돼
    if isInner(now-1) and t + 1 < dis[now-1]:
        dis[now-1] = t + 1 # 갱신
        dq.append((now-1, t+1))
    if isInner(now+1) and t + 1 < dis[now+1]:
        dis[now+1] = t + 1
        dq.append((now+1, t+1))
    if isInner(now * 2) and t < dis[now*2]:
        dis[now*2] = t
        dq.append((now*2, t))

print(dis[k])