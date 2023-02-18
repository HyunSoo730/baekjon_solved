import sys


n = int(input())
#인접한 수
dp = [[0] * 101 for _ in range(n+1)]
dp[1][0] = 0
for i in range(1,10):
    dp[1][i] = 1
#자명한건 미리 초기화

for i in range(2,n+1):
    dp[i][0] = dp[i-1][1] #0이 맨 뒤에 오려면 무조건 앞에 1이 있어야.
    dp[i][9] = dp[i-1][8] #9가 맨 뒤에 오려면 무조건 앞에 8이 있어야.
    for j in range(1,9): #1~8은 양쪽 대각선 모두 존재하니깐
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

res = sum(dp[n][:10]) #길이가 n이니까 n번째 자리수의 0으로 끝나는거부터 9로 끝나는거까지 총 가짓수 더하면 돼
print(res % 1000000000)

        
