from collections import defaultdict

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = defaultdict()
direction["U"] = 0
direction["R"] = 1
direction["D"] = 2
direction["L"] = 3
cnt = 0
x,y = 0,0
nx,ny = 0,0

def solution(dirs):
    def isInner(x, y):
        if -5 <= x <= 5 and -5 <= y <= 5:
            return True
        return False

    visited = set()
    def 이동(dir):
        global cnt, x, y
        d = direction[dir]
        nx = x + dx[d]
        ny = y + dy[d]
        if not isInner(nx, ny):
            return
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx,ny,x,y))
            cnt += 1
        x, y = nx, ny

    for dir in dirs:
        이동(dir)
    # print(cnt)
    return cnt