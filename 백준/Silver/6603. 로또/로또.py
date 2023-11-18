import sys

sys.setrecursionlimit(10 ** 5)



def dfs(L,start):
    if L == 7: # 6개 모두 선택.
        print(*res)
    else:
        for i in range(start, k+1):
            res.append(data[i])
            dfs(L+1, i+1)
            res.pop()



while True:
    k, *data = list(map(int, input().split()))
    data.insert(0,-1)
    if k == 0:
        break
    n = len(data)
    res = []
    ch = [0] * (n+1)
    dfs(1,1)
    print()
