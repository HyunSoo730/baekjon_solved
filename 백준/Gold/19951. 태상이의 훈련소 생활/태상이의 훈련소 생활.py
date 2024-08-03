import sys

# 일렬로 이어진 N개의 칸. 각 칸마다 높이 존재
# 조교 M명, 각 조교 a~b칸까지 높이 k만큼 흙을 덮거나 파라고 지시.
# 최종 높이 미리 구해 한번에 일 수행

# N,M <= 100,000 -> N^2 안됨

n,m = map(int, input().split())
heights = list(map(int, input().split())) # 각 칸의 높이

status = [0] * (n+1)
for _ in range(m):
    a,b,k = map(int, input().split())
    a -= 1
    b -= 1
    status[a] += k
    status[b+1] -= k

# print(status)
res = [0] * (n+1)
for i in range(1,n):
    status[i] += status[i-1]

# print(status)
for i in range(n):
    heights[i] += status[i]
print(*heights)