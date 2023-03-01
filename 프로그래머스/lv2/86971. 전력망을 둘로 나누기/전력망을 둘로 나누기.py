import itertools
def solution(n, wires):
    
    #노드 개수  n, 연결 정보
    data = wires
    m = len(wires)
        
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    def union_parent(a,b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
   #모든 노드 연결 완료
    
    res = 242424224 #최솟값
    #m개의 연결 중 한개 선택해서 최댓값 찾기
    for i in range(m):
        #i번째 인덱스 연결 끊었다고 가정
        parent = [i for i in range(n+1)]
        for idx, val in enumerate(data):
            if idx == i:
                continue
            a = val[0]
            b = val[1]
            union_parent(a,b)
        
        for i in range(1,n+1):
            i = find_parent(i)
        v = parent[1]
        cntA=cntB=0
        for i in range(1,n+1):
            if parent[i] == v:
                cntA += 1
            else:
                cntB += 1
        temp = abs(cntA-cntB)
        res = min(temp, res)
        print(parent)
    print(res)
    return res
            
    
