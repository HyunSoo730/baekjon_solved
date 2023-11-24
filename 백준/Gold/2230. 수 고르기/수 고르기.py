import sys

n,m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
res = int(2e9) # 차이가 m 이상이면서 가장 작은 경우를 기록하기 위해

e = 0
for s in range(n):
    # 차이가 m보다 작으면 끝점을 증가시켜서 차이를 키워
    while e < n and data[e] - data[s] < m:
        e += 1
    if e < n and data[e] - data[s] >= m: # 반복문 탈출 시 끝점과 시작점 값 차이가 m 이상.
        res = min(res, data[e] - data[s])
    else:
        break
print(res)