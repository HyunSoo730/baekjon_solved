import sys



N, M = map(int, input().split())
pack = []
one = []

for i in range(M):
    p, o = map(int, input().split())
    pack.append(p)
    one.append(o)

#N개를 다시 사야함
pack.sort()
one.sort()    # 둘다 오름차순으로 ..
min_pack = pack[0]
min_one = one[0]

res = 0
if min_one * 6 < min_pack:
    res = min_one * N 
else:
    res += min_pack * (N//6)
    #패키지 구매 이후에 남은 낱개 비교
    if min_one * (N%6) < min_pack:
        res += min_one * (N%6)
    else:
        res += min_pack

print(res)