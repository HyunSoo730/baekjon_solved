from collections import deque
def solution(n, computers):
    # 2차원 인접 리스트. 네트워크 개수 구하기
    # A-B 연결, B-C 연결 -> A,B,C 서로 연결
    
    visited = [False] * n
    cnt = 0
    def bfs(start):
        dq = deque()
        dq.append(start) # 시작노드
        visited[start] = True
        
        while dq:
            now = dq.popleft()
            for node in range(n):
                if not visited[node] and computers[now][node] == 1:
                    visited[node] = True
                    dq.append(node)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(cnt)
    return cnt