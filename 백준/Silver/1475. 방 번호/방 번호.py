import sys

#한 세트0~9
#필요한 세트의 최솟값.
# 6 ,9 서로 교환 가능

n = input()
res = [0] * 10
for i in range(len(n)):
    temp = int(n[i])
    if temp == 6 or temp == 9:
        if res[6] <= res[9]:
            res[6] += 1
        else:
            res[9] += 1
        #이 부분이 핵심 더 적게 쓴 것을 써주면 됨
    else:
        res[temp] += 1

print(max(res)) #최댓값이 바로 필요한 세트 수