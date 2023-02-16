import sys

input = sys.stdin.readline
#세로 x 가로
#작은 문제를 점진적으로 확장. 보자마자 dp
n = int(input())
dp = [0] * (10001) #dp[i]는 2xi를 채우는 방법의 수
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
