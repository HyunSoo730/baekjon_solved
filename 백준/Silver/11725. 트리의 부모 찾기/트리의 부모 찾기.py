import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
ch = [0] * (n+1) #0번 인덱스 사용안함
parent = [0] * (n+1) #부모노드 저장
g = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

#무방향 그래프 설정 끝.  노드 개수만큼 선언하기에는 너무 크다... 그렇기에 
#그래프의 연결 상태만 표시한다면 메모리의 사용을 크게 줄일 수 있다.

def DFS(v):
    ch[v] = 1 #방문 처리 후에
    for x in g[v]: #현재 노드의 인접 노드들 하나씩 꺼내서..
        if ch[x] == 0: #방문 전이라면
            parent[x] = v #현재 인접 노드의 부모는 v이다. 어차피 방문한거면 다시 재방문 안하잖아 !
            DFS(x)

DFS(1) 
for i in range(2,n+1):
    print(parent[i])