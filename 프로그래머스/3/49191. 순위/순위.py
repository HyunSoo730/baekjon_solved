def solution(n, results):
    # 1~n번까지 번호
    """
    플로이드 워셜 적용
    i>k, k>j라면 i>j 성립
    """
    INF = int(1e9)
    g = [[INF] * (n+1) for _ in range(n+1)]
    
    for a,b in results:
        g[a][b] = 1 # a가 b를 이김
    
    # 플로이드-워셜 : 간접 승패 추론
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                # i > k 이고, k>j 이면 i>j 임
                if g[i][k] == 1 and g[k][j] == 1:
                    g[i][j] = 1
                    
    # 순위 여부 확정 (정확히 순위를 매길 수 있는 선수)
    res = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            if i != j:
                # i > j or j > i 승패 명확하면
                if g[i][j] == 1 or g[j][i] == 1:
                    cnt += 1
        if cnt == n - 1:  # 모든 선수와 승패가 결정됨 : 명확
            res += 1
    
    print(res)
        
    return res