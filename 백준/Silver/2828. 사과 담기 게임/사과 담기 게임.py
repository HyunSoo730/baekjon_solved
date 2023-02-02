import sys


#바구니 이동거리의 최솟값.
N, M = map(int, input().split())    #바구니 시작위치 왼쪽 M칸, M칸 차지.
count = int(input()) #떨어지는 사과 개수
data = []
for _ in range(count):
    data.append(int(input()))  #사과가 떨어지는 위치

dis = 0
start = 1
end = M

for i in range(count):
    if data[i] >= start and data[i] <= M:  #안움직여도 사과 먹음
        continue
    elif data[i] < start:
        d = start - data[i]  #이동해야할 최소 거리
        dis += d
        start -= d
        end -= d
    elif data[i] > end:
        d = data[i] - end
        dis += d
        end += d
        start += d
print(dis)
