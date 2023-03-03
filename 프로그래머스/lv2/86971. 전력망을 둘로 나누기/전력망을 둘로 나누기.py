from collections import deque
def solution(n, wires):
    
    #노드 개수  n, 연결 정보
    data = wires
    m = len(wires)
        
    g = [[] for _ in range(n+1)]
    def BFS(v):
        ch = [0] * (n+1)
        ch[v] = 1 #시작좌표 
        dq = deque()
        dq.append(v)
        
        cnt = 1
        while dq:
            now = dq.popleft()
            for node in g[now]: #현재 노드 인접노드들
                if ch[node] == 0: #방문 전
                    ch[node] = 1
                    cnt += 1
                    dq.append(node)
        return cnt
    
    for i in range(m):
        a,b = data[i][0], data[i][1]
        g[a].append(b)
        g[b].append(a)
    #그래프 전부 연결해놓고
    res = 24242424
    
    for i in range(m):
        #한번씩 연결 끊어야지
        a,b = data[i][0], data[i][1]
        g[a].remove(b)
        g[b].remove(a)
        
        cntA = BFS(a)
        cntB = BFS(b)
        temp = abs(cntA-cntB)
        res = min(res, temp)
        
        g[a].append(b)
        g[b].append(a) #다시 연결!
        
        
    # for i in range(m):
    #     g = [[] for _ in range(n+1)]
    #     for j in range(m):
    #         if i == j:
    #             continue #제외하는 간선
    #         #i번째 간선을 제외시킴.
    #         a,b = data[j][0], data[j][1]
    #         g[a].append(b)
    #         g[b].append(a)
    #     #해당 간선 제외하고 그래프 연결 완료
    #     #끊은 간선의 두 노드에서 연결요소 개수 가져와야함
    #     a = data[i][0]
    #     b = data[i][1]
    #     cntA = BFS(a)
    #     cntB = BFS(b)
    #     temp = abs(cntA-cntB)
    #     res = min(res, temp)
    
    
    print(res)
    return res
        
        
        
            
    
