import sys

N = int(input())
dp = [0] * (N+1)

#방법이 3가지이기 때문에 그리디로 풀 수 없음 dp로 해야함
#1번 인덱스부터 사용.
# 3가지 방법 모두 구해보고 최솟값 채택.
for i in range(2,N+1):
    dp[i] = dp[i-1] + 1 #1을 뺴는 경우
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)   #1을 뺴는 것과 3으로 나누는 것중에 최솟값 채택
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])