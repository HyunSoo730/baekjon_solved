import sys

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
# 두 팀으로 나뉘어야 한다.
# 1. 두 집합으로 나누기 3개만 선택

res = []
result = int(1e9)
def dfs(L,start):
    global result
    if L == n // 2: # 모두 선택
        sumA, sumB = 0,0
        check = set(res)
        for i in range(n):
            for j in range(n):
                if i in check and j in check:
                    sumA += data[i][j]
                elif i not in check and j not in check:
                    sumB += data[i][j]
        result = min(result, abs(sumA - sumB))
    else: # 계속 선택
        for i in range(start, n):
            res.append(i)
            dfs(L+1, i+1)
            res.pop()

dfs(0,0)
print(result)