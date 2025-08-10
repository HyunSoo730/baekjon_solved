import sys

# 배낭 문제 -> 냅색 알고리즘
# N개의 물건, 각 물건은 무게 W, 가치 V, 최대 K만큼의 무게만 가능

n,k = map(int, input().split())
data = []
for _ in range(n):
    w,v = map(int, input().split())
    data.append((w,v))

dp = [[0] * (k+1) for _ in range(n+1)]
# dp[i][w] : i번째 물건까지 고려, 무게 w이하일 때 최대 가치

for i in range(1, n+1):
    weight, value = data[i-1]
    for w in range(k+1):
        # 현재 i번째 물건을 안 넣는 경우
        dp[i][w] = dp[i-1][w]
        # i번째 물건을 넣을 수 있고, 넣는 게 유리한 경우
        if w >= weight: # 넣을 수 있다면 더 좋은지 확인(이 조건이 있어야함 : 없으면 음수 인덱스 발생) -> 더 좋은쪽 선택 : max(현재값, 넣는경우값)
            # dp[i-1][w-weight] + value의 의미 : dp[i-1][w-weight] : 현재 물건의 무게만큼 여유를 남겨두고, 이전 물건들로 얻을 수 있는 최대가치
            # +value : 그 여유 공간에 현재 물건을 넣었을 때의 추가 가치
            dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)

print(dp[n][k])
