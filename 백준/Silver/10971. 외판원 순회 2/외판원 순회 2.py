import sys

n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n # 방문 체크 용

res = int(1e9) # 최소 비용
def dfs(start, v, sum_data): # start는 시작 노드 기억을 위해. v는 현재 노드, sum은 지금까지의 합 !
    global res
    if sum_data > res:
        return # 가지치기
    if sum(visited) == n: # 모두 방문했어.
        if g[v][start] != 0: # 다시 시작노드로 돌아가야한다 -> 이런 조건은 기록해놔야해.
            sum_data += g[v][start] # 시작노드로 가는 비용도 더했어야 !!! 
            if sum_data < res:
                res = sum_data
        return
    else: # 더 가야해
        for i in range(n):
            if visited[i] == 0 and g[v][i] > 0: # 방문하지 않았으면서 갈 수 있어야해
                visited[i] = 1
                dfs(start, i, sum_data + g[v][i])
                visited[i] = 0 # 백트랙킹 시 원상 복구

for i in range(n):
    visited = [0] * n # 계속 만들어줘야지
    visited[i] = 1 # 현재 노드가 시작점이니 방문처리 후에
    dfs(i,i,0)
print(res)
