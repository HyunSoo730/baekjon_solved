import sys

n,m = map(int, input().split())
data = list(map(int, input().split()))
res = []
data.sort()
def DFS(L):
    if L == m:
        for x in res:
            print(x,end = " ")
        print()
    else:
        for i in range(n):
            res.append(data[i])
            DFS(L+1)
            res.pop()
DFS(0)