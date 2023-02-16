import sys


T = int(input())
#n을 1,2,3의 합으로 나타내는 방법의 수
for _ in range(T):
    n = int(input())
    dp = [0] * (100) #dp[i]는 i값을 만드는데 필요한 1,2,3 방법 개수
    dp[1] = 1 
    dp[2] = 2
    dp[3] = 4   #자명한 것들 미리 초기화
    for i in range(4,n+1): #마지막 항이 1,2,3으로 끝날때는 생각?
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
