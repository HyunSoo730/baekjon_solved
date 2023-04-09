import sys
from collections import deque


n,m = map(int, input().split())
#중복없이 m개 선택 : 순열
res = []
ch = [0] * (n+1)
def DFS(L):
    if L == m: #모두 선택. 종료조건
        for x in res:
            print(x, end = " ")
        print()
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                ch[i] = 1
                res.append(i)
                DFS(L + 1)
                ch[i] = 0
                res.pop()  # 백트랙킹 시 원상복구


DFS(0)