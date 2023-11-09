
# 점수, 칼로리
# 점수의 합. 같은 재료 한번
# 냅색 알고리즘 ? x -> 너무 큼
def dfs(L,sum, lim):
    global res
    if L == n: # 모두 돌았음 종료조건
        if lim > limit:
            return
        if sum > res:
            res = sum
    else:   # 현재 재료 먹냐 안 먹냐.
        if lim + data[L][1] <= limit:
            dfs(L+1, sum + data[L][0], lim + data[L][1])
        dfs(L+1, sum, lim)


T = int(input())
for t in range(T):
    n,limit = map(int, input().split())
    data = []
    for _ in range(n):
        a,b = map(int, input().split()) # 점수, 칼로리
        data.append((a,b)) # 점수, 칼로리
    res = 0
    dfs(0,0,0)
    print(f"#{t+1} {res}")

