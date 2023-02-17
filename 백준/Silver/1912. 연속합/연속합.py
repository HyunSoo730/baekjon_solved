import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [-1001] * n
dp[0] = data[0]

for i in range(1,n):
    dp[i] = max(dp[i-1] + data[i], data[i])

#dp에 이제 연속된 수 중 최댓값이 저장되어 있을 것.
#이 중에 최댓값을 구하면 됨.
print(max(dp))
    