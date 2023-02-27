import sys

T = int(input())
dp = [0] * 100
dp[1] = 1
dp[2] = 2
dp[3] = 4 #자명한 것.
for _ in range(T):
    n = int(input())
    if dp[n] > 0: #이미 있음
        print(dp[n])
        continue
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])
    