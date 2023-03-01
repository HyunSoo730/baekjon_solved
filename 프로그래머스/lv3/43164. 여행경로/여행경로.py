from collections import defaultdict
def solution(tickets):
    n = len(tickets)
    data = tickets
    g = defaultdict(list) #노드값이 문자열일 경우 defaultdict 사용하자
    ch = defaultdict(list)
    for i in range(n):
        a,b = data[i][0], data[i][1]
        g[a].append(b)
        ch[a].append(0)
        #방향성 존재
        
    for x in g.values():
        x.sort()
    
    res = ["ICN"]
    result = []
    def DFS(L, now):
        if L == n + 1: #경로 모두 탐색. 종료조건
            result.append(res[:])
            return 
        else:
            for i in range(len(g[now])): #경로 여러개일 수도 있으니
                if ch[now][i] == 0:
                    ch[now][i] = 1 #방문 처리
                    res.append(g[now][i])
                    DFS(L+1, g[now][i])
                    ch[now][i] = 0
                    res.pop()  #이 문제는 딱 하나의 경로만을 찾으면 되므로 백트랙킹 시 원상복구 안시켜야 더 빨라.
                    #왜냐하면 위에서 이미 오름차순으로 정렬을 해준 상태에서 DFS를 시작하기 떄문.
                
    DFS(1, "ICN")
    print(result[0])
    return result[0] #한개가 저장되지만 첫번째꺼 리턴해줘야 함.
                
                
                
                
                
                
                
                
        