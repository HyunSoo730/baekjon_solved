import sys

# input = sys.stdin.readline

#현재 선택한 방법이 다음번에 영향을 끼치네. 그리디가 아닌 dp로
#n이 1이되는데 걸리는 최소 횟수..
n = int(input())
INF = 24242424
dp = [INF] * (n+1)
dp[1] = 0 #자명한건 미리 초기화.

#자명한건 미리 초기화

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 #1을 빼는 것을 확정적으로 하고 
    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
    if i%3==0:
        dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[n])