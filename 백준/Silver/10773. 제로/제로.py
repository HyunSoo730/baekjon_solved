import sys


k = int(input())
data = []
for _ in range(k):
    temp = int(input())
    if temp == 0:
        data.pop()
    else:
        data.append(temp)

print(sum(data))








