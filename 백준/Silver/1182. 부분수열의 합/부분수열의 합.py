import sys

input = sys.stdin.readline
from collections import deque

n, s = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
def DFS(L,sum, check):
    global cnt
    if L == n:
        if sum == s:
            if check != 0:
                cnt += 1
    else:
        DFS(L+1, sum + data[L], check + 1)
        DFS(L+1, sum, check)

DFS(0,0,0)
print(cnt)