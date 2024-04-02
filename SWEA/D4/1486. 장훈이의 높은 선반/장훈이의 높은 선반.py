
def DFS(L, length):
    global res
    if L == n: # 모든 인덱스 확인 종료조건
        if length >= B and length < res:
            res = length
    else:
        DFS(L+1, length + data[L]) # 현재 탑 추가
        DFS(L+1, length) # 현재 탑 추가하지 않음
T = int(input())
for t in range(1,T+1):
    n,B = map(int, input().split())
    data = list(map(int, input().split())) # 탑 각각의 높이
    # B이상인 것 중 가장 작아야함.
    res = int(1e9)
    DFS(0,0)

    print(f"#{t} {res-B}")
