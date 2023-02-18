import sys


#1x2 2x1 2x2 총 3개 타일 존재
n = int(input())
#dp[i]는 2xi 직사각형을 채우는 방법의 수
dp = [0] * 1001
dp[1] = 1 #자명
dp[2] = 3 # 각각 한번씩 써서

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n] % 10007)
