

def dfs(v, sum):
    global res
    if sum > res:  # 종점이 정해지지 않았기에 계속 비교해서 갱신..??
        res = sum
    else:
        for node in g[v]: # 현재 노드의 인접 노드들 방문
            if ch[node] == 0:
                ch[node] = 1  #방문 처리
                dfs(node, sum + 1) # 이제 해당 노드로 들어가서 다시 인접노드 있는지 탐색
                ch[node] = 0  # 백트랙킹 시 복구


T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split()) # 노드, 간선
    g = [[] for _ in range(n+1)] # 1번 인덱스부터 사용하기 위해.
    for _ in range(m):
        x,y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    # 1~n까지 모두 시작점으로 설정해서 진행해야함.
    res = 0 # 최장거리를 기록할 변수
    ch = [0] * (n+1) # 중복체크를 위한 배열
    for v in range(1,n+1):
        ch[v] = 1
        dfs(v, 1)
        ch[v] = 0

    print(f"#{t} {res}")


