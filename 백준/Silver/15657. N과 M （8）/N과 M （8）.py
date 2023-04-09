import sys

n,m = map(int, input().split())
data = list(map(int, input().split()))
res = []
data.sort()
def DFS(L, start):
    if L == m:
        for x in res:
            print(x,end = " ")
        print()
    else:
        for i in range(start,n):
            res.append(data[i])
            DFS(L+1, i)
            res.pop()
DFS(0,0)