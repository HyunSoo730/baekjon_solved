import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

data = []
n, limit = map(int, input().split()) #보석 종류, 무게 한계값
for _ in range(n):
    a,b = map(int, input().split())
    data.append((a,b)) #무게, 가치
data.insert(0,(0,0)) #0번 인덱스 사용안함
dp = [[0] * (limit+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,limit + 1):
        weight = data[i][0] # 현재 물건 무게
        value = data[i][1] # 현재 물건 가치

        if j < weight: #현재 물건 담을 수 없으니 이전꺼 가져와야함
            dp[i][j] = dp[i-1][j]
        else: #현재 물건 담을 수 있음
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])

print(dp[n][limit])