import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
m = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int ,input().split()))

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: #작은 것이 부모로 설정
        parent[b] = a
    else:
        parent[a] = b
    

for i in range(n):
    for j in range(n):
        if g[i][j] == 1: #연결되어 있다면. 같은 집합으로 분류
            union_parent(i+1,j+1)

v = plan[0]
for i in plan:
    if parent[i] != parent[v]:  #모두 부모가 같아야 하므로 시작노드를 기준으로 판단하면 됨.
        print("NO")
        break
else:
    print("YES")