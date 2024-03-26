import sys

n,m = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

INF = int(1e9)

dp = [INF] * (sum(memories)+1) # ! dp[i]는 i만큼의 메모리를 사용할 때 드는 최소 비용
dp[0] = 0
for i in range(1,n+1):
    # ! 메모리 사용량을 역순으로 반복하면서 DP 테이블 업데이트
    for memory in range(sum(memories), memories[i]-1, -1):
        dp[memory] = min(dp[memory], dp[memory-memories[i]] + costs[i])

res = min(dp[m:])
print(res)