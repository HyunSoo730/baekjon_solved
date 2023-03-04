from collections import defaultdict
def solution(tickets):
    data = tickets
    n = len(tickets)
    g = defaultdict(list)
    ch = defaultdict(list)
    for x,y in data:
        #x->y 인접 리스트 형식으로
        g[x].append(y)
        ch[x].append(0)
    #인접 리스트 완성
    #경로 알파벳 순
    for x in g.values():
        x.sort() #경로들 모두 정렬
    
    res = ["ICN"]
    result = []
    def DFS(L, now):
        if L == n+1: #종료조건
            result.append(res[:])
        else: #계속 돌아다녀야지
            for i in range(len(g[now])): #현재 노드의 인접 노드들의 개수만큼 확인
                if ch[now][i] == 0: #아직 방문 전
                    ch[now][i] = 1
                    res.append(g[now][i])
                    DFS(L+1, g[now][i]) #백트랙킹 시 원상복구
                    ch[now][i] = 0
                    res.pop()
    DFS(1, "ICN") 
    print(result[0])
    return result[0]
    