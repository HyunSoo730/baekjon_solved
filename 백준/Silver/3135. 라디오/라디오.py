import sys


A, B = map(int, input().split())
#A->B로 갈 때 눌러야 하는 가장 적은 버튼 수를 구하기
N = int(input()) #N개의 미리 지정된 주파수 입력
data=  []
for _ in range(N):
    data.append(int(input()))

#N개의 데이터와 목적지의 차이가 가장 적은 곳으로 이동 후 현재위치에서 이동하는 것과 비교하여 움직이면 될듯
temp = abs(A-B)
min_cha = 242424242424
for i in range(N):
    if abs(data[i] - B) < min_cha:
        min_cha = abs(data[i] - B)
        idx = i

if temp <= min_cha:  #그냥 이동하는게 더 가까운 경우
    print(abs(A-B))   #횟수
else:
    print(abs(B - data[idx]) + 1)