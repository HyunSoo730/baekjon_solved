import sys

n,m = map(int, input().split())
data = list(map(int, input().split()))
res = []
data.sort()
ch = [0] * n
def DFS(L):
    if L == m:
        for x in res:
            print(x, end = " " )
        print()
    else:
        rem = 0 #정렬했기 때문에 이전과만 비교해주면 됨.
        for i in range(n):
            if rem != data[i]:
                res.append(data[i])
                rem = data[i]
                DFS(L+1)
                res.pop()
DFS(0)