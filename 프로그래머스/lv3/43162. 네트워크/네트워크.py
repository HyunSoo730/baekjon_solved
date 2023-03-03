from collections import deque
def solution(n, computers):
    data = computers
    print(data)
    #네트워크 개수 = 연결요소의 개수
    
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if data[i][j] == 1:
                    g[i].append(j)
    
    def BFS(v):
        ch[v] = 1
        dq = deque()
        dq.append(v)
        while dq:
            now = dq.popleft()
            for node in g[now]:
                if ch[node] == 0:
                    ch[node] = 1
                    dq.append(node)
        
    res = 0
    ch = [0] * n
    for i in range(n):
        if ch[i] == 0:
            BFS(i)
            res += 1
    return res            