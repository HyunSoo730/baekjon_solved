import sys

# 집 N개가 수직선 위에 존재.
# 공유기 C개 설치 예정. 최대한 많은 곳에서 와이파이를 사용하고자 함.
# 인접한 두 공유기 사이의 거리를 가능한 크게 설치.
# C개의 공유기를 N개의 집에 설치하여 가장 인접한 두 공유기 사이의 거리를 최대로 하기.
# 두 공유기 사이 거리 최대... 결정 문제
# 두 공유기 사이 거리 늘어날 수록 공유기 설치 개수는 줄어든다.
n,c = map(int, input().split())
data = []
for _ in range(n):
    temp = int(input())
    data.append(temp)

data.sort() # 이 문제는 정렬이 필요
def is_possible(length):
    cnt = 1 # 시작 지점에 공유기를 박아야 인접한 두 공유기 사이의 거리를 가능한 크게 할 수 있다 (자명한 사실)
    now = data[0] # 이전 공유기 위치 저장.
    for i in range(1,n):
        if data[i] - now >= length: # 설치해야함
            cnt += 1
            now = data[i]
    return cnt >= c
left, right = 1, data[-1] - data[0] + 1 # 두 공유기 사이 거리 최대거리는 양 끝 집 사이 거리 !.. 최악의 경우 !
while left < right:
    mid = (left + right) // 2 # 두 공유기 사이 거리.
    if is_possible(mid): # c개 설치 가능
        left = mid + 1
    else:
        right = mid
print(left -1)