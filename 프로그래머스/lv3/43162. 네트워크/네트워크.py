def DFS(v):
    global g
    global ch
    global N
    ch[v] = 1
    for i in range(N):
        if g[v][i] == 1 and ch[i] == 0:
            DFS(i)


def solution(n, computers):
    #n개의 노드, 연결상태 computers
    global g
    global ch
    global N
    N = n
    ch = [0] * n
    g = computers
    cnt = 0
    ch = [0] * n
    for i in range(n):
        if ch[i] == 0:
            DFS(i)
            cnt += 1
    return cnt
        
    
        