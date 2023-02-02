import sys

N = int(input())
data = list(map(int, input().split()))
S = int(input())

# 연속된 두개의 원소만 교환 가능
for i in range(N):
    max_num = max(data[i:min(N, i+S+1)])
    idx = data.index(max_num)  #해당 최댓값..

    for j in range(idx, i, -1):
        data[j], data[j-1] = data[j-1], data[j]

    #이후에 S값 갱신
    S -= idx -i
    if S == 0:
        break

for x in data:
    print(x, end = " " )
