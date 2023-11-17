import sys

from collections import deque

A,P = map(int, input().split())
ch = []
ch.append(A)

def makeNum(num, p):
    res = 0
    for x in str(num):
        t = int(x)
        res += pow(t, p)
    return res


while True:
    k = makeNum(ch[-1], P)
    if k in ch:
        break
    ch.append(k)

idx = ch.index(k)
print(idx)