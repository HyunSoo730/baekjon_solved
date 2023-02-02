import sys



#k개의 로프, w인 중량 각각의 로프에는 w/k만큼의 중량이 걸린다

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))


data.sort(reverse = True)
res = 0 #최대 무게

for i in range(N):
    if res < data[i] * (i+1):
        res = data[i] * (i+1)

print(res)
