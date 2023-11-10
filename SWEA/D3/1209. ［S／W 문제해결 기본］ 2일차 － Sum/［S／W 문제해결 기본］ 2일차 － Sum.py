

def maxSum(data):
    res = 0
    # 가로 세로 최대
    row_max = 0 # 행 최대
    col_max = 0 # 열 최대
    for i in range(100):
        sumA = 0
        sumB = 0
        for j in range(100):
            sumA += data[i][j]
            sumB += data[j][i]
        row_max = max(row_max, sumA)
        col_max = max(col_max, sumB)
    # 대각선 최대
    d1_max = 0
    d2_max = 0
    for i in range(100):
        d1_max += data[i][i]
        d2_max += data[i][100-i-1]
    return max(row_max, col_max, d1_max, d2_max)


T = 10
for t in range(1,T+1):
    ss = int(input())
    data = [list(map(int ,input().split())) for _ in range(100)]
    MAX = maxSum(data)
    print(f"#{t} {MAX}")
