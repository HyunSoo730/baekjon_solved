
N = int(input())

res = 0

while N > 0:
    if N % 5 == 0:
        res += N // 5
        break
    N -= 3
    res += 1

if N < 0:
    print(-1)
else:
    print(res)

