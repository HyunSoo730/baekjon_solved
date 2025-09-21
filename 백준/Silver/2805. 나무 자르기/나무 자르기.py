import sys


# 나무 M미터 필요, 절단기 높이 H 지정. 각 나무 - H에 해당하는 길이 가져감
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
# 결정 문제 -> 파라미터 서치
# H 값이 커질수록 가져갈 수 있는 길이 짧아짐.
# O^2 안됨
n,m = map(int, input().split())
data = list(map(int, input().split()))

left, right = 1, max(data) + 1

def is_possible(H):
    result = 0
    for i in range(n):
        if data[i] - H > 0:
            result += data[i] - H
    return result >= m # 적어도 M 길이만큼 가능

while left < right:
    mid = (left + right) // 2

    if is_possible(mid): # 최댓값이라서 !
        left = mid + 1
    else:
        right = mid

print(left - 1)

