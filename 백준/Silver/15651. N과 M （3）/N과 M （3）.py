import sys


n,m = map(int, input().split())
#n개 중 m개 중복 순열

res = [0] * m #결과를 저장할 리스트

def DFS(L):
    if L == m: #종료 조건, m개 선택
        for x in res:
            print(x, end = " ")
        print()
    else: #계속 선택
        for i in range(1,n+1):
            res[L] = i
            DFS(L+1)

DFS(0)