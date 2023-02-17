import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 가장 긴 증가하는 부분 수열 = 최장 부분 증가수열
n = int(input())
data = list(map(int, input().split()))
data.insert(0,-1)
dp = [0] * (n+1)
dp[1] = 1 #자명한 사실

for i in range(2,n+1):
    max_length = 0
    for j in range(1,i): #본인 앞에까지 중에
        if dp[j] > max_length and data[j] < data[i]: #앞에 숫자가 작아야 현재 숫자가 그 뒤에 붙을 수 있지
            max_length = dp[j]
    dp[i] = max_length + 1

print(max(dp))
            
