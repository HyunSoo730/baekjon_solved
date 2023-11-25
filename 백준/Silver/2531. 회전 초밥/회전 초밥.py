import sys

n,d,k,c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

res = 0
for s in range(n): # 시작지점 기준.
    dish = set()
    for i in range(k):  # 슬라이딩 윈도우 알고리즘 !!!
        dish.add(data[(s+i)%n])
    if c in dish:
        res = max(res, len(dish))
    else:
        res = max(res, len(dish) + 1)
print(res)


