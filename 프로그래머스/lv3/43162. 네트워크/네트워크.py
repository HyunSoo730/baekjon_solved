def solution(n, computers):
    #n은 노드 개수 computers는 2차원 그래프
    g = computers
    ch = [0] * n
    
    def DFS(v):
        ch[v] = 1
        for i in range(n):
            if g[v][i] == 1 and ch[i] == 0:
                DFS(i)
    cnt = 0
    for i in range(n):
        if ch[i] == 0:
            DFS(i)
            cnt += 1
    return cnt