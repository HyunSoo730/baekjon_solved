from collections import defaultdict
def solution(tickets):
    n = len(tickets)
    data =tickets
    
    g = defaultdict(list)
    ch = defaultdict(list) #중복 체크도 딕셔너리로
    
    for i in range(n):
        k, v = data[i][0], data[i][1]
        g[k].append(v) #해당 딕셔너리에 k값에 대응하는 value가 비어있으면 빈 리스트 만들고 v추가.
        ch[k].append(0)
    #알파벳 순이니까 value를 기준으로 오름차순
    for k,v in g.items():
        v.sort()
    
    res = ["ICN"]
    def DFS(L, now):
        if L == n+1: #전부 다 확인. 종료조건
            tmp = []
            for x in res:
                tmp.append(x)
            result.append(tmp)
        else: #계속 가야함
            for i in range(len(g[now])):
                if ch[now][i] == 0: #아직 해당 문자열 노드를 아직 방문하지 않았다면
                    ch[now][i] = 1
                    node = g[now][i] #인접노드
                    res.append(node)
                    DFS(L+1, node)
                    res.pop()
                    ch[now][i] = 0
        
    result = []
    DFS(1,"ICN") 
    return result[0]
    
        
    
            