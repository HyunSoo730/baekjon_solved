import sys

N, M = map(int, input().split())
data = []
for i in range(N):
    data.append(int(input()))

data.sort()   #이진 탐색이든 투 포인터 알고리즘이든 정렬될 상태에서 시작해야함 !!

#투 포인터 알고리즘
left = 0
right = 1

res = 2424242424
while left < N and right < N:
    temp = data[right] - data[left]

    if temp == M: #특수한 경우. 이것보다 작아질 수 없으니 무조건 답
        res = M
        break       
    elif temp > M: #답의 범위
        res = min(res, temp)   #기존 최솟값과 비교해서 더 최솟값을 찾아야지.
        left += 1
    else:
        right += 1

print(res)