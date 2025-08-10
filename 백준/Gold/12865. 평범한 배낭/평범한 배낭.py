import sys

# 배낭 문제 -> 냅색 알고리즘
# N개의 물건, 각 물건은 무게 W, 가치 V, 최대 K만큼의 무게만 가능

n,k = map(int, input().split())
data = []
for _ in range(n):
    w,v = map(int, input().split())
    data.append((w,v))

# 1차원 DP로 해결
dp = [0] * (k+1)
# dp[w] : 무게 w 이하일 때 최대 가치

for weight, value in data: # 하나씩 확인
    # 뒤에서부터 업데이트 (중복 방지)
    for w in range(k, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight] + value)

print(dp[k])
