
T = int(input())
for t in range(1,T+1):
    n = int(input())
    data = [0] + list(map(int, input().split()))

    dp = [0] * (n+1)
    for i in range(1,n+1): # ! n개 모두 확인
        max_length = 0
        for j in range(i-1, 0, -1): # * i-1 ~ 1번까지 순차적으로 확인
            if data[i] > data[j] and dp[j] > max_length:
                max_length = dp[j]
        dp[i] = max_length + 1
    print(f"#{t} {max(dp)}")
