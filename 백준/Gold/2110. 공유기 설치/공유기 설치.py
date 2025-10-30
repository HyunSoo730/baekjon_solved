import sys

# 공유기 C개 설치. 최대한 많은 곳에서 와이파이 사용
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치
# 즉, 가장 인접한 두 공유기 사이의 거리를 최대로 하기 (최댓값)
# 인접한 두 공유기 사이의 거리 X이상으로 C개 이상 설치 가능해 ?


n,c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
left, right = 1, max(data) - min(data) + 1

def is_possible(length): # length 라는 길이로 공유기 C개 이상 설치 가능해 ?
    cnt = 1
    now = data[0] # 가장 첫번째에 설치해야 많이 설치 가능 (자명한 사실)
    for i in range(1,n):
        if data[i] - now >= length: # 설치
            cnt += 1
            now = data[i]
    return cnt >= c

while left < right:
    mid = (left + right) // 2 # 두 공유기 사이 거리
    if is_possible(mid): # 가능한가 ?
        left = mid + 1
    else:
        right = mid
print(left - 1)
