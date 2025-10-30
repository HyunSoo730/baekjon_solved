import sys

# N개의 수 1차월 배열
# 배열을 M개 이하의 구간으로 나누어서 구간의 점수의 최댓값을 최소로 구하기.
# # 구간의 점수 = 구간에 속한 수의 최댓값 - 최솟값
# 최적화 : 구간의 점수 최대의 최솟값 구하기
# 결정 : X라는 구간 점수 최댓값으로 M개 구간 이하로 나눌 수 있는가 ?

n,m = map(int, input().split())
data = list(map(int, input().split()))

left, right = 0, max(data) + 1

def is_possible(score): # score 라는 구간의 최댓값으로 M개 이하의 구간으로 만들 수 있는가 ?
    cnt = 1
    temp_max, temp_min = data[0], data[0]
    for i in range(n):
        temp_max = max(temp_max, data[i])
        temp_min = min(temp_min, data[i])
        if temp_max - temp_min > score: # 구간의 최댓값보다 커지면 이제 새로운 구간 추가
            cnt += 1
            temp_max = data[i]
            temp_min = data[i]
    return cnt <= m

while left < right:
    mid = (left + right) // 2
    if not is_possible(mid): # score 라는 점수로 구간의 최댓값 표현 못함 ?
        left = mid + 1
    else:
        right = mid

print(left)
