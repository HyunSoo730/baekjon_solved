import sys

sys.setrecursionlimit(10**6)

#한 계단 or 두 계단
#연속된 세 개의 계단을 밟을 순 없다
#도착 계단은 밟아야 한다.

n = int(input())
data =[-1] #1번 인덱스부터 사용하기 위해.
for _ in range(n):
    data.append(int(input()))
if n == 1:
    print(data[1])
    sys.exit(0)
dp = [0] * (301) #dp 테이블은 그래도 좀 많이 만들어놓고 풀자
dp[1] = data[1]
dp[2] = data[1] + data[2] #자명한 사실.
for i in range(3,n+1):
    caseA = dp[i-3] + data[i-1] + data[i]
    caseB = dp[i-2] + data[i]
    dp[i] = max(caseA, caseB)

print(dp[n])