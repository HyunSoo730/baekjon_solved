import sys

n = int(input())

ch = [0] * (n+1)
res = []
def dfs(L):
    if L == n+1:
        print(*res)
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                ch[i] = 1
                res.append(i)
                dfs(L+1)
                ch[i] = 0
                res.pop()

dfs(1)