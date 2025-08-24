import sys


# n개의 랜선 만들기
# 자체적으로 k개의 랜선 가지고 있음.
# 랜선을 모두 같은 길이 n개.
# 만들 수 있는 최대 랜선 길이 구하기
# 변수를 랜선 길이로 .

k,n = map(int, input().split())
data = []
for i in range(k):
    data.append(int(input()))
data.sort() # 일단 오름차순 정렬을 해야 이진탐색 가능

def can_make(length):
    cnt = 0
    for value in data:
        cnt += value // length
    return cnt >= n # 길이 length로 n개 이상 만들 수 있는지 확인

# 매개변수 탐색
left, right = 1, max(data) + 1
while left < right:
    mid = (left + right) // 2 # 가능한 랜선 길이
    if can_make(mid): # mid 길이로 n개 이상 가능 ?
        left = mid + 1 # 더 긴 길이 시도
    else:
        right = mid # 길이 줄이기
print(left-1)