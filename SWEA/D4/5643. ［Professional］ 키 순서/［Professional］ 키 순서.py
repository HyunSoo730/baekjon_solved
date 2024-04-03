from collections import defaultdict, deque



def BFS(v, g):
    cnt = 0
    dq = deque()
    dq.append(v)
    visited = [False] * (n+1)
    while dq:
        node = dq.popleft()
        for x in g[node]:
            if not visited[x]:
                visited[x] = True
                dq.append(x)
                cnt += 1
    return cnt

T = int(input())
for t in range(1,T+1):
    n = int(input()) # 학생 수
    m = int(input()) #  키 비교 횟수
    g = defaultdict(list)
    reverse_g = defaultdict(list)
    for _ in range(m):
        a,b = map(int, input().split())
        g[b].append(a)
        reverse_g[a].append(b)

    # 본인을 통해 나가는 개수를 확인
    cnt = [0] * (n+1)
    reverse_cnt = [0] * (n+1)

    # 진출 차수에 대해서
    for v in range(1,n+1):
        cnt[v] = BFS(v,g)
    # 진입 차수에 대해서
    for v in range(1,n+1):
        reverse_cnt[v] = BFS(v,reverse_g)

    # print(f"진출차수 개수 = {cnt[1:]}")
    # print(f"진입차수 개수 = {reverse_cnt[1:]}")

    res = 0
    for v in range(1,n+1):
        if cnt[v] + reverse_cnt[v] == n-1:
            res += 1
    print(f"#{t} {res}")
