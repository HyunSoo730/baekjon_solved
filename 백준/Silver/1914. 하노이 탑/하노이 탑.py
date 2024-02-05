import sys
from collections import deque


n = int(input())

def DFS(n, start, temp, end):
    if n==1:
        print(f"{start} {end}")
    else:
        DFS(n-1,start, end, temp)
        print(f"{start} {end}")
        DFS(n-1, temp, start, end)

print(pow(2, n) -1)
if n <= 20:
    DFS(n,1,2,3)