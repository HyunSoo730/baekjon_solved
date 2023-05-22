import sys

n,m = map(int, input().split())

g = [list(map(int, input())) for _ in range(n)]

res = 1
length = min(n,m)

def check(x,y,h):
    if 0<=x+h<n and 0<=y+h<m:
        if g[x][y] == g[x][y+h] and g[x][y] == g[x+h][y] and g[x][y] == g[x+h][y+h]:
            return True
        else:
            return False
    else:
        return False

for h in range(1,length + 1): #높이는 2~length 모두 둘러봄
    for x in range(n):
        for y in range(m):
            if check(x,y,h) == True:
                res = (h+1) ** 2

print(res)