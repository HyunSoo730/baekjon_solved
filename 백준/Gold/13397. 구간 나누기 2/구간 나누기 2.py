import sys

# N개의 수로 이루어진 1차원 배열.
# 이 배열을 M개 이하의 구간으로 나누어서 구간의 점수의 최댓값을 최소로 하고자.
# 1. 하나의 구간은 하나 이상의 연속된 수들로 이루어져 있음 (순서가 바뀌면 안됨)
# 2. 배열의 각 수는 모두 하나의 구간에 포함되어야 함.
# 2-1. 구간의 점수란, 구간에 속한 수의 최댓값과 최솟값의 차이
# 구간의 점수의 최댓값의 최솟값 구하기
# 최솟값 X일 때 각 구간에서의 조건 만족하는가 ? -> 결정 문제로 변환

n,m = map(int, input().split())
data = list(map(int, input().split()))

left, right = 0, max(data) - min(data) + 1

def is_possible(score):
    cnt = 1 # 구간 개수 (1부터 구간 시작)
    max_score = data[0]
    min_score = data[0]
    for i in range(1,n):
        temp_min = min(min_score, data[i])
        temp_max = max(max_score, data[i])

        if temp_max - temp_min <= score:
            min_score = temp_min
            max_score = temp_max
        else:
            cnt += 1
            min_score = data[i]
            max_score = data[i]
    return cnt <= m
while left < right:
    mid = (left + right) // 2 # 해당 최솟값으로 M개 이하의 각 구간 모두 만족 ?

    if not is_possible(mid): # 불가능하다면 -> 점수 올려야지
        left = mid + 1
    else:
        right = mid

print(left)
