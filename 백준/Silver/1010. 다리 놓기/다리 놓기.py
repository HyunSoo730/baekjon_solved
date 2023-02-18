import sys


#조합 값.
T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    #m combination n 구하기
    dp = [0] * 50
    dp[0] = 1
    dp[m] = 1 #자명한 것
    for i in range(1,n+1):
        dp[i] = dp[i-1] * (m+1-i) // i
    print(dp[n])
    