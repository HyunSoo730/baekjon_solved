import sys

input = sys.stdin.readline


n = int(input())
data = []
for _ in range(n):
    r,g,b = map(int, input().split())
    data.append((r,g,b))

#모든 집을 칠하는 비용의 최솟값
#dp 테이블에는 각 색깔을 칠했을 떄의 최솟값을 저장하자.
dp = [[0] * 3 for _ in range(n)] 
dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2] #자명한건 미리 초기화

for i in range(1,n): #각 색깔별로 구해야.
    #현재 j번째 색을 칠할 때, 최솟값을 저장해야 하니까 아래와 같이 작성해야함.
    dp[i][0] = min(dp[i-1][1] + data[i][0], dp[i-1][2] + data[i][0]) 
    dp[i][1] = min(dp[i-1][0] + data[i][1], dp[i-1][2] + data[i][1])
    dp[i][2] = min(dp[i-1][0] + data[i][2], dp[i-1][1] + data[i][2])
    
res = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

print(res)