import sys

n,m = map(int, input().split())
data = list(map(int ,input().split()))
data.sort()

res = []
ch = [0] * n
def DFS(L):
    if L == m:
        for x in res:
            print(x, end = " ")
        print()
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res.append(data[i])
                DFS(L + 1)
                res.pop()
                ch[i] = 0

DFS(0)