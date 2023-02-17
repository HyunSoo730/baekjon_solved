import sys

input = sys.stdin.readline

#내려갈때마다 대각선 왼쪽 or 대각선 오른쪽만 선택
#현재층의 i번째 인덱스면 다음층의 i, i+1 둘중하나 선택가능
#현재의 선택이 미래에 영향. 그리디 x dp로 풀어야함

n = int(input())
dp = [[0] * 501 for _ in range(n+1)]
data = [[0]]
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.insert(0,0)
    data.append(temp)

dp[1][1] = data[1][1] #1층 1번 인덱스 자명한건 미리 초기화
res = 0
for i in range(2,n+1): #2번째 층부터 탐색.
    for j in range(1,i+1):
        if j == 1:
            dp[i][j] = dp[i-1][1] + data[i][1]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + data[i][j]
        else:
            caseA = dp[i-1][j-1] + data[i][j]
            caseB = dp[i-1][j] + data[i][j]
            dp[i][j] = max(caseA, caseB)

for i in range(1,n+1):
    res = max(dp[n][i], res)
    
print(res)

