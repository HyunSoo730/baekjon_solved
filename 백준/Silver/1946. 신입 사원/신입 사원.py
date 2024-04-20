import heapq
import sys

# 1차 -> 2차
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발.
# 기준 2개. 하나 정렬 후 확인
# 선발 최대인원

def solve():
    global data
    cnt = 0
    prev_data = int(1e9)
    for i in range(n):
        if data[i][0] < prev_data:
            cnt += 1
            prev_data = data[i][0]
    return cnt

T = int(input())
for _ in range(T):
    n = int(input())
    data = []
    for _ in range(n):
        a,b = map(int, input().split())
        data.append((a,b)) # 기준 A 기준 B

    data.sort(key = lambda x : x[1]) # 오름차순 -> 순위라서
    # print(data)
    res = solve()
    print(res)