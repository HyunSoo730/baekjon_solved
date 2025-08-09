import sys


# 연속합.
# n개의 정수. 연속된 몇개의 수를 선택해서 가장 큰 합 만들기
# n 10^5 -> N^2 안됨

# dp[i] : i번쨰 원소를 포함하는 최대 연속합.
n = int(input())
data = list(map(int, input().split()))
dp = [-int(1e9)] * 100000

dp[0] = data[0] # 당연 : 첫 시작은 무조건
for i in range(1,n):
    dp[i] = max(dp[i-1] + data[i], data[i])

res = max(dp)
print(res)