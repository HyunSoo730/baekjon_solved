import sys


# 시험지를 반드시 순서대로 제출하라는 규칙.
# 시험지를 현재 순서 그대로 k개의 그룹으로 나눈 뒤
# 각각의 그룹에서 맞은 문제 개수의 합을 구하여 그 중 최솟값을 시험 점수로 하기
# 받을 수 있는 최대 점수 계산

n,k = map(int, input().split()) # 시험지 개수 n, 그룹 수 k
data = list(map(int, input().split()))

# 최적화 : 받을 수 있는 점수의 최댓값
# 결정 : 최대점수 X점 이상으로 K개 이상으로 가능한가 ? (k개 이상이 된다면 k개도 된다.)

def is_possible(score): # 해당 점수로 k개 이상 그룹 만들 수 있는가 ?
    cnt = 0 # 그룹 개수
    total_score = 0
    for i in range(n):
        if total_score + data[i] < score:
            total_score += data[i]
        else:
            cnt += 1
            total_score = 0 # 초기화
    return cnt >= k


left, right = min(data), sum(data) + 1 # 최악은 k=1 즉 전부다 가능
while left < right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
    else:
        right = mid

print(left -1)
