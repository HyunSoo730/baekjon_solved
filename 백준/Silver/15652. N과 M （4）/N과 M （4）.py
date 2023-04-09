import sys


n,m = map(int, input().split())
#오름차순. 중복 가능
res = []
def DFS(L, start):
    if L == m: #모두 선택. 종료조건,
        for x in res:
            print(x, end = " ")
        print()
    else:
        for i in range(start, n+1):
            res.append(i)
            DFS(L+1, i)
            res.pop()
DFS(0,1)