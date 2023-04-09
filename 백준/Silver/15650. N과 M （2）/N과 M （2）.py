import sys

n,m = map(int, input().split())
#중복없이 m개
#오름차순 --> 조합.

res = []
def DFS(L, start):
    if L == m: #모두 선택. 종료조건
        for x in res:
            print(x, end = " ")
        print()
    else:
        for i in range(start, n+1):
            res.append(i)
            DFS(L+1, i+1)
            res.pop()

DFS(0,1)