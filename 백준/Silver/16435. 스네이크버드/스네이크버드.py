N, L = map(int, input().split())
height = list(map(int, input().split()))

height.sort()
for x in height:
    if L >= x:
        L += 1

print(L)