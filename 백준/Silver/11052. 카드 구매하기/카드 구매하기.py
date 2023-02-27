import sys



n = int(input())
data = list(map(int, input().split()))

#n개를 갖기 위해 지불해야 하는 금액의 최댓값
data.insert(0,-1)
dp = [0] * (n+1)
#dp[i]는 i개의 카드를 살 때 지불하는 최댓값.
dp[1] = data[1] #1개를 뽑는데는 자명하게 1개 카드팩
for i in range(1,n+1):
    cnt = i
    val = data[i]
    for j in range(cnt, n+1):
        caseA = dp[j] #기존에 j개의 카드를 살 때의 최댓값
        caseB = dp[j-cnt] + val #cnt개의 카드팩을 살떄 가격
        dp[j] = max(caseA, caseB)

print(dp[n])