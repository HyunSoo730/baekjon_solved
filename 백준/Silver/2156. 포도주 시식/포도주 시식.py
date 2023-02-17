import sys

input = sys.stdin.readline

#연속 세잔 마실 수 없음
#dp[i]는 i번째까지 마실 때 최대로 마실 수 있는 최대값 저장
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.insert(0,0) #1번 인덱스부터 사용하기 위해.
if n == 1:
    print(data[1])
    exit(0)
dp = [0] * 10001
dp[1] = data[1]
dp[2] = data[1] + data[2]
#dp[i]는 i번째 음료수를 마실 떄의 최댓값.
#이 문제는 마지막 잔을 안마셔도 되는거였어. 그렇기에... 3가지 경우가 존재했다.
#즉 현재 잔을 마시지 않을 경우도 생각했어야 했다 !!!
for i in range(3, n+1):
    caseA = dp[i-2] + data[i]
    caseB = dp[i-3] + data[i-1] + data[i]
    caseC = dp[i-1]
    dp[i] = max(caseA, caseB, caseC)
print(dp[n])




