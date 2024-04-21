import sys

n = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 2
# dp[i]는 2*i를 채우는데 필요한 방법의 수

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n] % 10007)