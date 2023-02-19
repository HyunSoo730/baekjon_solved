import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#유니온 파인드
n,m = map(int, input().split()) #노드, 간선(연산)
#0은 합집합 연산, 1은 찾기 연산
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

cycle = False #사이클 발생 여부

#특정 원소가 속한 집합(부모)을 찾기(Find)
def find_parent(x): #현재 노드에 대한 부모 찾기.
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기(합집합)
def union_parent(a,b): 
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0: #합집합
        union_parent(a,b)
    elif oper == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
