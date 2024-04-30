import sys

# n개의 센서, k개의 집중국
# n개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 함.
# 각 집중국의 수신 가능 영역의 길이의 합을 최소화.

# 그리디적으로 딱 센서가 위치한 곳에 일단 집중국을 놔야 한다.

n = int(input())
k = int(input())
data = list(map(int, input().split()))
if k >= n:
    print(0) # 모두 커버 가능하므로
else:
    data.sort()
    sense_length = [0] * n
    for i in range(1,n):
        sense_length[i] = data[i] - data[i-1]
    sense_length.sort(reverse = True)
    # print(sense_length)
    print(sum(sense_length[k-1:]))