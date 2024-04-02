def step1(g): # 있는 그대로의 상태에서 가능한지 확인
    result = True
    # 각 열들을 확인 -> 열 고정
    for y in range(m):
        if not result:
            break
        end = 0
        flag = False
        for x in range(n): # x를 차례대로 증가시키면서 확인
            cnt = 0 # 시작 개수 0
            while end < n and g[x][y] == g[end][y]: # 인덱스가 범위 내부에 있으면서 계속 같을 때까지
                cnt += 1
                end += 1
            if not flag and cnt >= k:
                flag = True
                break # 가능한 경우가 나오면 현재 열은 끝내도 돼
        if not flag:
            result = False
            break

    return result

def makeCell(x,g,val):
    for y in range(m):
        g[x][y] = val # 하나로 쭉 밀기

def DFS(L,start,g): # 매 순간 확인, 현재 g의 상황에서 가능한지, L은 현재 약품 투약 횟수
    global res
    if L > res:
        return # 가지치기
    if step1(g):  # 가능
        res = min(res, L) # 갱신
    else: # 현재 통과하지 못한다면 약품 투약 진행
        for i in range(start,n): # 조합으로 계속 진행 -> 현재 행에 대해
            for j in range(2): # 0 1 특성 2개 -> 약품 투약
                copy_g = [arr[:] for arr in g] # 복사
                makeCell(i, copy_g, j)
                # print(f"{i}번째 행 {j}로 약품 투입 후 결과")
                # print("=====================")
                # printBoard(copy_g)
                DFS(L+1, i+1, copy_g)

def printBoard(g):
    for i in range(n):
        for j in range(m):
            print(g[i][j] , end = " ")
        print()

T = int(input())
for t in range(1,T+1):
    n,m,k = map(int, input().split()) # 행, 열, 통과 기준
    g = [list(map(int, input().split())) for _ in range(n)]
    # 특성은 0 1 2가지
    result = step1(g) # 있는 그대로의 상태에서 기준 통과하는지 확인
    INF = int(1e9)
    res = INF
    if result:
        print(f"#{t} 0")
    else:
        DFS(0,0,g)
        if res == INF:
            print(f"#{t} {res}")
        else:
            print(f"#{t} {res}")
