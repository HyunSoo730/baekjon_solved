import sys
n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

#동전의 최대 값 k == 10000 이걸 맥스로 dp 사용
max_val = 10001
dp = [max_val] * (k + 1)
dp[0] = 0 #처음부터 알 수 있는 값
#dp[n]은 동전 리스트에서 n원을 만들었을 때 최소가 되는 동전의 개수


for x in data:
    for i in range(x, k+1):
        if dp[i] > 0: #값을 가지고 있어야 판단
            dp[i] = min(dp[i-x]+ 1, dp[i])

if dp[k] == max_val:
    print(-1)
else:
    print(dp[k])
