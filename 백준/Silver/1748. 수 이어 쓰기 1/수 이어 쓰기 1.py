import sys

n = int(input())
k = len(str(n)) - 1
length = 0
i = 0
cnt = 1
d = 1
while i < k:  #n-1 자리수까지 구하고 n자리수는 따로.
    length += 9 * d * cnt
    d *= 10
    cnt += 1
    i += 1
length += (n - 10 ** k + 1) * (cnt)

print(length)
