import sys


data = list(map(int, input()))
data.sort(reverse = True)
res = 0
for i in range(len(data)):
    res = res * 10 + data[i]

if res % 10 != 0 or res % 3 != 0:
    print(-1)
else:
    print(res)

