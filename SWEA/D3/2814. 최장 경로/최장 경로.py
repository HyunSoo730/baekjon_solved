

def dfs(v, sum): # 현재 g에서 최장거리 구하기.
    global res
    if sum > res: # 먼저 최댓값을 넘었는지 확인.
        res = sum
    else:
        for node in g[v]: # 인접노드들 하나씩 확인
            if ch[node] == 0: # 아직 방문 전
                ch[node] = 1
                dfs(node, sum + 1)
                ch[node] = 0 # 백트랙킹 시 반환



T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    res = 0
    for _ in range(m):
        x,y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    ch = [0] * (n+1)
    for i in range(1,n+1):
        ch[i] = 1
        dfs(i, 1)
        ch[i] = 0
    print(f"#{t} {res}")
