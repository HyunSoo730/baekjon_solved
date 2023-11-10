
def dfs(L,sum):
    global cnt
    if sum > k:
        return # 가지치기
    if L == n: # 모두 확인. 종료조건
        if sum == k:
            cnt += 1
    else:
        dfs(L+1, sum + data[L]) # 현재 숫자 선택
        dfs(L+1, sum)


T = int(input())
for i in range(1,T+1):
    n,k = map(int, input().split())
    data = list(map(int, input().split())) # n 개
    cnt = 0
    dfs(0,0)
    print(f"#{i} {cnt}")
