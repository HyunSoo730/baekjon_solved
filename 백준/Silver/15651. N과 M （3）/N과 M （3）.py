import sys

n,m = map(int, input().split())
#중복 가능.
#중복 순열

res = []
def DFS(L):
    if L == m: #모두 선택. 종료조건
        for x in res:
            print(x, end = " ")
        print()
    else:
        for i in range(1,n+1):
            res.append(i)
            DFS(L+1)
            res.pop()
DFS(0)